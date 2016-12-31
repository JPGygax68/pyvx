from clang.cindex import *

class APIFilter:

    def __init__(self, header_files = [], include_dirs = [], ppdefs = {}):

        self.include_dirs = include_dirs
        self.ppdefs = ppdefs

        self.index = Index.create()

        for filename in header_files:
            self.read_header(filename)

    def read_header(self, filename):
        args = ["-I"+incdir for incdir in self.include_dirs]
        args += ["-D%s=%s" % (k,v) for k, v in self.ppdefs.items()]
        self.tu = self.index.parse(filename, args=args)
