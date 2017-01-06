#from pyvx.backend.sample import ffi, lib
from pyvx.backend import ffi, lib
import os
import re

assert '256' == str(lib.VX_MAX_KERNEL_NAME) # Hardcoded in build_cbackend

vx_fd = open(os.path.join('pyvx', '_auto_vx.py'), 'w')
vx_fd.write("from pyvx.backend import lib, ffi\n")
for n in dir(lib):
    if n[:3].upper() == 'VX_':
        vx_fd.write("%s = lib.%s\n" % (n[3:], n))

vxu_fd = open(os.path.join('pyvx', '_auto_vxu.py'), 'w')
vxu_fd.write("from pyvx.backend import lib, ffi\n")

# TODO: use directory of implementation library ?
# TODO: obtain this data from CLang ?
api = open("pyvx/cdefs/vx_api.h").read() + open("pyvx/cdefs/vx_nodes.h").read() + open("pyvx/cdefs/vxu.h").read()
for entry in api.split('/*!'):
    if 'VX_API_ENTRY' not in entry:
        continue
    doc, entry = entry.split('VX_API_ENTRY')
    i = entry.find(';')
    entry = entry[:i].strip()
    name, args = entry.split('(')
    fullname = re.split(r'\s+', name.strip())[-1]
    assert fullname[:2] == 'vx'
    assert args[-1] == ')'
    args = args[:-1]
    args = args.replace('[VX_MAX_KERNEL_NAME]', '[]')
    args = [re.split(r'\s+', a.strip())[-1] for a in args.split(',')]
    if args[-1] == '...':
        args.pop()

    doc = doc.strip()
    assert doc[-2:] == '*/'
    doc = doc[:-2]
    doc = re.sub(r'^\s*\*\s+', '', doc, 0, re.MULTILINE) # remove asterisk and whitespace introducing lines
    lines = []
    for line in doc.splitlines():
        if len(lines) == 0 or len(line) > 0 and line[0] == '\\':
            lines.append(line)
        else:
            lines[-1] += ' ' + line
    lines2 = []
    for line in lines:
        # Markers
        line = re.subn(r'\*', r'\*', line)[0] # "neutralize" asterisks
        #line = re.subn(r':', r'\:', line)[0] # ditto for colons
        line = re.subn(r'\\ref\s+', '', line)[0]  # remove \ref markers
        line = re.subn(r'\\brief\s+(.*)', r'\1', line)[0]
        line = re.subn(r'\\param\s+(\[[^\]]+\])\s+([^\s]+)\s+(.*)', r' :\2: \1 \3', line)[0]
        line = re.subn(r'\\arg\s(.[^\: ]+)\s*\:(.*)', r'\n  :\1: \2', line)[0] # Special form introducing values
        line = re.subn(r'\\arg\s(.*)', r'\n  \1', line)[0] # General form
        line = re.subn(r'\\return\s+(.*)', r':Returns: \1', line)[0]
        line = re.subn(r'\\retval\s+([^\s]+)\s+(.*)', r'\n  :\1: \2', line)[0] # :Return value: \1', line)[0]
        line = re.subn(r'\\pre\s+(.*)$', r':Precondition: \1', line)[0]  # Precondition
        line = re.subn(r'\\post\s+(.*)$', r':Postcondition: \1', line)[0] # Postcondition
        line = re.subn(r'\\a\s+([^\s]+)', r'*\1*', line)[0]  # emphasis; TODO: more doxygen tags?
        line = re.subn(r'\\f\$\s+(.*?)\s+\\f\$', r':math:`\1`', line)[0]  # inline math
        line = re.subn(r'\\ingroup\s+(.*)$', r':In group: \1', line)[0]  # degrade to text
        line = re.subn(r'\\see\s+(.*)$', r':See: \1', line)[0]  # degrade to text
        line = re.subn(r'\\note\s+(.*)$', r':Note: \1', line)[0]  # degrade to text
        #line = re.subn(r'\\([^\s]+)\s+(.*)', r' :\1: \2', line)[0] # any tags not caught above
        line = re.subn(r'<\/?tt>', r'*', line)[0]  # replace "typewriter" tags with asterisks *
        lines2.append(line)
    doc = '\n'.join(lines2)

    args = ', '.join(a.strip(' []*') for a in args)

    if fullname[:3] == 'vxu':
        name = fullname[3:]
    else:
        name = fullname[2:]

    func = """
def %s(%s):
    '''
%s
    '''
    return lib.%s(%s)
    """ % (name, args, doc, fullname, args)
    if fullname[:3] == 'vxu':
        vxu_fd.write(func)
    else:
        vx_fd.write(func)



