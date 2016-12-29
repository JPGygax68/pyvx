import os
import re
import sys
import distutils.ccompiler as cc
from distutils.msvccompiler import MSVCCompiler
from distutils.errors import DistutilsExecError, DistutilsPlatformError, CompileError
#from tempfile import gettempdir
#from pycparser import preprocess_file #, parse_file
#from pycparser import parse_file
from cpip.core import PpLexer, IncludeHandler
from pycparser.c_parser import CParser

from cffi import FFI

from pyvx import __backend_version__

mydir = os.path.dirname(os.path.abspath(__file__))

class MyMSVCCompiler(MSVCCompiler):
    
    #def compile(self, *args, **kwargs):
    #    print("It's me!")
    #    super().compile(*args, **kwargs)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initialize()
        
    def preprocess(self, source):
        try:
            #self.spawn([self.cc, '/E', '/Tc'+source] + ["-I%s" % dir for dir in self.include_dirs])
            return _popen([self.cc, '/E', '/Tc'+source] + ["-I%s" % dir for dir in self.include_dirs]).read()
        except DistutilsExecError as msg:
            raise CompileError(msg)
        

# Ripped and adapted from distutils/spawn.py

def _popen(cmd, search_path=1, verbose=0, dry_run=0):
    executable = cmd[0]
    cmd = _nt_quote_args(cmd)
    #if search_path:
    #    # either we find one or it stays the same
    #    executable = find_executable(executable) or executable
    #log.info(' '.join([executable] + cmd[1:]))
    return os.popen(' '.join(cmd))

# Verbatim from distutils/spawn.py

def _nt_quote_args(args):
    """Quote command-line arguments for DOS/Windows conventions.

    Just wraps every argument which contains blanks in double quotes, and
    returns a new argument list.
    """
    # XXX this doesn't seem very robust to me -- but if the Windows guys
    # say it'll work, I guess I'll have to accept it.  (What if an arg
    # contains quotes?  What other magic characters, other than spaces,
    # have to be escaped?  Is there an escaping mechanism other than
    # quoting?)
    for i, arg in enumerate(args):
        if ' ' in arg:
            args[i] = '"%s"' % arg
    return args

