import os
import re
import sys
import distutils.ccompiler as cc
from distutils.msvccompiler import MSVCCompiler
from distutils.errors import DistutilsExecError, DistutilsPlatformError, CompileError

from cffi import FFI

from pyvx import __backend_version__

from .api_filter import *

mydir = os.path.dirname(os.path.abspath(__file__))

DEFS = {"VX_API_ENTRY": '', "VX_API_CALL": '', "VX_CALLBACK": ''}

def build(name, openvx_install, default):
    pwd = os.getcwd()
    os.chdir(os.path.dirname(mydir))
    assert name != 'default'

    hdr = os.path.join(openvx_install, 'include', 'VX', 'vx.h')
    if not os.path.exists(hdr):
        print("ERROR: Can't find header", hdr)
        exit(-1)

    bindir = os.path.join(openvx_install, 'bin')
    libdir = os.path.join(openvx_install, 'lib')
    incdir = os.path.join(openvx_install, 'include')
    
    lib = next(lib for lib in ['libopenvx', 'VisionWorks'] 
        if  any(os.path.exists(os.path.join(bindir, lib) + '.'+ext) for ext in ['so', 'dll'])
        and any(os.path.exists(os.path.join(libdir, lib) + '.'+ext) for ext in ['lib', 'a' ]) )
    print('Found OpenVX library: %s' % lib)
    libs = [lib] + (['vxu'] if lib != 'VisionWorks' else []) 
    print("libs: {}".format(libs))

    apifilter = APIFilter([os.path.join(incdir, "VX", "vx.h")], include_dirs = [incdir], ppdefs = DEFS)

    ffi = FFI()
    
    if True:

        def get_token(t) -> Token:
            return DEFS[t.spelling] if t.spelling in DEFS else t.spelling
            return t

        code = ''
        for c in apifilter.tu.cursor.get_children():
            #print("Name: {}, kind: {}".format(c.displayname, c.kind))
            if c.kind == CursorKind.ENUM_DECL:
                #defs += "enum %s {\n" % c.displayname
                #for v in c.get_children():
                #    defs += "    %s = ...,\n" % v.displayname
                #defs += "};\n"
                s = ' '.join([get_token(t) for t in c.get_tokens() if t.kind != TokenKind.COMMENT])
                code += s + "\n"
            elif c.kind == CursorKind.TYPEDEF_DECL:
                #s = ' '.join([get_token(t) for t in c.get_tokens() if t.kind != TokenKind.COMMENT])
                print(c.displayname)
                for c in c.get_children():
                    print("child: %s" % c.displayname)
                #print(s)
                code += s + "\n"
            else:
                #print("name: %s, kind: %s" % (c.displayname, c.kind))
                pass
        exit(-1)
        print(code)
        ffi.cdef(code)
        exit(-1)

        # Metadata query declarations
        ffi.cdef('''
            char *_get_FMT_REF(void);
            char *_get_FMT_SIZE(void);
            int _get_KERNEL_BASE(int vendor, int lib);
            char *_get_backend_version();
            char *_get_backend_name();
            char *_get_backend_install_path();
        ''')

        #exit(-1)
        
    if False:
        # TODO: the following is not necessarily correct - should be extracted from include files?
        code= dict(VX_API_ENTRY='', VX_API_CALL='', VX_CALLBACK='', VX_MAX_KERNEL_NAME='256')
        if os.name == 'nt':
            code['VX_API_CALL'] = '__stdcall'
            code['VX_CALLBACK'] = '__stdcall'

        # vx.h
        if True:
            vx = open(os.path.join(mydir, "cdefs", "vx.h")).read()
            #vx = get_and_cleanup_header_file(os.path.join(incdir, "VX", "vx.h"))
            #print("vx.h:\n{}".format(vx))
            ffi.cdef(vx)

        # vx_vendors.h
        if True:
            vendors = open(os.path.join(mydir, "cdefs", "vx_vendors.h")).read()
            #vendors = get_and_cleanup_header_file(os.path.join(incdir, "VX", "vx_vendors.h"))
            #print("Vendors:\n{}".format(vendors))
            ffi.cdef(vendors)

        # vx_types.h
        if True:
            #types = open(os.path.join(mydir, "cdefs", "vx_types.h")).read()
            types = get_and_cleanup_header_file("vx_types.h")
            for k,v in code.items():
                types = types.replace(k, v)
            # The following only works because
            #types = re.subn(r'(#if defined\(EXPERIMENTAL_PLATFORM_SUPPORTS_16_FLOAT\).*?#endif)', 
            #    r'', types, 0, re.DOTALL|re.MULTILINE)[0]
            #types = re.subn(r'(typedef)\s+((?:struct\s+)[^\s]+)\s+(.*);', r'\1 ... \3;', types)[0]
            #typedef vx_action (VX_CALLBACK *vx_nodecomplete_f)(vx_node node);
            #types = re.subn(r'typedef\s+[^\(]+\([^\*]+\*([^\)]+)\)\s*\([^\)]*\);', r'typedef ... \1;', types)[0]
            #print("vx_types.h:\n%s" % types)
            #open(os.path.join(mydir, "pp_vx_types.h"), "w").write(types)
            ffi.cdef(types)
        
        # vx_kernels.h
        if False:
            #kernels = open(os.path.join(mydir, "cdefs", "vx_kernels.h")).read()
            kernels = get_and_cleanup_header_file(os.path.join(incdir, "VX", "vx_kernels.h"))
            #kernels = re.subn(r'=.*,', r'= ...,', kernels)[0] # Remove specifics from enums
            print("vx_kernels.h\n%s" % kernels)
            ffi.cdef(kernels)

        # vx_api.h
        if False:
            #api = open(os.path.join(mydir, "cdefs", "vx_api.h")).read()
            api = get_and_cleanup_header_file(os.path.join(incdir, "VX", "vx_api.h"))
            for k, v in code.items():
                api = api.replace(k, v)
            ffi.cdef(api)

        # vx_nodes.h
        if False:
            #nodes = open(os.path.join(mydir, "cdefs", "vx_nodes.h")).read()
            nodes = get_and_cleanup_header_file(os.path.join(incdir, "VX", "vx_nodes.h"))
            for k, v in code.items():
                nodes = nodes.replace(k, v)
            ffi.cdef(nodes)

        # vxu.h
        if False:
            #vxu = open(os.path.join(mydir, "cdefs", "vxu.h")).read()
            vxu = get_and_cleanup_header_file(os.path.join(incdir, "VX", "vxu.h"))
            for k, v in code.items():
                vxu = vxu.replace(k, v)
            ffi.cdef(vxu)

    if True:
        ffi.set_source("pyvx.backend.%s" % name, 
            """
                #include <VX/vx.h>
                //#include <VX/vx_compatibility.h>
                #include <VX/vxu.h>
                char *_get_FMT_REF(void) {return VX_FMT_REF;}
                char *_get_FMT_SIZE(void) {return VX_FMT_SIZE;}
                int _get_KERNEL_BASE(int vendor, int lib) {return VX_KERNEL_BASE(vendor, lib);}
                char *_get_backend_version() {return "%s";}
                char *_get_backend_name() {return "%s";}
                char *_get_backend_install_path() {return "%s";}
            """ % (__backend_version__.decode("utf8"), name.replace('\\', '\\\\'), openvx_install.replace('\\', '\\\\')),
           include_dirs=[os.path.join(openvx_install, 'include')],
           library_dirs=[os.path.join(openvx_install, 'lib')],
           #extra_link_args=['-Wl,-rpath=' + os.path.abspath(os.path.join(openvx_install, 'bin'))],
           libraries=libs)
        
        ffi.compile()
        
        default_file_name = os.path.join('pyvx', 'backend', '_default.py')
        if default or not os.path.exists(default_file_name):
            fd = open(default_file_name, 'w')
            fd.write("from pyvx.backend.%s import ffi, lib\n" % name)
            fd.close()

            import pyvx.backend as backend
            assert backend.ffi.string(backend.lib._get_backend_version()) == __backend_version__
            assert backend.ffi.string(backend.lib._get_backend_name()).decode("utf8") == name
            assert backend.ffi.string(backend.lib._get_backend_install_path()).decode("utf8") == openvx_install

        names = {}
        exec("import pyvx.backend.%s as backend" % name, names)
        backend = names['backend']
        assert backend.ffi.string(backend.lib._get_backend_version()) == __backend_version__
        assert backend.ffi.string(backend.lib._get_backend_name()).decode("utf8") == name
        assert backend.ffi.string(backend.lib._get_backend_install_path()).decode("utf8") == openvx_install

        print('')
        print("Successfully built backend pyvx.backend.%s in %s" % (name, mydir))
        print('')
        

