from array import array
import sys

from py.test import raises

from pyvx import vx
import pyvx

if sys.version_info > (3,):
    unicode = str

class TestVX(object):
    def test_context(self):
        c = vx.CreateContext()
        assert vx.GetStatus(vx.reference(c)) == vx.SUCCESS
        assert vx.QueryReference(vx.reference(c), vx.REF_ATTRIBUTE_TYPE, 'vx_enum') == (vx.SUCCESS, vx.TYPE_CONTEXT)
        s, v = vx.QueryContext(c, vx.CONTEXT_VENDOR_ID, 'vx_uint16')
        assert s == vx.SUCCESS
        assert isinstance(v, int)
        s, v = vx.QueryContext(c, vx.CONTEXT_IMPLEMENTATION, 'vx_char[VX_MAX_IMPLEMENTATION_NAME]', str)
        assert s == vx.SUCCESS
        assert isinstance(v, unicode)

        s = vx.SetContextAttribute(c, vx.CONTEXT_IMMEDIATE_BORDER_MODE,
                                      vx.border_mode_t(vx.BORDER_MODE_CONSTANT, 42))
        assert s == vx.SUCCESS
        s, v = vx.QueryContext(c, vx.CONTEXT_IMMEDIATE_BORDER_MODE, 'vx_border_mode_t')
        assert s == vx.SUCCESS
        assert v.mode == vx.BORDER_MODE_CONSTANT
        assert v.constant_value == 42

        vx.Hint(vx.reference(c), vx.HINT_SERIALIZE)
        vx.Directive(vx.reference(c), vx.DIRECTIVE_DISABLE_LOGGING)
        assert vx.GetContext(vx.reference(c)) == c
        vx.RegisterUserStruct(c, 42)

        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_image(self):
        c = vx.CreateContext()
        img = vx.CreateImage(c, 640, 480, vx.DF_IMAGE_RGB)
        assert vx.GetStatus(vx.reference(img)) == vx.SUCCESS
        assert vx.QueryReference(vx.reference(img), vx.REF_ATTRIBUTE_TYPE, 'vx_enum') == (vx.SUCCESS, vx.TYPE_IMAGE)

        roi = vx.CreateImageFromROI(img, vx.rectangle_t(10, 10, 100, 100))
        assert vx.GetStatus(vx.reference(roi)) == vx.SUCCESS
        assert vx.ReleaseImage(roi) == vx.SUCCESS
        roi = None

        const = vx.CreateUniformImage(c, 640, 480, vx.DF_IMAGE_S16, 7, 'vx_int16')
        assert vx.GetStatus(vx.reference(const)) == vx.SUCCESS

        const = vx.CreateUniformImage(c, 640, 480, vx.DF_IMAGE_RGB, (7, 8, 9), 'vx_uint8[]')
        assert vx.GetStatus(vx.reference(const)) == vx.SUCCESS

        addr = vx.imagepatch_addressing_t(640, 480, 1, 640, vx.SCALE_UNITY, vx.SCALE_UNITY, 1, 1)
        data = array('B', [0x42]) * (640 * 480)
        hand = vx.CreateImageFromHandle(c, vx.DF_IMAGE_U8, (addr,), (data,), vx.IMPORT_TYPE_HOST)
        assert vx.GetStatus(vx.reference(hand)) == vx.SUCCESS
        hand = vx.CreateImageFromHandle(c, vx.DF_IMAGE_U8, addr, data, vx.IMPORT_TYPE_HOST)
        assert vx.GetStatus(vx.reference(hand)) == vx.SUCCESS
        hand = vx.CreateImageFromHandle(c, vx.DF_IMAGE_RGB, (addr, addr, addr), (data, data, data), vx.IMPORT_TYPE_HOST)
        assert vx.GetStatus(vx.reference(hand)) == vx.SUCCESS

        assert vx.QueryImage(img, vx.IMAGE_ATTRIBUTE_WIDTH, 'vx_uint32') == (vx.SUCCESS, 640)
        assert vx.SetImageAttribute(img, vx.IMAGE_ATTRIBUTE_SPACE, vx.COLOR_SPACE_BT601_525, 'vx_enum') == vx.SUCCESS
        assert vx.QueryImage(img, vx.IMAGE_ATTRIBUTE_SPACE, 'vx_enum') == (vx.SUCCESS, vx.COLOR_SPACE_BT601_525)

        assert vx.GetContext(vx.reference(img)) == c

        r = vx.rectangle_t(10, 20, 30, 40)
        s = vx.ComputeImagePatchSize(img, r, 0)
        status, addr, ptr = vx.AccessImagePatch(img, r, 0, None, None, vx.READ_AND_WRITE)
        assert status == vx.SUCCESS
        assert addr.dim_x == addr.dim_y == 20
        ptr[0] = b'H'
        assert vx.CommitImagePatch(img, r, 0, addr, ptr) == vx.SUCCESS
        status, addr, ptr = vx.AccessImagePatch(img, r, 0, None, None, vx.READ_AND_WRITE)
        assert status == vx.SUCCESS
        assert ptr[0] == b'H'
        pixel = vx.FormatImagePatchAddress1d(ptr, 0, addr)
        assert pixel[0] == b'H'
        assert vx.CommitImagePatch(img, r, 0, addr, ptr) == vx.SUCCESS

        assert 7 not in data
        addr = vx.imagepatch_addressing_t(20, 20, 1, 20, vx.SCALE_UNITY, vx.SCALE_UNITY, 1, 1)
        rdata = array('B', [0]) * (20 * 20)
        status, addr, ptr = vx.AccessImagePatch(hand, r, 0, addr, rdata, vx.READ_AND_WRITE)
        assert rdata[1] == 0x42
        rdata[1] = 7
        pixel = vx.FormatImagePatchAddress1d(ptr, 1, addr)
        assert pixel[0] == b'\x07'
        pixel = vx.FormatImagePatchAddress2d(ptr, 0, 0, addr)
        assert pixel[0] == b'\x42'
        assert vx.CommitImagePatch(hand, r, 0, addr, ptr) == vx.SUCCESS
        assert data[11 + 20*640] == 7

        status, r = vx.GetValidRegionImage(const)
        assert status == vx.SUCCESS
        assert r.end_x == 640
        assert r.end_y == 480

        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_kernel(self):
        c = vx.CreateContext()
        kernel = vx.GetKernelByName(c, b"org.khronos.openvx.sobel_3x3")
        assert vx.GetStatus(vx.reference(kernel)) == vx.SUCCESS
        assert vx.QueryReference(vx.reference(kernel), vx.REF_ATTRIBUTE_TYPE, 'vx_enum') == (vx.SUCCESS, vx.TYPE_KERNEL)
        k = vx.GetKernelByEnum(c, vx.KERNEL_SOBEL_3x3)
        assert kernel == k
        s, i = vx.QueryKernel(kernel, vx.KERNEL_ATTRIBUTE_ENUM, 'vx_enum')
        assert i == vx.KERNEL_SOBEL_3x3
        vx.ReleaseKernel(k)
        param = vx.GetKernelParameterByIndex(kernel, 0)
        assert vx.GetStatus(vx.reference(param)) == vx.SUCCESS

        assert vx.LoadKernels(c, "openvx-extras") == vx.SUCCESS
        k = vx.GetKernelByName(c, b"org.khronos.extra.edge_trace")
        assert vx.GetStatus(vx.reference(k)) == vx.SUCCESS

        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_graph(self):
        c = vx.CreateContext()
        g = vx.CreateGraph(c)
        assert vx.GetStatus(vx.reference(g)) == vx.SUCCESS
        assert vx.QueryReference(vx.reference(g), vx.REF_ATTRIBUTE_TYPE, 'vx_enum') == (vx.SUCCESS, vx.TYPE_GRAPH)
        assert vx.IsGraphVerified(g) == vx.false_e
        assert vx.QueryGraph(g, vx.GRAPH_ATTRIBUTE_NUMNODES, 'vx_uint32') == (vx.SUCCESS, 0)

        img = vx.CreateImage(c, 640, 480, vx.DF_IMAGE_U8)
        dx = vx.CreateImage(c, 640, 480, vx.DF_IMAGE_S16)
        dy = vx.CreateImage(c, 640, 480, vx.DF_IMAGE_S16)
        node = vx.Sobel3x3Node(g, img, dx, dy)
        assert vx.VerifyGraph(g) == vx.SUCCESS
        assert vx.ProcessGraph(g) == vx.SUCCESS
        assert vx.ScheduleGraph(g) == vx.SUCCESS
        assert vx.WaitGraph(g) == vx.SUCCESS

        p = vx.GetParameterByIndex(node, 0)
        assert vx.AddParameterToGraph(g, p) == vx.SUCCESS
        p2 = vx.GetGraphParameterByIndex(g, 0)
        assert vx.SetGraphParameterByIndex(g, 0, vx.reference(dx)) == vx.SUCCESS
        assert vx.VerifyGraph(g) != vx.SUCCESS
        assert vx.SetGraphParameterByIndex(g, 0, vx.reference(img)) == vx.SUCCESS
        assert vx.VerifyGraph(g) == vx.SUCCESS
        assert vx.IsGraphVerified(g) == vx.true_e

        def callback(node):
            callback.called = True
            return vx.SUCCESS

        assert vx.AssignNodeCallback(node, callback) == vx.SUCCESS
        assert vx.ProcessGraph(g) == vx.SUCCESS
        assert callback.called

        def callback(node):
            raise TypeError('Escaping from callback')
            return vx.SUCCESS

        assert vx.AssignNodeCallback(node, callback) != vx.SUCCESS
        assert vx.AssignNodeCallback(node, None) == vx.SUCCESS
        assert vx.AssignNodeCallback(node, callback) == vx.SUCCESS
        assert vx.VerifyGraph(g) == vx.SUCCESS
        assert vx.ProcessGraph(g) != vx.SUCCESS

        img = vx.CreateVirtualImage(g, 640, 480, vx.DF_IMAGE_RGB)
        assert vx.GetStatus(vx.reference(img)) == vx.SUCCESS

        assert vx.ReleaseGraph(g) == vx.SUCCESS
        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_node(self):
        c = vx.CreateContext()
        g = vx.CreateGraph(c)

        k = vx.GetKernelByEnum(c, vx.KERNEL_SOBEL_3x3)
        assert vx.GetStatus(vx.reference(k)) == vx.SUCCESS
        node = vx.CreateGenericNode(g, k)
        assert vx.GetStatus(vx.reference(node)) == vx.SUCCESS
        assert vx.QueryReference(vx.reference(node), vx.REF_ATTRIBUTE_TYPE, 'vx_enum') == (vx.SUCCESS, vx.TYPE_NODE)
        s = vx.SetNodeAttribute(node, vx.NODE_ATTRIBUTE_BORDER_MODE,
                                vx.border_mode_t(vx.BORDER_MODE_CONSTANT, 42))
        assert s == vx.SUCCESS
        s, v = vx.QueryNode(node, vx.NODE_ATTRIBUTE_BORDER_MODE, 'vx_border_mode_t')
        assert v.mode == vx.BORDER_MODE_CONSTANT
        assert v.constant_value == 42

        assert vx.ReleaseNode(node) == vx.SUCCESS

        node = vx.CreateGenericNode(g, k)
        assert vx.RemoveNode(node) == vx.SUCCESS

        assert vx.ReleaseGraph(g) == vx.SUCCESS
        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_parameter(self):
        c = vx.CreateContext()
        g = vx.CreateGraph(c)
        img = vx.CreateImage(c, 640, 480, vx.DF_IMAGE_U8)
        dx = vx.CreateImage(c, 640, 480, vx.DF_IMAGE_S16)
        dy = vx.CreateImage(c, 640, 480, vx.DF_IMAGE_S16)
        node = vx.Sobel3x3Node(g, img, dx, dy)

        param = vx.GetParameterByIndex(node, 0)
        assert vx.GetStatus(vx.reference(param)) == vx.SUCCESS
        assert vx.QueryReference(vx.reference(param), vx.REF_ATTRIBUTE_TYPE, 'vx_enum') == (vx.SUCCESS, vx.TYPE_PARAMETER)
        s, v = vx.QueryParameter(param, vx.PARAMETER_ATTRIBUTE_REF, "vx_reference")
        assert s == vx.SUCCESS
        assert v == img

        assert vx.SetParameterByIndex(node, 0, vx.reference(dx)) == vx.SUCCESS
        s, v = vx.QueryParameter(param, vx.PARAMETER_ATTRIBUTE_REF, "vx_reference")
        assert s == vx.SUCCESS
        assert v == dx

        assert vx.SetParameterByReference(param, vx.reference(dy)) == vx.SUCCESS
        s, v = vx.QueryParameter(param, vx.PARAMETER_ATTRIBUTE_REF, "vx_reference")
        assert s == vx.SUCCESS
        assert v == dy

        assert vx.ReleaseParameter(param) == vx.SUCCESS
        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_scalar(self):
        c = vx.CreateContext()
        scalar = vx.CreateScalar(c, vx.TYPE_INT16, 7)
        assert vx.GetStatus(vx.reference(scalar)) == vx.SUCCESS
        assert vx.QueryReference(vx.reference(scalar), vx.REF_ATTRIBUTE_TYPE, 'vx_enum') == (vx.SUCCESS, vx.TYPE_SCALAR)
        assert vx.QueryScalar(scalar, vx.SCALAR_ATTRIBUTE_TYPE, "vx_enum") == (vx.SUCCESS, vx.TYPE_INT16)
        assert vx.ReadScalarValue(scalar) == (vx.SUCCESS, 7)
        assert vx.WriteScalarValue(scalar, 42) == vx.SUCCESS
        assert vx.ReadScalarValue(scalar) == (vx.SUCCESS, 42)
        assert vx.ReleaseScalar(scalar) == vx.SUCCESS
        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_reference(self):
        with raises(TypeError):
            vx.reference(vx.imagepatch_addressing_t())

    def test_delay(self):
        c = vx.CreateContext()
        img = vx.CreateImage(c, 640, 480, vx.DF_IMAGE_RGB)
        delay = vx.CreateDelay(c, vx.reference(img), 3)
        assert vx.GetStatus(vx.reference(delay)) == vx.SUCCESS
        assert vx.QueryReference(vx.reference(delay), vx.REF_ATTRIBUTE_TYPE, 'vx_enum') == (vx.SUCCESS, vx.TYPE_DELAY)
        assert vx.QueryDelay(delay, vx.DELAY_ATTRIBUTE_SLOTS, 'vx_size') == (vx.SUCCESS, 3)
        ref0 = vx.GetReferenceFromDelay(delay, 0)
        ref1 = vx.GetReferenceFromDelay(delay, 1)
        ref2 = vx.GetReferenceFromDelay(delay, 2)
        g = vx.CreateGraph(c)
        node = vx.Sobel3x3Node(g, vx.from_reference(ref0), vx.from_reference(ref1), vx.from_reference(ref2))

        param = vx.GetParameterByIndex(node, 1)
        s, v = vx.QueryParameter(param, vx.PARAMETER_ATTRIBUTE_REF, "vx_reference")
        assert s == vx.SUCCESS
        assert v == ref1
        assert vx.AgeDelay(delay) == vx.SUCCESS
        s, v = vx.QueryParameter(param, vx.PARAMETER_ATTRIBUTE_REF, "vx_reference")
        assert s == vx.SUCCESS
        assert v == ref0

        assert vx.ReleaseDelay(delay) == vx.SUCCESS
        assert vx.ReleaseContext(c) == vx.SUCCESS


    def test_log(self):
        c = vx.CreateContext()
        def callback(context, ref, status, string):
            assert status == vx.FAILURE
            assert string == b"Test"
            callback.called = True
        vx.RegisterLogCallback(c, callback, vx.false_e)
        vx.AddLogEntry(vx.reference(c), vx.FAILURE, b"Test")
        assert callback.called
        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_lut(self):
        c = vx.CreateContext()
        lut = vx.CreateLUT(c, vx.TYPE_UINT8, 256)
        assert vx.GetStatus(vx.reference(lut)) == vx.SUCCESS
        assert vx.QueryReference(vx.reference(lut), vx.REF_ATTRIBUTE_TYPE, 'vx_enum') == (vx.SUCCESS, vx.TYPE_LUT)
        assert vx.QueryLUT(lut, vx.LUT_ATTRIBUTE_COUNT, 'vx_size') == (vx.SUCCESS, 256)

        s, data = vx.AccessLUT(lut, None, vx.READ_AND_WRITE)
        assert s == vx.SUCCESS
        data[1] = b'H'
        assert vx.CommitLUT(lut, data) == vx.SUCCESS
        s, data = vx.AccessLUT(lut, None, vx.READ_ONLY)
        assert data[1] == b'H'
        assert vx.CommitLUT(lut, data) == vx.SUCCESS

        data = array('B', [0]) * 256
        vx.AccessLUT(lut, data, vx.READ_ONLY)
        assert data[1] == ord('H')
        assert vx.CommitLUT(lut, data) == vx.SUCCESS

        assert vx.ReleaseLUT(lut) == vx.SUCCESS
        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_distribution(self):
        c = vx.CreateContext()
        distribution = vx.CreateDistribution(c, 8, 0, 16)
        assert vx.GetStatus(vx.reference(distribution)) == vx.SUCCESS
        assert vx.QueryReference(vx.reference(distribution), vx.REF_ATTRIBUTE_TYPE, 'vx_enum') == (vx.SUCCESS, vx.TYPE_DISTRIBUTION)
        assert vx.QueryDistribution(distribution, vx.DISTRIBUTION_ATTRIBUTE_BINS, 'vx_size') == (vx.SUCCESS, 8)

        s, data = vx.AccessDistribution(distribution, None, vx.READ_AND_WRITE)
        assert s == vx.SUCCESS
        data[:4] = b'HHHH'
        assert vx.CommitDistribution(distribution, data) == vx.SUCCESS
        s, data = vx.AccessDistribution(distribution, None, vx.READ_ONLY)
        assert data[:4] == b'HHHH'
        assert vx.CommitDistribution(distribution, data) == vx.SUCCESS

        data = array('I', [0]) * 256
        vx.AccessDistribution(distribution, data, vx.READ_ONLY)
        assert data[0] == sum(ord('H') * i for i in [2**24 + 2**16 + 2**8 + 1])
        assert vx.CommitDistribution(distribution, data) == vx.SUCCESS

        assert vx.ReleaseDistribution(distribution) == vx.SUCCESS
        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_threshold(self):
        c = vx.CreateContext()
        threshold = vx.CreateThreshold(c, vx.THRESHOLD_TYPE_BINARY, vx.TYPE_UINT8)
        assert vx.GetStatus(vx.reference(threshold)) == vx.SUCCESS
        assert vx.QueryReference(vx.reference(threshold), vx.REF_ATTRIBUTE_TYPE, 'vx_enum') == (vx.SUCCESS, vx.TYPE_THRESHOLD)
        assert vx.QueryThreshold(threshold, vx.THRESHOLD_ATTRIBUTE_TYPE, 'vx_enum') == (vx.SUCCESS, vx.THRESHOLD_TYPE_BINARY)
        assert vx.SetThresholdAttribute(threshold, vx.THRESHOLD_ATTRIBUTE_THRESHOLD_VALUE, 7, 'vx_int32') == vx.SUCCESS
        assert vx.QueryThreshold(threshold, vx.THRESHOLD_ATTRIBUTE_THRESHOLD_VALUE, 'vx_int32') == (vx.SUCCESS, 7)
        assert vx.ReleaseThreshold(threshold) == vx.SUCCESS
        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_matrix(self):
        c = vx.CreateContext()
        matrix = vx.CreateMatrix(c, vx.TYPE_INT32, 3, 3)
        assert vx.GetStatus(vx.reference(matrix)) == vx.SUCCESS
        assert vx.QueryReference(vx.reference(matrix), vx.REF_ATTRIBUTE_TYPE, 'vx_enum') == (vx.SUCCESS, vx.TYPE_MATRIX)
        assert vx.QueryMatrix(matrix, vx.MATRIX_ATTRIBUTE_COLUMNS, 'vx_size') == (vx.SUCCESS, 3)

        data = array('i', [42]) * 9
        assert vx.WriteMatrix(matrix, data) == vx.SUCCESS
        data = array('i', [0]) * 9
        assert vx.ReadMatrix(matrix, data) == vx.SUCCESS
        assert data[0] == 42

        assert vx.ReleaseMatrix(matrix) == vx.SUCCESS
        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_convolution(self):
        c = vx.CreateContext()
        convolution = vx.CreateConvolution(c, 3, 3)
        assert vx.GetStatus(vx.reference(convolution)) == vx.SUCCESS
        assert vx.QueryReference(vx.reference(convolution), vx.REF_ATTRIBUTE_TYPE, 'vx_enum') == (vx.SUCCESS, vx.TYPE_CONVOLUTION)
        assert vx.QueryConvolution(convolution, vx.CONVOLUTION_ATTRIBUTE_ROWS, 'vx_size') == (vx.SUCCESS, 3)

        data = array('i', [42]) * 9
        assert vx.WriteConvolutionCoefficients(convolution, data) == vx.SUCCESS
        data = array('i', [0]) * 9
        assert vx.ReadConvolutionCoefficients(convolution, data) == vx.SUCCESS
        assert data[0] == 42

        assert vx.SetConvolutionAttribute(convolution, vx.CONVOLUTION_ATTRIBUTE_SCALE, 8, 'vx_uint32') == vx.SUCCESS
        assert vx.QueryConvolution(convolution, vx.CONVOLUTION_ATTRIBUTE_SCALE, 'vx_uint32') == (vx.SUCCESS, 8)

        assert vx.ReleaseConvolution(convolution) == vx.SUCCESS
        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_pyramid(self):
        c = vx.CreateContext()
        pyramid = vx.CreatePyramid(c, 4, vx.SCALE_PYRAMID_HALF, 640, 480, vx.DF_IMAGE_U8)
        assert vx.GetStatus(vx.reference(pyramid)) == vx.SUCCESS
        assert vx.QueryReference(vx.reference(pyramid), vx.REF_ATTRIBUTE_TYPE, 'vx_enum') == (vx.SUCCESS, vx.TYPE_PYRAMID)
        assert vx.QueryPyramid(pyramid, vx.PYRAMID_ATTRIBUTE_WIDTH, 'vx_uint32') == (vx.SUCCESS, 640)
        img = vx.GetPyramidLevel(pyramid, 1)
        assert img
        assert vx.QueryImage(img, vx.IMAGE_ATTRIBUTE_WIDTH, 'vx_uint32') == (vx.SUCCESS, 320)

        g = vx.CreateGraph(c)
        p = vx.CreateVirtualPyramid(g, 3, vx.SCALE_PYRAMID_HALF, 0, 0, vx.DF_IMAGE_VIRT)
        assert vx.ReleasePyramid(p) == vx.SUCCESS

        assert vx.ReleasePyramid(pyramid) == vx.SUCCESS
        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_remap(self):
        c = vx.CreateContext()
        remap = vx.CreateRemap(c, 640, 480, 320, 240)
        assert vx.GetStatus(vx.reference(remap)) == vx.SUCCESS
        assert vx.QueryReference(vx.reference(remap), vx.REF_ATTRIBUTE_TYPE, 'vx_enum') == (vx.SUCCESS, vx.TYPE_REMAP)
        assert vx.QueryRemap(remap, vx.REMAP_ATTRIBUTE_DESTINATION_HEIGHT, 'vx_uint32') == (vx.SUCCESS, 240)
        assert vx.SetRemapPoint(remap, 10, 15, 20.5, 30.5) == vx.SUCCESS
        assert vx.GetRemapPoint(remap, 10, 15) == (vx.SUCCESS, 20.5, 30.5)
        assert vx.ReleaseRemap(remap) == vx.SUCCESS
        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_array(self):
        c = vx.CreateContext()
        arr = vx.CreateArray(c, vx.TYPE_COORDINATES2D, 64)
        assert vx.GetStatus(vx.reference(arr)) == vx.SUCCESS
        assert vx.QueryReference(vx.reference(arr), vx.REF_ATTRIBUTE_TYPE, 'vx_enum') == (vx.SUCCESS, vx.TYPE_ARRAY)
        assert vx.QueryArray(arr, vx.ARRAY_ATTRIBUTE_CAPACITY, 'vx_size') == (vx.SUCCESS, 64)
        s, size = vx.QueryArray(arr, vx.ARRAY_ATTRIBUTE_ITEMSIZE, 'vx_size')

        data = array('B', [0]) * size * 10
        d = vx.ArrayItem('vx_coordinates2d_t', data, 0, size)
        d.x, d.y, d[1].x, d[1].y = 1, 2, 3, 4
        assert vx.AddArrayItems(arr, 10, data, size) == vx.SUCCESS
        assert vx.AddArrayItems(arr, 10, d, size) == vx.SUCCESS
        assert vx.QueryArray(arr, vx.ARRAY_ATTRIBUTE_NUMITEMS, 'vx_size') == (vx.SUCCESS, 20)
        assert vx.TruncateArray(arr, 15) == vx.SUCCESS
        assert vx.QueryArray(arr, vx.ARRAY_ATTRIBUTE_NUMITEMS, 'vx_size') == (vx.SUCCESS, 15)

        status, stride, ptr = vx.AccessArrayRange(arr, 0, 14, None, None, vx.READ_AND_WRITE)
        assert status == vx.SUCCESS
        d0 = vx.ArrayItem('vx_coordinates2d_t', ptr, 0, stride)
        d1 = vx.ArrayItem('vx_coordinates2d_t', ptr, 1, stride)
        assert (d0.x, d0.y, d1.x, d1.y) == (1, 2, 3, 4)
        d1.y = 42
        assert vx.CommitArrayRange(arr, 0, 14, ptr) == vx.SUCCESS

        data = array('B', [0]) * size * 15 * 2
        status, stride, ptr = vx.AccessArrayRange(arr, 0, 14, size*2, data, vx.READ_AND_WRITE)
        assert stride == size*2
        d = vx.ArrayItem('vx_coordinates2d_t', data, 0, size)
        assert (d.x, d.y, d[2].x, d[2].y) == (1, 2, 3, 42)
        assert vx.CommitArrayRange(arr, 0, 14, ptr) == vx.SUCCESS

        g = vx.CreateGraph(c)
        a = vx.CreateVirtualArray(g, vx.TYPE_KEYPOINT, 64)
        assert vx.ReleaseArray(a) == vx.SUCCESS

        assert vx.ReleaseArray(arr) == vx.SUCCESS
        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_user_kernel(self):
        c = vx.CreateContext()

        def func(node, parameters, num):
            func.called = True
            assert num == 2
            input, output = vx.from_reference(parameters[0]), vx.from_reference(parameters[0])
            _, r = vx.GetValidRegionImage(input)
            _, addr, indata = vx.AccessImagePatch(input, r, 0, None, None, vx.READ_ONLY)
            _, addr, outdata = vx.AccessImagePatch(output, r, 0, None, None, vx.WRITE_ONLY)
            outdata[0], outdata[100] = indata[100], indata[0]
            vx.CommitImagePatch(output, r, 0, addr, outdata)
            vx.CommitImagePatch(input, r, 0, addr, indata)
            return vx.SUCCESS

        def validate_input(node, index):
            validate_input.called = True
            assert index == 0
            param = vx.GetParameterByIndex(node, index)
            image = vx.QueryParameter(param, vx.PARAMETER_ATTRIBUTE_REF, 'vx_image')[1]
            if vx.QueryImage(image, vx.IMAGE_ATTRIBUTE_FORMAT, 'vx_df_image') == (vx.SUCCESS, vx.DF_IMAGE_U8):
                s = vx.SUCCESS
            else:
                s = vx.ERROR_INVALID_VALUE
            vx.ReleaseImage(image)
            vx.ReleaseParameter(param)
            return s

        def validate_output(node, index, meta):
            validate_output.called = True
            assert index == 1
            param0 = vx.GetParameterByIndex(node, 0)
            input = vx.QueryParameter(param0, vx.PARAMETER_ATTRIBUTE_REF, 'vx_image')[1]
            param1 = vx.GetParameterByIndex(node, index)
            output = vx.QueryParameter(param1, vx.PARAMETER_ATTRIBUTE_REF, 'vx_image')[1]
            _, width = vx.QueryImage(input, vx.IMAGE_ATTRIBUTE_WIDTH, 'vx_uint32')
            _, height = vx.QueryImage(input, vx.IMAGE_ATTRIBUTE_HEIGHT, 'vx_uint32')
            vx.SetMetaFormatAttribute(meta, vx.IMAGE_ATTRIBUTE_WIDTH, width, 'vx_uint32')
            vx.SetMetaFormatAttribute(meta, vx.IMAGE_ATTRIBUTE_HEIGHT, height, 'vx_uint32')
            vx.SetMetaFormatAttribute(meta, vx.IMAGE_ATTRIBUTE_FORMAT, vx.DF_IMAGE_U8, 'vx_df_image')
            vx.ReleaseImage(input)
            vx.ReleaseImage(output)
            vx.ReleaseParameter(param0)
            vx.ReleaseParameter(param1)
            return vx.SUCCESS

        enum = vx.KERNEL_BASE(vx.ID_DEFAULT, 7) + 1
        kernel = vx.AddKernel(c, b"org.test.hello", enum, func, 2, validate_input, validate_output, None, None)
        assert vx.GetStatus(vx.reference(kernel)) == vx.SUCCESS
        assert vx.AddParameterToKernel(kernel, 0, vx.INPUT, vx.TYPE_IMAGE, vx.PARAMETER_STATE_REQUIRED) == vx.SUCCESS
        assert vx.AddParameterToKernel(kernel, 1, vx.OUTPUT, vx.TYPE_IMAGE, vx.PARAMETER_STATE_REQUIRED) == vx.SUCCESS
        assert vx.SetKernelAttribute(kernel, vx.KERNEL_ATTRIBUTE_LOCAL_DATA_SIZE, 42, 'vx_size') == vx.SUCCESS
        assert vx.FinalizeKernel(kernel) == vx.SUCCESS

        g = vx.CreateGraph(c)
        img = vx.CreateImage(c, 640, 480, vx.DF_IMAGE_U8)
        _, r = vx.GetValidRegionImage(img)
        assert r.start_x == 0
        assert r.end_x == 640
        _, addr, data = vx.AccessImagePatch(img, r, 0, None, None, vx.WRITE_ONLY)
        data[0], data[100] = b'H', b'I'
        assert vx.CommitImagePatch(img, r, 0, addr, data) == vx.SUCCESS

        virt = vx.CreateVirtualImage(g, 0, 0, vx.DF_IMAGE_VIRT)
        # virt = vx.CreateImage(c, 640, 480, vx.DF_IMAGE_U8)
        node = vx.CreateGenericNode(g, kernel)
        vx.SetParameterByIndex(node, 0, vx.reference(img))
        vx.SetParameterByIndex(node, 1, vx.reference(virt))

        assert vx.VerifyGraph(g) == vx.SUCCESS
        assert validate_input.called
        assert validate_output.called
        assert vx.QueryImage(virt, vx.IMAGE_ATTRIBUTE_WIDTH, 'vx_uint32') == (vx.SUCCESS, 640)
        assert vx.QueryImage(virt, vx.IMAGE_ATTRIBUTE_HEIGHT, 'vx_uint32') == (vx.SUCCESS, 480)
        assert vx.ProcessGraph(g) == vx.SUCCESS
        assert func.called == True

        _, addr, data = vx.AccessImagePatch(virt, r, 0, None, None, vx.READ_ONLY)
        assert data[0], data[100] == 'IH'
        vx.CommitImagePatch(virt, r, 0, addr, data)

        img2 = vx.CreateImage(c, 640, 480, vx.DF_IMAGE_U16)
        vx.SetParameterByIndex(node, 0, vx.reference(img2))
        assert vx.VerifyGraph(g) == vx.ERROR_INVALID_VALUE


        enum = vx.KERNEL_BASE(vx.ID_DEFAULT, 7) + 2
        kernel = vx.AddKernel(c, b"org.test.hello2", enum, func, 2, validate_input, validate_output, None, None)
        assert vx.RemoveKernel(kernel) == vx.SUCCESS

        assert vx.ReleaseGraph(g) == vx.SUCCESS
        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_module(self):
        c = vx.CreateContext()
        assert vx.LoadKernels(c, "test.module") == vx.SUCCESS
        kernel = vx.GetKernelByName(c, b"org.test.module")
        assert vx.GetStatus(vx.reference(kernel)) == vx.SUCCESS
        assert vx.QueryKernel(kernel, vx.KERNEL_ATTRIBUTE_PARAMETERS, 'vx_uint32') == (vx.SUCCESS, 1)
        assert vx.ReleaseContext(c) == vx.SUCCESS

    def test_use_backend(self):
        for l in range(2):
            pyvx.use_backend("mock_backend")
            from pyvx import vx
            assert vx.CreateContext() == 42

            from test import mock_backend2
            pyvx.use_backend(mock_backend2)
            from pyvx import vx
            assert vx.CreateContext() == 7

            with raises(ImportError):
                pyvx.use_backend("none_excistant")

            pyvx.use_backend("_default")
            from pyvx import vx
            assert not isinstance(vx.CreateContext(), int)
