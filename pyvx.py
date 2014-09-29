import vx

context = vx.Context()
context.current_graph = None


class Graph(vx.Graph):

    def __init__(self):
        vx.Graph.__init__(self, context)

    def __enter__(self):
        assert context.current_graph is None
        context.current_graph = self

    def __exit__(self, *args):
        assert context.current_graph is self
        context.current_graph = None


class Image(vx.Image):

    def __init__(self, *args, **kwargs):
        vx.Image.__init__(self, context, *args, **kwargs)

    @property
    def channel_y(self):
        return ChannelExtract(self, vx.CHANNEL_Y)


def VirtualImage(w=0, h=0, color=vx.FOURCC_VIRT):
    return Image(w, h, color, None, True, context.current_graph)


def ChannelExtract(input, channel):
    output = VirtualImage()
    vx.ChannelExtractNode(context.current_graph,
                          input, channel, output)
    return output


def Gaussian3x3(input):
    output = VirtualImage()
    vx.Gaussian3x3Node(context.current_graph, input, output)
    return output


def Sobel3x3(input):
    dx, dy = VirtualImage(), VirtualImage()
    vx.Sobel3x3Node(context.current_graph, input, dx, dy)
    return dx, dy


def Magnitude(grad_x, grad_y):
    mag = VirtualImage()
    vx.MagnitudeNode(context.current_graph, grad_x, grad_y, mag)
    return mag


def Phase(grad_x, grad_y):
    ph = VirtualImage()
    vx.PhaseNode(context.current_graph, grad_x, grad_y, ph)
    return ph


def AccumulateImage(input):
    accum = VirtualImage()
    vx.VirtualImageNode(context.current_graph, input, accum)
    return accum

if __name__ == '__main__':
    from imgpy.io import Mplayer, view
    video = Mplayer("/usr/share/cognimatics/data/facit/events/passanger/bustst1-M3014-180.mjpg", True)
    frame = video.next()
    w, h = frame.width, frame.height
    res = frame.new()    

    g = Graph()
    with g:
        img = Image(w, h, vx.FOURCC_U8, data=frame)
        gimg = Gaussian3x3(img)
        gimg.producer.border_mode = vx.BORDER_MODE_REPLICATE
        gimg.force(res)
        # dx, dy = Sobel3x3(gimg)
        # mag = Magnitude(dx, dy)
        # phi = Phase(dx, dy)
    g.verify()

    for new_frame in video:
        frame.data[:] = new_frame.data
        g.process()
        view(res)
