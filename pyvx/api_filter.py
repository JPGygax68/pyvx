from clang.cindex import *

class APIFilter:

    def __init__(self, header_files = [], include_dirs = [], ppdefs = {}):

        self.include_dirs = include_dirs
        self.ppdefs = ppdefs

        self.index = Index.create()

        self.tu = None # type: Cursor

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

        def reassemble(cursor: Cursor):
            #return ' '.join(filtered_tokens(c))
            return ' '.join(c.spelling for c in cursor.get_children())

        def node_to_string(cursor: Cursor) -> str:
            if cursor.kind == CursorKind.ENUM_DECL:
                defs = ["%s = %s" % (c.displayname, c.enum_value) for c in cursor.get_children()]
                return 'enum %s { %s };' % (cursor.displayname, ', '.join(defs))
            elif cursor.kind == CursorKind.TYPEDEF_DECL:
                children = [_ for _ in cursor.get_children()]
                if children and children[0].kind == CursorKind.STRUCT_DECL:
                    mdefs = ['%s %s;' % (c.type.spelling, c.displayname) for c in children[0].get_children()]
                    td = '%s {\n    ' % children[0].spelling + '\n    '.join(mdefs) + '\n}'
                else:
                    td = cursor.underlying_typedef_type.spelling
                return 'typedef %s %s;' % (td, cursor.displayname)
            else:
                # TODO (the following is a placeholder)
                return "/* %s: %s */" % (cursor.spelling, cursor.kind)

        return '\n'.join([node_to_string(c) for c in self.tu.cursor.get_children()
                          if c.spelling[:2].lower() == "vx"])

    def dbg_print_all(self):

        def print_node(n: Cursor, indent):
            print('  ' * indent + 'displayname: %s, kind: %s, type: %s' %
                  (n.displayname, n.kind, n.result_type.spelling))
            for c in n.get_children():
                print_node(c, indent + 1)

        print_node(self.tu.cursor, 0)