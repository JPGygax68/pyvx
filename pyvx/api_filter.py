import re
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
        args += ["-D%s%s%s" % (k, '=' if len(v) > 0 else '', v) for k, v in self.ppdefs.items() if v != '']
        self.tu = self.index.parse(filename, args=args, options=TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD)
        #self.tu = self.index.parse(filename, args=args)

    def apply(self):

        def filtered_tokens(c: Cursor) -> list:
            return [
                self.ppdefs[t.spelling] if t.spelling in self.ppdefs else t.spelling
                for t in c.get_tokens() if t.kind != TokenKind.COMMENT]

        def reassemble(cursor: Cursor):
            #return ' '.join(filtered_tokens(c))
            return ' '.join(c.spelling for c in cursor.get_children())

        def node_to_string(cursor: Cursor) -> str:
            """Converts an AST node back to a C declaration.
            CAUTION! This code was evolved by trial and error, and just barely covers the needs of PyVX. It cannot
            reliably be used in any other context."""

            ARRAY_KINDS = [TypeKind.CONSTANTARRAY, TypeKind.INCOMPLETEARRAY, TypeKind.VARIABLEARRAY,
                           TypeKind.DEPENDENTSIZEDARRAY]

            def is_func_ptr_tdef(t: Type) -> bool:
                """"Pass the underlying_typedef_type of a Cursor here."""
                #u = node.underlying_typedef_type
                ca = t.get_canonical() # type: Type
                return ca.kind == TypeKind.POINTER and ca.get_pointee().get_canonical().kind == TypeKind.FUNCTIONPROTO

            def type_name(t: Type) -> str:
                if True:
                    # DO NOT CANONICALIZE
                    if t.kind in ARRAY_KINDS:
                        return t.element_type.spelling
                    return t.spelling
                else:
                    if is_func_ptr_tdef(t):
                        return t.spelling
                    else:
                        ca = t.get_canonical() # type: Type
                        if ca.kind in ARRAY_KINDS:
                            return ca.element_type.spelling
                        else:
                            return ca.spelling

            def var_decl_to_str(c: Cursor) -> str:
                t = c.type # type: Type
                t = t.get_canonical() #
                if t.kind == TypeKind.INCOMPLETEARRAY:
                    return '%s %s[]' % (type_name(c.type), c.displayname)
                elif t.kind == TypeKind.CONSTANTARRAY:
                    t = c.type # type: Type
                    return '%s %s[%d]' % (type_name(t), c.displayname, t.element_count)
                # TODO: other array types (see ARRAY_KINDS definition)
                else:
                    return '%s %s' % (type_name(c.type), c.displayname)

            def struct_or_union_members_to_text(basetype_name: str, node: Cursor):
                mdefs = [var_decl_to_str(c) for c in node.get_children()]
                return '%s %s {\n    ' % (basetype_name, node.spelling) + ';\n    '.join(mdefs) + ';\n}'

            if cursor.kind == CursorKind.ENUM_DECL:
                defs = ["%s = %s" % (c.displayname, c.enum_value) for c in cursor.get_children()]
                return 'enum %s { %s };' % (cursor.displayname, ', '.join(defs))
            elif cursor.kind == CursorKind.TYPEDEF_DECL:
                ch = [_ for _ in cursor.get_children()] # children
                utdt = cursor.underlying_typedef_type # type: Type
                if utdt.kind == TypeKind.POINTER:
                    pe = utdt.get_pointee()  # type: Type
                    ca = pe.get_canonical()  # type: Type
                    if ca.kind == TypeKind.FUNCTIONPROTO:
                        rt = pe.get_result()  # type: Type
                        args = ['%s' % var_decl_to_str(_) for _ in ch[1:]] # 1 if ch[0].kind == CursorKind.TYPE_REF else 0:]]
                        if ca.is_function_variadic(): args += ['...']
                        at = ' '.join(['__'+_ for _ in re.findall(r'__attribute__\(\(([^,\)]+)\)\)', utdt.spelling)])
                        return 'typedef %s (%s *%s)(%s);' % (type_name(rt), at, cursor.spelling, ', '.join(args))
                fc = ch and ch[0] # type:Cursor; first child
                if fc:
                    if fc.kind == CursorKind.STRUCT_DECL:
                        return 'typedef %s %s;' % (struct_or_union_members_to_text('struct', fc), cursor.spelling)
                    elif fc.kind == CursorKind.UNION_DECL:
                        return 'typedef %s %s;' % (struct_or_union_members_to_text('union', fc), cursor.spelling)
                    #elif fc.kind in [CursorKind.TYPE_REF, CursorKind.PARM_DECL]:
                    elif fc.kind == CursorKind.ENUM_DECL:
                        return 'typedef %s %s;' % (utdt.spelling, cursor.spelling)
                return 'typedef %s %s;' % (utdt.spelling, cursor.spelling)
            elif cursor.kind == CursorKind.FUNCTION_DECL:
                rt = cursor.type.get_result()  # type: Type
                ca = cursor.type.get_canonical() # type: Type
                #ch = [_ for _ in cursor.get_children()]
                #args = ['%s' % var_decl_to_str(_) for _ in ch[1 if ch[0].kind == CursorKind.TYPE_REF else 0:]]
                args = ['%s' % var_decl_to_str(_) for _ in cursor.get_children() if _.kind == CursorKind.PARM_DECL]
                ch = [_ for _ in cursor.get_children()]
                tk = [_ for _ in ch[1].get_tokens()]
                #cc = self.ppdefs.get(tk[1].cursor.spelling, tk[1].cursor.spelling) \
                #    if tk[1].cursor.kind == CursorKind.MACRO_INSTANTIATION else tk[1].cursor.spelling
                cc = self.ppdefs[tk[1].cursor.spelling] \
                    if tk[1].cursor.kind == CursorKind.MACRO_INSTANTIATION else ''
                if ca.kind == TypeKind.FUNCTIONPROTO and ca.is_function_variadic(): args += ['...']
                return '%s %s %s(%s);' % (rt.spelling, cc, cursor.spelling, ', '.join(args))
            elif cursor.kind == CursorKind.MACRO_DEFINITION:
                #return '#define %s %s' % (cursor.spelling, ''.join([_.spelling for _ in cursor.get_tokens()][:1]))
                #return '#define %s ...' % cursor.spelling
                v = ''.join([_.spelling for _ in cursor.get_tokens()][1:-1])
                self.ppdefs[cursor.spelling] = v
                return None
            elif cursor.kind == CursorKind.MACRO_INSTANTIATION:
                return None
            else:
                return "/* NOT IMPLEMENTED YET: %s: %s */" % (cursor.spelling, cursor.kind)
                pass

            # TODO (the following is a placeholder)
            return "/* %s: %s */" % (cursor.spelling, cursor.kind)

        return '\n'.join(_ for _ in [node_to_string(c) for c in self.tu.cursor.get_children()
                          if c.spelling[:2].lower() == "vx"] if not _ is None)

    def dbg_print_all(self):

        def print_node(n: Cursor, indent):
            print('  ' * indent + 'spelling: %s, kind: %s, type: %s' %
                  (n.spelling, n.kind, type(n)))
            for c in n.get_children():
                print_node(c, indent + 1)

        print_node(self.tu.cursor, 0)