# The following doesn't work because new_compiler() imports the compiler class on-the-fly        
#distutils.msvccompiler.MSVCCompiler = MyMSVCCompiler

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
    
    #if not os.path.exists(lib):
    #    print("ERROR: Can't find lib", lib)
    #    exit(-1)
    #libpaths = [os.path.join(openvx_install, 'bin', name) for name in ['libopenvx.so', 'VisionWorks.dll']]
    #if not any([os.path.exists(lib) for lib in libpaths]):
    #    print("Can't find a loadable library implementing OpenVX, tried: {}".format(libpaths))
    #    exit(-1)  
    
    lib = next(lib for lib in ['libopenvx', 'VisionWorks'] 
        if  any(os.path.exists(os.path.join(bindir, lib) + '.'+ext) for ext in ['so', 'dll'])
        and any(os.path.exists(os.path.join(libdir, lib) + '.'+ext) for ext in ['lib', 'a' ]) )
    print('Found OpenVX library: %s' % lib)
    libs = [lib] + (['vxu'] if lib != 'VisionWorks' else []) 
    print("libs: {}".format(libs))

    ffi = FFI()
    
    if False:
        # Parsing the header files may not be necessary after all
        #print(os.environ['ProgramFiles(x86)'])
        #cc.show_compilers()
        from distutils.ccompiler import CCompiler, new_compiler
        dflt_compiler = cc.get_default_compiler(os.name, sys.platform)
        compiler = MyMSVCCompiler() if dflt_compiler == 'msvc' else new_compiler()
        #print("compiler: {}".format(compiler))
        compiler.add_include_dir(os.path.join(mydir, 'fake_libc_include'))
        compiler.add_include_dir(os.path.join(openvx_install, 'include'))
        # define_macro doesn't appear to work
        #compiler.define_macro("__pragma(x)", "")
        #compiler.define_macro("__cdecl", "")
        #compiler.define_macro("__fastcall", "")
        #compiler.compile([hdr])
        code = compiler.preprocess(hdr)
        
    if True:
        inc_hndlr = IncludeHandler.CppIncludeStdOs([], [incdir, os.path.join(mydir, 'fake_libc_include')])
        lexer = PpLexer.PpLexer(hdr, inc_hndlr)
        #for tok in lexer.ppTokens():
        #    print(tok.t)
        code = ''.join([tok.t for tok in lexer.ppTokens()])
        #exit(-1)
        
    if False:
        code = re.subn(r'(^\w*$)+', r'', code, flags=re.MULTILINE)[0]
        code = re.subn(r'#line\s+.*', r'', code)[0] # Remove #line ... comments
        code = re.subn(r'__pragma.*', r'', code)[0] # Remove __pragma annotations
        code = re.subn(r'#pragma.*', r'', code)[0] # Remove __pragma directives
        code = re.subn(r'\b__cdecl\b', r'', code)[0] # Remove __cdecl
        code = re.subn(r'\b__stdcall\b', r'', code)[0] # Remove __stdcall
        code = re.subn(r'\b__declspec\(.*\)', r'', code)[0] # Remove __declspec(...)
                
    open("preproc_out.c", "w").write(code)

    if False:
        parser = CParser()
        ast = parser.parse(code)
        print("AST: \n");
        ast.show()
        #for child in ast.children():
        #    child.show()
        #exit(-1)
        
    if False:
        code = re.subn(r'(#line\s+.*)', r'//\1', code)[0] # Remove #line ... comments
        code = re.subn(r'(__pragma.*)', r'//\1', code)[0] # Remove __pragma directives
        code = re.subn(r'(__fastcall)', r'', code)[0] # __fastcall
        code = re.subn(r'(__declspec\(.*\))', r'', code)[0] # remove __declspec
        code = re.subn(r'(\b__int[^\s]*\b)', r'int...', code)[0]
        #code = re.subn(r'(\b__time32_t\b)', r'...', code)[0]
        #code = re.subn(r'(\b__time64_t\b)', r'...', code)[0]
        
    if True:
        ffi.cdef(code)
        
        ffi.set_source("pyvx.backend.%s" % name, 
            """
                #include <VX/vx.h>
                #include <VX/vx_compatibility.h>
                #include <VX/vxu.h>
                char *_get_FMT_REF(void) {return VX_FMT_REF;}
                char *_get_FMT_SIZE(void) {return VX_FMT_SIZE;}
                int _get_KERNEL_BASE(int vendor, int lib) {return VX_KERNEL_BASE(vendor, lib);}
                char *_get_backend_version() {return "%s";}
                char *_get_backend_name() {return "%s";}
                char *_get_backend_install_path() {return "%s";}
            """ % (__backend_version__.decode("utf8"), name, openvx_install),
           include_dirs=[os.path.join(openvx_install, 'include')],
           library_dirs=[os.path.join(openvx_install, 'bin')],
           extra_link_args=['-Wl,-rpath=' + os.path.abspath(os.path.join(openvx_install, 'bin'))],
           libraries=libs)
        ffi.compile()
        
        exit(-1)

    if False:
    
        ffi = FFI()
        
        # TODO: the following is not necessarily correct - should be extract from include files
        defs= dict(VX_API_ENTRY='', VX_API_CALL='', VX_CALLBACK='', VX_MAX_KERNEL_NAME='256')
        if os.name == 'nt':
            defs['VX_API_CALL'] = '__stdcall'
            defs['VX_CALLBACK'] = '__stdcall'

        # vx.h
        #vx = open(os.path.join(mydir, "cdefs", "vx.h")).read()
        vx = get_and_cleanup_header_file(os.path.join(incdir, "VX", "vx.h"))
        ffi.cdef(vx)

        # vx_vendors.h
        #ffi.cdef(open(os.path.join(mydir, "cdefs", "vx_vendors.h")).read())
        ffi.cdef( get_and_cleanup_header_file(os.path.join(incdir, "VX", "vx_vendors.h")) )

        # vx_types.h
        #types = open(os.path.join(mydir, "cdefs", "vx_types.h")).read()
        types = get_and_cleanup_header_file(os.path.join(incdir, "VX", "vx_types.h"))

        for k,v in defs.items():
            types = types.replace(k, v)

        #types = re.subn(r'(#define\s+[^\s]+)\s*.*', r'\1 ...', types)[0] # Remove specifics from #defines
        types = re.subn(r'(/\*.*?\*/)', r'', types)[0] # Remove some one line comments
        types = re.subn(r'=.*,', r'= ...,', types)[0] # Remove specifics from enums
        types = re.subn(r'\[\s*[^\s]+?.*?\]', r'[...]', types)[0] # Remove specific array sizes
        types = re.subn(r'(#\s*if\s+.*)', r'//\1', types)[0] # #if ...
        types = re.subn(r'(#\s*else.*)', r'//\1', types)[0] # #else
        types = re.subn(r'(#\s*endif.*)', r'//\1', types)[0] # #endif

        ffi.cdef(types)
        ffi.cdef('''
            char *_get_FMT_REF(void);
            char *_get_FMT_SIZE(void);
            int _get_KERNEL_BASE(int vendor, int lib);
            char *_get_backend_version();
            char *_get_backend_name();
            char *_get_backend_install_path();
        ''')

        # vx_kernels.h
        #kernels = open(os.path.join(mydir, "cdefs", "vx_kernels.h")).read()
        kernels = open(os.path.join(incdir, "VX", "vx_kernels.h")).read()
        kernels = re.subn(r'=.*,', r'= ...,', kernels)[0] # Remove specifics from enums
        ffi.cdef(kernels)

        # vx_api.h
        #api = open(os.path.join(mydir, "cdefs", "vx_api.h")).read()
        api = open(os.path.join(incdir, "VX", "vx_api.h")).read()
        for k, v in defs.items():
            api = api.replace(k, v)
        ffi.cdef(api)

        # vx_nodes.h
        #nodes = open(os.path.join(mydir, "cdefs", "vx_nodes.h")).read()
        nodes = open(os.path.join(incdir, "VX", "vx_nodes.h")).read()
        for k, v in defs.items():
            nodes = nodes.replace(k, v)
        ffi.cdef(nodes)

        # vxu.h
        #vxu = open(os.path.join(mydir, "cdefs", "vxu.h")).read()
        vxu = open(os.path.join(incdir, "VX", "vxu.h")).read()
        for k, v in defs.items():
            vxu = vxu.replace(k, v)
        ffi.cdef(vxu)

        ffi.set_source("pyvx.backend.%s" % name, """
            #include <VX/vx.h>
            #include <VX/vxu.h>
            char *_get_FMT_REF(void) {return VX_FMT_REF;}
            char *_get_FMT_SIZE(void) {return VX_FMT_SIZE;}
            int _get_KERNEL_BASE(int vendor, int lib) {return VX_KERNEL_BASE(vendor, lib);}
            char *_get_backend_version() {return "%s";}
            char *_get_backend_name() {return "%s";}
            char *_get_backend_install_path() {return "%s";}
                       """ % (__backend_version__.decode("utf8"), name, openvx_install),
                       include_dirs=[os.path.join(openvx_install, 'include')],
                       library_dirs=[libdir],
                       extra_link_args=['-Wl,-rpath=' + os.path.abspath(os.path.join(openvx_install, 'bin'))],
                       libraries=libs) # ['openvx', 'vxu'])
        ffi.compile()        
        exit(-1)

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


def get_and_cleanup_header_file(filename):
    code = open(filename).read()
    code = re.subn(r'(#\s*ifndef\s+[^\s]+)', r'//\1', code)[0] # Remove directives
    code = re.subn(r'(#\s*include\s+<[^\>]+>)', r'//\1', code)[0] # Remove directives
    code = re.subn(r'(#\s*endif.*)', r'//\1', code)[0] # Remove directives
    # TODO: remove parameterized macros
    code = re.subn(r'(#\s*define\s+[^\s]+)\s.*', r'\1 ...', code)[0] # Remove specifics from #defines
    code = re.subn(r'(#\s*define\s+[^\s]+\s*\([^\)]*\)\s.*)', r'//\1', code)[0] # Remove parameterized macros
    code = re.subn(r'#\s*(define\s+.*)', r'#\1', code)[0] # remove whitespace between '#' and directive
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
