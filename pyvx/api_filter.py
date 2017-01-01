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

            def type_name(t: Type) -> str:
                return t.spelling

            def var_decl_to_str(c: Cursor) -> str:
                t = c.type # type: Type
                if t.kind == TypeKind.INCOMPLETEARRAY:
                    return '%s %s[]' % (t.element_type.spelling, c.displayname)
                elif t.kind == TypeKind.CONSTANTARRAY:
                    t = c.type # type: Type
                    return '%s %s[%d]' % (t.element_type.spelling, c.displayname, t.element_count)
                else:
                    return '%s %s' % (type_name(c.type), c.displayname)

            def struct_or_union_members_to_text(basetype_name: str, node: Cursor):
                mdefs = [var_decl_to_str(c) for c in node.get_children()]
                return '%s %s {\n    ' % (basetype_name, node.spelling) + ';\n    '.join(mdefs) + ';\n}'

            if cursor.kind == CursorKind.ENUM_DECL:
                defs = ["%s = %s" % (c.displayname, c.enum_value) for c in cursor.get_children()]
                return 'enum %s { %s };' % (cursor.displayname, ', '.join(defs))
            elif cursor.kind == CursorKind.TYPEDEF_DECL:
                c = [_ for _ in cursor.get_children()] # children
                utdt = cursor.underlying_typedef_type # type: Type
                fc = c and c[0] # type:Cursor; first child
                if fc:
                    if fc.kind == CursorKind.STRUCT_DECL:
                        return 'typedef %s %s;' % (struct_or_union_members_to_text('struct', fc), cursor.spelling)
                    elif fc.kind == CursorKind.UNION_DECL:
                        return 'typedef %s %s;' % (struct_or_union_members_to_text('union', fc), cursor.spelling)
                    elif fc.kind in [CursorKind.TYPE_REF, CursorKind.PARM_DECL]:
                        if utdt.kind == TypeKind.POINTER:
                            pe = utdt.get_pointee() # type: Type
                            # Is this a function ?
                            ca = pe.get_canonical() # type: Type
                            rt = pe.get_result() # type: Type
                            if ca.kind == TypeKind.FUNCTIONPROTO:
                                args = ['%s' % var_decl_to_str(_) for _ in c[1:]]
                                return 'typedef %s (*%s)(%s);' % (rt.spelling, cursor.spelling, ', '.join(args))
                    elif fc.kind == CursorKind.ENUM_DECL:
                        return 'typedef %s %s;' % (utdt.spelling, cursor.spelling)
                    else:
                        raise NotImplementedError("unsupported typedef variant")
                return 'typedef %s %s;' % (utdt.spelling, cursor.spelling)

            # TODO (the following is a placeholder)
            return "/* %s: %s */" % (cursor.spelling, cursor.kind)

        return '\n'.join([node_to_string(c) for c in self.tu.cursor.get_children()
                          if c.spelling[:2].lower() == "vx"])

    def dbg_print_all(self):

        def print_node(n: Cursor, indent):
            print('  ' * indent + 'spelling: %s, kind: %s, type: %s' %
                  (n.spelling, n.kind, type(n)))
            for c in n.get_children():
                print_node(c, indent + 1)

        print_node(self.tu.cursor, 0)