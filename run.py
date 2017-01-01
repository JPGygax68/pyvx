# Intended for debugging purposes

import sys
import pyvx.build_cbackend

if __name__ == '__main__':

    cmd, *args = sys.argv[1:]

    if cmd == 'build_cbackend':
        default = '--default' in args
        if default:
            args.remove('--default')
        if len(args) == 2:
            name, openvx_install = args
            pyvx.build_cbackend.build(name, openvx_install, default)
        else:
            print("Usage: %s %s [--default] <name> <openvx install path>" % (sys.argv[0], cmd))
    else:
        print("Unsupported command: \"%s\"" % cmd)