#_RE_REMOVE_COMMENTS = re.compile(r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"', re.DOTALL|re.MULTILINE)
_RE_REMOVE_COMMENTS = re.compile(r'/\*.*?\*/', re.DOTALL|re.MULTILINE)

def get_and_cleanup_header_file(filename):
    IDENTIFIER = '[_A-Za-z][_A-Za-z0-9]*'
    FLOAT = '[+-]?[0-9]*(?:\.[0-9]+)[fd]?' # TODO: e...
    
    code = open(os.path.join(mydir, "cdefs", filename)).read()
    code = re.subn(_RE_REMOVE_COMMENTS, '', code)[0]
    #code = re.subn(r'#ifdef\s+__cplusplus\b.*#endif\b', r'', code, 0, re.DOTALL|re.MULTILINE)[0]
    #code = re.subn(r'(#\s*ifn?def\s+[^\s]+)', r'//\1', code)[0] # Remove preproc conditionals (old style)
    #code = re.subn(r'(#\s*if\s+.*)', r'//\1', code)[0] # Remove preproc conditionals (new style)
    #code = re.subn(r'(#\s*else\b.*)', r'//\1', code)[0] # "
    #code = re.subn(r'(#\s*end\b.*)', r'//\1', code)[0] # "
    #code = re.subn(r'(#\s*include\s+<[^\>]+>)', r'//\1', code)[0] # Remove directives
    #code = re.subn(r'(#\s*endif.*)', r'//\1', code)[0] # Remove directives
    #code = re.subn(r'(#\s*define\s+[^\s]+.*)', r'//\1', code)[0] # Remove all #define's
    code = re.subn(r'(#\s*define\s+'+IDENTIFIER+'\s+)\((0x[0-9A-Fa-f]+|[0-9]+u?|'+FLOAT+')\)', r'\1\2', code)[0]
    
    return code

if __name__ == '__main__':
    args = sys.argv[1:]
    default = '--default' in args
    if default:
        args.remove('--default')
    if len(args) == 2:
        name, openvx_install = args
        build(name, openvx_install, default)
    else:
        print("Usage: %s [--default] <name> <openvx install path>" % sys.argv[0])
