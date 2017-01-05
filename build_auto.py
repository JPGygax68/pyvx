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
    assert args[-1] == ')'
    args = args[:-1]
    args = args.replace('[VX_MAX_KERNEL_NAME]', '[]')
    args = [re.split(r'\s+', a.strip())[-1] for a in args.split(',')]
    if args[-1] == '...':
        args.pop()

    doc = doc.strip()
    assert doc[-2:] == '*/'
    doc = doc[:-2]
    #doc = re.sub(r' \*[ \/]?', '', doc) # remove asterisk in front of comment lines, and at end */
    doc = re.sub(r'^\s+\*\s+', '', doc, 0, re.MULTILINE) # remove asterisk and whitespace introducing lines
    lines = []
    for line in doc.splitlines():
        para = line[0] == '\\'
        # Markers
        line = re.subn(r'\\ref\s+', '', line)[0]  # remove \ref markers
        line = re.subn(r'\\brief\s+(.*)', r'\1', line)[0]
        line = re.subn(r'\\param\s+(\[[^\]]+\])\s+([^\s]+)\s+(.*)', r' :param \2: \1 \3', line)[0]
        line = re.subn(r'\\return\s+(.*)', r':return: \1', line)[0]
        line = re.subn(r'\\retval\s+(.*)', r':retval: \1', line)[0]
        line = re.subn(r'\\a\s+([^\s]+)', r'*\1*', line)[0] # emphasis; TODO: more doxygen tags?
        line = re.subn(r'\\([^\s]+)\s+(.*)', r' :\1: \2', line)[0]
        line = re.subn(r'<\/?tt>', r'*', line)[0]  # replace "typewriter" tags with asterisks *
        if para or len(lines) == 0:
            lines.append(line)
        else:
            lines[-1] += ' ' + line
    doc = '\n'.join(lines)

    fullname = re.split(r'\s+', name.strip())[-1]
    assert fullname[:2] == 'vx'
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



