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

# TODO: extract VX_MAX_KERNEL_NAME from actual header files
DEFS = {"VX_API_ENTRY": '', "VX_API_CALL": '__cdecl', "VX_CALLBACK": '__cdecl', "VX_MAX_KERNEL_NAME": '256'}
#DEFS = {"VX_API_ENTRY": '', "VX_API_CALL": '', "VX_CALLBACK": '', "VX_MAX_KERNEL_NAME": '256'}

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

    ffi = FFI()

    vx_file  = os.path.join(incdir, "VX", "vx.h" )
    vxu_file = os.path.join(incdir, "VX", "vxu.h")

    apifilter = APIFilter([vx_file], r'^(vx[A-Z_]|VX_).*$', include_dirs = [incdir], ppdefs = DEFS)
    vx_code = apifilter.get_api_declaration()
    #print("Preprocessor definitions:\n%s" % '\n'.join('%s %s' % (k, v) for k, v in apifilter.ppdefs.items()))
    #code += '\n' + '\n'.join(["#define %s %s" % (k, v) for k, v in DEFS.items() if re.match(r'[0-9]+', v)])
    # Remove parentheses and keep only integer definitions
    vx_code += '\n' + '\n'.join(apifilter.get_simple_macro_definitions())
    print("vx.h code:\n%s" % vx_code)
    ffi.cdef(vx_code)

    apifilter = APIFilter([vxu_file], r'^vxu[A-Z_].*$', include_dirs=[incdir], ppdefs = DEFS, include_before=[vx_file])
    vxu_code = apifilter.get_api_declaration()
    #vxu_code += '\n' + '\n'.join(apifilter.get_simple_macro_definitions())
    print("vxu.h code:\n%s" % vxu_code)
    ffi.cdef(vxu_code)

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
