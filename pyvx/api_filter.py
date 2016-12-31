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

    def apply(self):

        def filtered_tokens(c: Cursor) -> list:
            return [
                self.ppdefs[t.spelling] if t.spelling in self.ppdefs else t.spelling
                for t in c.get_tokens() if t.kind != TokenKind.COMMENT]

        def reassemble(c: Cursor):
            return ' '.join(filtered_tokens(c))

        return '\n'.join([reassemble(c) for c in self.tu.cursor.get_children()
                          if c.spelling[:2].lower() == "vx"])

    def dbg_print_all(self):
        for c in self.tu.cursor.get_children():
            if c.spelling[:2].lower() == 'vx':
                s = ' '.join([t.spelling for t in c.get_tokens() if t.kind != TokenKind.COMMENT])
                print(s)