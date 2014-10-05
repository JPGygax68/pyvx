from codegen import PythonApi, export, Enum, Reference
from pyvx import *


class OpenVxApi(PythonApi):
    
    vx_context = Reference()
    vx_image = Reference()

    vx_fourcc = Enum(FOURCC_VIRT, FOURCC_RGB, FOURCC_RGBX, FOURCC_UYVY,
                     FOURCC_YUYV, FOURCC_U8, FOURCC_S8, FOURCC_U16, 
                     FOURCC_S16, FOURCC_U32, FOURCC_S32)

    @export("vx_context()")
    def vxCreateContext(self):
        return Context()

    @export("vx_image(vx_context, uint32_t, uint32_t, vx_fourcc)")
    def vxCreateImage(self, context, width, height, color):
        img = Image(width, height, color, context=context)
        # FIXME: context.free_on_del.add(img)
        return img

if __name__ == '__main__':
    import sys
    api = OpenVxApi(True)
    api.build(sys.argv[1])