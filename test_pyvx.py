from pyvx import *
from array import array

class TestPyVx(object):
    def test_gaussian(self):
        g = Graph()
        img = Image(3, 4, vx.FOURCC_U8, array('B', range(12)))
        with g:
            gimg = Gaussian3x3(img)
            gimg.force()
        g.verify()
        g.process()
        assert gimg.data[4] == 4
        assert gimg.data[7] == 7

    def test_replicate_border(self):
        g = Graph()
        img = Image(3, 4, vx.FOURCC_U8, array('B', range(12)))
        with g:
            gimg = Gaussian3x3(img)
            gimg.producer.border_mode = vx.BORDER_MODE_REPLICATE
            gimg.force()
        g.verify()
        g.process()
        assert gimg.data[0] == 1
        assert gimg.data[1] == 1
        assert gimg.data[11] == 10

    def test_add(self):
        g = Graph()
        img = Image(3, 4, vx.FOURCC_U8, array('B', range(12)))
        with g:
            sa = img + img
            sa.force()
        g.verify()
        g.process()
        for i in range(12):
            assert sa.data[i] == 2*i
