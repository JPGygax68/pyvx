from pyvx.backend import lib, ffi
ACTION_ABANDON = lib.VX_ACTION_ABANDON
ACTION_CONTINUE = lib.VX_ACTION_CONTINUE
ARRAY_CAPACITY = lib.VX_ARRAY_CAPACITY
ARRAY_ITEMSIZE = lib.VX_ARRAY_ITEMSIZE
ARRAY_ITEMTYPE = lib.VX_ARRAY_ITEMTYPE
ARRAY_NUMITEMS = lib.VX_ARRAY_NUMITEMS
ATTRIBUTE_ID_MASK = lib.VX_ATTRIBUTE_ID_MASK
BIDIRECTIONAL = lib.VX_BIDIRECTIONAL
BORDER_CONSTANT = lib.VX_BORDER_CONSTANT
BORDER_POLICY_DEFAULT_TO_UNDEFINED = lib.VX_BORDER_POLICY_DEFAULT_TO_UNDEFINED
BORDER_POLICY_RETURN_ERROR = lib.VX_BORDER_POLICY_RETURN_ERROR
BORDER_REPLICATE = lib.VX_BORDER_REPLICATE
BORDER_UNDEFINED = lib.VX_BORDER_UNDEFINED
CHANNEL_0 = lib.VX_CHANNEL_0
CHANNEL_1 = lib.VX_CHANNEL_1
CHANNEL_2 = lib.VX_CHANNEL_2
CHANNEL_3 = lib.VX_CHANNEL_3
CHANNEL_A = lib.VX_CHANNEL_A
CHANNEL_B = lib.VX_CHANNEL_B
CHANNEL_G = lib.VX_CHANNEL_G
CHANNEL_R = lib.VX_CHANNEL_R
CHANNEL_RANGE_FULL = lib.VX_CHANNEL_RANGE_FULL
CHANNEL_RANGE_RESTRICTED = lib.VX_CHANNEL_RANGE_RESTRICTED
CHANNEL_U = lib.VX_CHANNEL_U
CHANNEL_V = lib.VX_CHANNEL_V
CHANNEL_Y = lib.VX_CHANNEL_Y
COLOR_SPACE_BT601_525 = lib.VX_COLOR_SPACE_BT601_525
COLOR_SPACE_BT601_625 = lib.VX_COLOR_SPACE_BT601_625
COLOR_SPACE_BT709 = lib.VX_COLOR_SPACE_BT709
COLOR_SPACE_DEFAULT = lib.VX_COLOR_SPACE_DEFAULT
COLOR_SPACE_NONE = lib.VX_COLOR_SPACE_NONE
CONTEXT_CONVOLUTION_MAX_DIMENSION = lib.VX_CONTEXT_CONVOLUTION_MAX_DIMENSION
CONTEXT_EXTENSIONS = lib.VX_CONTEXT_EXTENSIONS
CONTEXT_EXTENSIONS_SIZE = lib.VX_CONTEXT_EXTENSIONS_SIZE
CONTEXT_IMMEDIATE_BORDER = lib.VX_CONTEXT_IMMEDIATE_BORDER
CONTEXT_IMMEDIATE_BORDER_POLICY = lib.VX_CONTEXT_IMMEDIATE_BORDER_POLICY
CONTEXT_IMPLEMENTATION = lib.VX_CONTEXT_IMPLEMENTATION
CONTEXT_MODULES = lib.VX_CONTEXT_MODULES
CONTEXT_NONLINEAR_MAX_DIMENSION = lib.VX_CONTEXT_NONLINEAR_MAX_DIMENSION
CONTEXT_OPTICAL_FLOW_MAX_WINDOW_DIMENSION = lib.VX_CONTEXT_OPTICAL_FLOW_MAX_WINDOW_DIMENSION
CONTEXT_REFERENCES = lib.VX_CONTEXT_REFERENCES
CONTEXT_UNIQUE_KERNELS = lib.VX_CONTEXT_UNIQUE_KERNELS
CONTEXT_UNIQUE_KERNEL_TABLE = lib.VX_CONTEXT_UNIQUE_KERNEL_TABLE
CONTEXT_VENDOR_ID = lib.VX_CONTEXT_VENDOR_ID
CONTEXT_VERSION = lib.VX_CONTEXT_VERSION
CONVERT_POLICY_SATURATE = lib.VX_CONVERT_POLICY_SATURATE
CONVERT_POLICY_WRAP = lib.VX_CONVERT_POLICY_WRAP
CONVOLUTION_COLUMNS = lib.VX_CONVOLUTION_COLUMNS
CONVOLUTION_ROWS = lib.VX_CONVOLUTION_ROWS
CONVOLUTION_SCALE = lib.VX_CONVOLUTION_SCALE
CONVOLUTION_SIZE = lib.VX_CONVOLUTION_SIZE
DELAY_SLOTS = lib.VX_DELAY_SLOTS
DELAY_TYPE = lib.VX_DELAY_TYPE
DF_IMAGE_IYUV = lib.VX_DF_IMAGE_IYUV
DF_IMAGE_NV12 = lib.VX_DF_IMAGE_NV12
DF_IMAGE_NV21 = lib.VX_DF_IMAGE_NV21
DF_IMAGE_RGB = lib.VX_DF_IMAGE_RGB
DF_IMAGE_RGBX = lib.VX_DF_IMAGE_RGBX
DF_IMAGE_S16 = lib.VX_DF_IMAGE_S16
DF_IMAGE_S32 = lib.VX_DF_IMAGE_S32
DF_IMAGE_U16 = lib.VX_DF_IMAGE_U16
DF_IMAGE_U32 = lib.VX_DF_IMAGE_U32
DF_IMAGE_U8 = lib.VX_DF_IMAGE_U8
DF_IMAGE_UYVY = lib.VX_DF_IMAGE_UYVY
DF_IMAGE_VIRT = lib.VX_DF_IMAGE_VIRT
DF_IMAGE_YUV4 = lib.VX_DF_IMAGE_YUV4
DF_IMAGE_YUYV = lib.VX_DF_IMAGE_YUYV
DIRECTIVE_DISABLE_LOGGING = lib.VX_DIRECTIVE_DISABLE_LOGGING
DIRECTIVE_DISABLE_PERFORMANCE = lib.VX_DIRECTIVE_DISABLE_PERFORMANCE
DIRECTIVE_ENABLE_LOGGING = lib.VX_DIRECTIVE_ENABLE_LOGGING
DIRECTIVE_ENABLE_PERFORMANCE = lib.VX_DIRECTIVE_ENABLE_PERFORMANCE
DISTRIBUTION_BINS = lib.VX_DISTRIBUTION_BINS
DISTRIBUTION_DIMENSIONS = lib.VX_DISTRIBUTION_DIMENSIONS
DISTRIBUTION_OFFSET = lib.VX_DISTRIBUTION_OFFSET
DISTRIBUTION_RANGE = lib.VX_DISTRIBUTION_RANGE
DISTRIBUTION_SIZE = lib.VX_DISTRIBUTION_SIZE
DISTRIBUTION_WINDOW = lib.VX_DISTRIBUTION_WINDOW
ENUM_ACCESSOR = lib.VX_ENUM_ACCESSOR
ENUM_ACTION = lib.VX_ENUM_ACTION
ENUM_BORDER = lib.VX_ENUM_BORDER
ENUM_BORDER_POLICY = lib.VX_ENUM_BORDER_POLICY
ENUM_CHANNEL = lib.VX_ENUM_CHANNEL
ENUM_COLOR_RANGE = lib.VX_ENUM_COLOR_RANGE
ENUM_COLOR_SPACE = lib.VX_ENUM_COLOR_SPACE
ENUM_COMPARISON = lib.VX_ENUM_COMPARISON
ENUM_CONVERT_POLICY = lib.VX_ENUM_CONVERT_POLICY
ENUM_DIRECTION = lib.VX_ENUM_DIRECTION
ENUM_DIRECTIVE = lib.VX_ENUM_DIRECTIVE
ENUM_GRAPH_STATE = lib.VX_ENUM_GRAPH_STATE
ENUM_HINT = lib.VX_ENUM_HINT
ENUM_INTERPOLATION = lib.VX_ENUM_INTERPOLATION
ENUM_MASK = lib.VX_ENUM_MASK
ENUM_MEMORY_TYPE = lib.VX_ENUM_MEMORY_TYPE
ENUM_NONLINEAR = lib.VX_ENUM_NONLINEAR
ENUM_NORM_TYPE = lib.VX_ENUM_NORM_TYPE
ENUM_OVERFLOW = lib.VX_ENUM_OVERFLOW
ENUM_PARAMETER_STATE = lib.VX_ENUM_PARAMETER_STATE
ENUM_PATTERN = lib.VX_ENUM_PATTERN
ENUM_ROUND_POLICY = lib.VX_ENUM_ROUND_POLICY
ENUM_TARGET = lib.VX_ENUM_TARGET
ENUM_TERM_CRITERIA = lib.VX_ENUM_TERM_CRITERIA
ENUM_THRESHOLD_TYPE = lib.VX_ENUM_THRESHOLD_TYPE
ENUM_TYPE_MASK = lib.VX_ENUM_TYPE_MASK
ERROR_GRAPH_ABANDONED = lib.VX_ERROR_GRAPH_ABANDONED
ERROR_GRAPH_SCHEDULED = lib.VX_ERROR_GRAPH_SCHEDULED
ERROR_INVALID_DIMENSION = lib.VX_ERROR_INVALID_DIMENSION
ERROR_INVALID_FORMAT = lib.VX_ERROR_INVALID_FORMAT
ERROR_INVALID_GRAPH = lib.VX_ERROR_INVALID_GRAPH
ERROR_INVALID_LINK = lib.VX_ERROR_INVALID_LINK
ERROR_INVALID_MODULE = lib.VX_ERROR_INVALID_MODULE
ERROR_INVALID_NODE = lib.VX_ERROR_INVALID_NODE
ERROR_INVALID_PARAMETERS = lib.VX_ERROR_INVALID_PARAMETERS
ERROR_INVALID_REFERENCE = lib.VX_ERROR_INVALID_REFERENCE
ERROR_INVALID_SCOPE = lib.VX_ERROR_INVALID_SCOPE
ERROR_INVALID_TYPE = lib.VX_ERROR_INVALID_TYPE
ERROR_INVALID_VALUE = lib.VX_ERROR_INVALID_VALUE
ERROR_MULTIPLE_WRITERS = lib.VX_ERROR_MULTIPLE_WRITERS
ERROR_NOT_ALLOCATED = lib.VX_ERROR_NOT_ALLOCATED
ERROR_NOT_COMPATIBLE = lib.VX_ERROR_NOT_COMPATIBLE
ERROR_NOT_IMPLEMENTED = lib.VX_ERROR_NOT_IMPLEMENTED
ERROR_NOT_SUFFICIENT = lib.VX_ERROR_NOT_SUFFICIENT
ERROR_NOT_SUPPORTED = lib.VX_ERROR_NOT_SUPPORTED
ERROR_NO_MEMORY = lib.VX_ERROR_NO_MEMORY
ERROR_NO_RESOURCES = lib.VX_ERROR_NO_RESOURCES
ERROR_OPTIMIZED_AWAY = lib.VX_ERROR_OPTIMIZED_AWAY
ERROR_REFERENCE_NONZERO = lib.VX_ERROR_REFERENCE_NONZERO
FAILURE = lib.VX_FAILURE
GRAPH_NUMNODES = lib.VX_GRAPH_NUMNODES
GRAPH_NUMPARAMETERS = lib.VX_GRAPH_NUMPARAMETERS
GRAPH_PERFORMANCE = lib.VX_GRAPH_PERFORMANCE
GRAPH_STATE = lib.VX_GRAPH_STATE
GRAPH_STATE_ABANDONED = lib.VX_GRAPH_STATE_ABANDONED
GRAPH_STATE_COMPLETED = lib.VX_GRAPH_STATE_COMPLETED
GRAPH_STATE_RUNNING = lib.VX_GRAPH_STATE_RUNNING
GRAPH_STATE_UNVERIFIED = lib.VX_GRAPH_STATE_UNVERIFIED
GRAPH_STATE_VERIFIED = lib.VX_GRAPH_STATE_VERIFIED
HINT_PERFORMANCE_DEFAULT = lib.VX_HINT_PERFORMANCE_DEFAULT
HINT_PERFORMANCE_HIGH_SPEED = lib.VX_HINT_PERFORMANCE_HIGH_SPEED
HINT_PERFORMANCE_LOW_POWER = lib.VX_HINT_PERFORMANCE_LOW_POWER
ID_AMD = lib.VX_ID_AMD
ID_ARM = lib.VX_ID_ARM
ID_AXIS = lib.VX_ID_AXIS
ID_BDTI = lib.VX_ID_BDTI
ID_BROADCOM = lib.VX_ID_BROADCOM
ID_CADENCE = lib.VX_ID_CADENCE
ID_CEVA = lib.VX_ID_CEVA
ID_DEFAULT = lib.VX_ID_DEFAULT
ID_FREESCALE = lib.VX_ID_FREESCALE
ID_HUAWEI = lib.VX_ID_HUAWEI
ID_IMAGINATION = lib.VX_ID_IMAGINATION
ID_INTEL = lib.VX_ID_INTEL
ID_ITSEEZ = lib.VX_ID_ITSEEZ
ID_KHRONOS = lib.VX_ID_KHRONOS
ID_MARVELL = lib.VX_ID_MARVELL
ID_MAX = lib.VX_ID_MAX
ID_MEDIATEK = lib.VX_ID_MEDIATEK
ID_MOVIDIUS = lib.VX_ID_MOVIDIUS
ID_NVIDIA = lib.VX_ID_NVIDIA
ID_NXP = lib.VX_ID_NXP
ID_QUALCOMM = lib.VX_ID_QUALCOMM
ID_RENESAS = lib.VX_ID_RENESAS
ID_SAMSUNG = lib.VX_ID_SAMSUNG
ID_ST = lib.VX_ID_ST
ID_SYNOPSYS = lib.VX_ID_SYNOPSYS
ID_TI = lib.VX_ID_TI
ID_USER = lib.VX_ID_USER
ID_VIDEANTIS = lib.VX_ID_VIDEANTIS
ID_VIVANTE = lib.VX_ID_VIVANTE
ID_XILINX = lib.VX_ID_XILINX
IMAGE_FORMAT = lib.VX_IMAGE_FORMAT
IMAGE_HEIGHT = lib.VX_IMAGE_HEIGHT
IMAGE_MEMORY_TYPE = lib.VX_IMAGE_MEMORY_TYPE
IMAGE_PLANES = lib.VX_IMAGE_PLANES
IMAGE_RANGE = lib.VX_IMAGE_RANGE
IMAGE_SIZE = lib.VX_IMAGE_SIZE
IMAGE_SPACE = lib.VX_IMAGE_SPACE
IMAGE_WIDTH = lib.VX_IMAGE_WIDTH
INPUT = lib.VX_INPUT
INTERPOLATION_AREA = lib.VX_INTERPOLATION_AREA
INTERPOLATION_BILINEAR = lib.VX_INTERPOLATION_BILINEAR
INTERPOLATION_NEAREST_NEIGHBOR = lib.VX_INTERPOLATION_NEAREST_NEIGHBOR
KERNEL_ABSDIFF = lib.VX_KERNEL_ABSDIFF
KERNEL_ACCUMULATE = lib.VX_KERNEL_ACCUMULATE
KERNEL_ACCUMULATE_SQUARE = lib.VX_KERNEL_ACCUMULATE_SQUARE
KERNEL_ACCUMULATE_WEIGHTED = lib.VX_KERNEL_ACCUMULATE_WEIGHTED
KERNEL_ADD = lib.VX_KERNEL_ADD
KERNEL_AND = lib.VX_KERNEL_AND
KERNEL_BOX_3x3 = lib.VX_KERNEL_BOX_3x3
KERNEL_CANNY_EDGE_DETECTOR = lib.VX_KERNEL_CANNY_EDGE_DETECTOR
KERNEL_CHANNEL_COMBINE = lib.VX_KERNEL_CHANNEL_COMBINE
KERNEL_CHANNEL_EXTRACT = lib.VX_KERNEL_CHANNEL_EXTRACT
KERNEL_COLOR_CONVERT = lib.VX_KERNEL_COLOR_CONVERT
KERNEL_CONVERTDEPTH = lib.VX_KERNEL_CONVERTDEPTH
KERNEL_CUSTOM_CONVOLUTION = lib.VX_KERNEL_CUSTOM_CONVOLUTION
KERNEL_DILATE_3x3 = lib.VX_KERNEL_DILATE_3x3
KERNEL_ENUM = lib.VX_KERNEL_ENUM
KERNEL_EQUALIZE_HISTOGRAM = lib.VX_KERNEL_EQUALIZE_HISTOGRAM
KERNEL_ERODE_3x3 = lib.VX_KERNEL_ERODE_3x3
KERNEL_FAST_CORNERS = lib.VX_KERNEL_FAST_CORNERS
KERNEL_GAUSSIAN_3x3 = lib.VX_KERNEL_GAUSSIAN_3x3
KERNEL_GAUSSIAN_PYRAMID = lib.VX_KERNEL_GAUSSIAN_PYRAMID
KERNEL_HALFSCALE_GAUSSIAN = lib.VX_KERNEL_HALFSCALE_GAUSSIAN
KERNEL_HARRIS_CORNERS = lib.VX_KERNEL_HARRIS_CORNERS
KERNEL_HISTOGRAM = lib.VX_KERNEL_HISTOGRAM
KERNEL_INTEGRAL_IMAGE = lib.VX_KERNEL_INTEGRAL_IMAGE
KERNEL_LAPLACIAN_PYRAMID = lib.VX_KERNEL_LAPLACIAN_PYRAMID
KERNEL_LAPLACIAN_RECONSTRUCT = lib.VX_KERNEL_LAPLACIAN_RECONSTRUCT
KERNEL_LOCAL_DATA_SIZE = lib.VX_KERNEL_LOCAL_DATA_SIZE
KERNEL_MAGNITUDE = lib.VX_KERNEL_MAGNITUDE
KERNEL_MASK = lib.VX_KERNEL_MASK
KERNEL_MAX_1_0 = lib.VX_KERNEL_MAX_1_0
KERNEL_MEAN_STDDEV = lib.VX_KERNEL_MEAN_STDDEV
KERNEL_MEDIAN_3x3 = lib.VX_KERNEL_MEDIAN_3x3
KERNEL_MINMAXLOC = lib.VX_KERNEL_MINMAXLOC
KERNEL_MULTIPLY = lib.VX_KERNEL_MULTIPLY
KERNEL_NAME = lib.VX_KERNEL_NAME
KERNEL_NON_LINEAR_FILTER = lib.VX_KERNEL_NON_LINEAR_FILTER
KERNEL_NOT = lib.VX_KERNEL_NOT
KERNEL_OPTICAL_FLOW_PYR_LK = lib.VX_KERNEL_OPTICAL_FLOW_PYR_LK
KERNEL_OR = lib.VX_KERNEL_OR
KERNEL_PARAMETERS = lib.VX_KERNEL_PARAMETERS
KERNEL_PHASE = lib.VX_KERNEL_PHASE
KERNEL_REMAP = lib.VX_KERNEL_REMAP
KERNEL_SCALE_IMAGE = lib.VX_KERNEL_SCALE_IMAGE
KERNEL_SOBEL_3x3 = lib.VX_KERNEL_SOBEL_3x3
KERNEL_SUBTRACT = lib.VX_KERNEL_SUBTRACT
KERNEL_TABLE_LOOKUP = lib.VX_KERNEL_TABLE_LOOKUP
KERNEL_THRESHOLD = lib.VX_KERNEL_THRESHOLD
KERNEL_WARP_AFFINE = lib.VX_KERNEL_WARP_AFFINE
KERNEL_WARP_PERSPECTIVE = lib.VX_KERNEL_WARP_PERSPECTIVE
KERNEL_XOR = lib.VX_KERNEL_XOR
LIBRARY_KHR_BASE = lib.VX_LIBRARY_KHR_BASE
LIBRARY_MASK = lib.VX_LIBRARY_MASK
LUT_COUNT = lib.VX_LUT_COUNT
LUT_OFFSET = lib.VX_LUT_OFFSET
LUT_SIZE = lib.VX_LUT_SIZE
LUT_TYPE = lib.VX_LUT_TYPE
MATRIX_COLUMNS = lib.VX_MATRIX_COLUMNS
MATRIX_ORIGIN = lib.VX_MATRIX_ORIGIN
MATRIX_PATTERN = lib.VX_MATRIX_PATTERN
MATRIX_ROWS = lib.VX_MATRIX_ROWS
MATRIX_SIZE = lib.VX_MATRIX_SIZE
MATRIX_TYPE = lib.VX_MATRIX_TYPE
MAX_IMPLEMENTATION_NAME = lib.VX_MAX_IMPLEMENTATION_NAME
MAX_KERNEL_NAME = lib.VX_MAX_KERNEL_NAME
MAX_LOG_MESSAGE_LEN = lib.VX_MAX_LOG_MESSAGE_LEN
MAX_REFERENCE_NAME = lib.VX_MAX_REFERENCE_NAME
MEMORY_TYPE_HOST = lib.VX_MEMORY_TYPE_HOST
MEMORY_TYPE_NONE = lib.VX_MEMORY_TYPE_NONE
NODE_BORDER = lib.VX_NODE_BORDER
NODE_IS_REPLICATED = lib.VX_NODE_IS_REPLICATED
NODE_LOCAL_DATA_PTR = lib.VX_NODE_LOCAL_DATA_PTR
NODE_LOCAL_DATA_SIZE = lib.VX_NODE_LOCAL_DATA_SIZE
NODE_PARAMETERS = lib.VX_NODE_PARAMETERS
NODE_PERFORMANCE = lib.VX_NODE_PERFORMANCE
NODE_REPLICATE_FLAGS = lib.VX_NODE_REPLICATE_FLAGS
NODE_STATUS = lib.VX_NODE_STATUS
NODE_VALID_RECT_RESET = lib.VX_NODE_VALID_RECT_RESET
NOGAP_X = lib.VX_NOGAP_X
NONLINEAR_FILTER_MAX = lib.VX_NONLINEAR_FILTER_MAX
NONLINEAR_FILTER_MEDIAN = lib.VX_NONLINEAR_FILTER_MEDIAN
NONLINEAR_FILTER_MIN = lib.VX_NONLINEAR_FILTER_MIN
NORM_L1 = lib.VX_NORM_L1
NORM_L2 = lib.VX_NORM_L2
OBJECT_ARRAY_ITEMTYPE = lib.VX_OBJECT_ARRAY_ITEMTYPE
OBJECT_ARRAY_NUMITEMS = lib.VX_OBJECT_ARRAY_NUMITEMS
OUTPUT = lib.VX_OUTPUT
PARAMETER_DIRECTION = lib.VX_PARAMETER_DIRECTION
PARAMETER_INDEX = lib.VX_PARAMETER_INDEX
PARAMETER_REF = lib.VX_PARAMETER_REF
PARAMETER_STATE = lib.VX_PARAMETER_STATE
PARAMETER_STATE_OPTIONAL = lib.VX_PARAMETER_STATE_OPTIONAL
PARAMETER_STATE_REQUIRED = lib.VX_PARAMETER_STATE_REQUIRED
PARAMETER_TYPE = lib.VX_PARAMETER_TYPE
PATTERN_BOX = lib.VX_PATTERN_BOX
PATTERN_CROSS = lib.VX_PATTERN_CROSS
PATTERN_DISK = lib.VX_PATTERN_DISK
PATTERN_OTHER = lib.VX_PATTERN_OTHER
PYRAMID_FORMAT = lib.VX_PYRAMID_FORMAT
PYRAMID_HEIGHT = lib.VX_PYRAMID_HEIGHT
PYRAMID_LEVELS = lib.VX_PYRAMID_LEVELS
PYRAMID_SCALE = lib.VX_PYRAMID_SCALE
PYRAMID_WIDTH = lib.VX_PYRAMID_WIDTH
READ_AND_WRITE = lib.VX_READ_AND_WRITE
READ_ONLY = lib.VX_READ_ONLY
REF_ATTRIBUTE_COUNT = lib.VX_REF_ATTRIBUTE_COUNT
REF_ATTRIBUTE_NAME = lib.VX_REF_ATTRIBUTE_NAME
REF_ATTRIBUTE_TYPE = lib.VX_REF_ATTRIBUTE_TYPE
REMAP_DESTINATION_HEIGHT = lib.VX_REMAP_DESTINATION_HEIGHT
REMAP_DESTINATION_WIDTH = lib.VX_REMAP_DESTINATION_WIDTH
REMAP_SOURCE_HEIGHT = lib.VX_REMAP_SOURCE_HEIGHT
REMAP_SOURCE_WIDTH = lib.VX_REMAP_SOURCE_WIDTH
ROUND_POLICY_TO_NEAREST_EVEN = lib.VX_ROUND_POLICY_TO_NEAREST_EVEN
ROUND_POLICY_TO_ZERO = lib.VX_ROUND_POLICY_TO_ZERO
SCALAR_TYPE = lib.VX_SCALAR_TYPE
SCALE_UNITY = lib.VX_SCALE_UNITY
STATUS_MIN = lib.VX_STATUS_MIN
SUCCESS = lib.VX_SUCCESS
TARGET_ANY = lib.VX_TARGET_ANY
TARGET_STRING = lib.VX_TARGET_STRING
TARGET_VENDOR_BEGIN = lib.VX_TARGET_VENDOR_BEGIN
TERM_CRITERIA_BOTH = lib.VX_TERM_CRITERIA_BOTH
TERM_CRITERIA_EPSILON = lib.VX_TERM_CRITERIA_EPSILON
TERM_CRITERIA_ITERATIONS = lib.VX_TERM_CRITERIA_ITERATIONS
THRESHOLD_DATA_TYPE = lib.VX_THRESHOLD_DATA_TYPE
THRESHOLD_FALSE_VALUE = lib.VX_THRESHOLD_FALSE_VALUE
THRESHOLD_THRESHOLD_LOWER = lib.VX_THRESHOLD_THRESHOLD_LOWER
THRESHOLD_THRESHOLD_UPPER = lib.VX_THRESHOLD_THRESHOLD_UPPER
THRESHOLD_THRESHOLD_VALUE = lib.VX_THRESHOLD_THRESHOLD_VALUE
THRESHOLD_TRUE_VALUE = lib.VX_THRESHOLD_TRUE_VALUE
THRESHOLD_TYPE = lib.VX_THRESHOLD_TYPE
THRESHOLD_TYPE_BINARY = lib.VX_THRESHOLD_TYPE_BINARY
THRESHOLD_TYPE_RANGE = lib.VX_THRESHOLD_TYPE_RANGE
TYPE_ARRAY = lib.VX_TYPE_ARRAY
TYPE_BOOL = lib.VX_TYPE_BOOL
TYPE_CHAR = lib.VX_TYPE_CHAR
TYPE_CONTEXT = lib.VX_TYPE_CONTEXT
TYPE_CONVOLUTION = lib.VX_TYPE_CONVOLUTION
TYPE_COORDINATES2D = lib.VX_TYPE_COORDINATES2D
TYPE_COORDINATES3D = lib.VX_TYPE_COORDINATES3D
TYPE_DELAY = lib.VX_TYPE_DELAY
TYPE_DF_IMAGE = lib.VX_TYPE_DF_IMAGE
TYPE_DISTRIBUTION = lib.VX_TYPE_DISTRIBUTION
TYPE_ENUM = lib.VX_TYPE_ENUM
TYPE_ERROR = lib.VX_TYPE_ERROR
TYPE_FLOAT32 = lib.VX_TYPE_FLOAT32
TYPE_FLOAT64 = lib.VX_TYPE_FLOAT64
TYPE_GRAPH = lib.VX_TYPE_GRAPH
TYPE_IMAGE = lib.VX_TYPE_IMAGE
TYPE_INT16 = lib.VX_TYPE_INT16
TYPE_INT32 = lib.VX_TYPE_INT32
TYPE_INT64 = lib.VX_TYPE_INT64
TYPE_INT8 = lib.VX_TYPE_INT8
TYPE_INVALID = lib.VX_TYPE_INVALID
TYPE_KERNEL = lib.VX_TYPE_KERNEL
TYPE_KEYPOINT = lib.VX_TYPE_KEYPOINT
TYPE_KHRONOS_OBJECT_END = lib.VX_TYPE_KHRONOS_OBJECT_END
TYPE_KHRONOS_OBJECT_START = lib.VX_TYPE_KHRONOS_OBJECT_START
TYPE_KHRONOS_STRUCT_MAX = lib.VX_TYPE_KHRONOS_STRUCT_MAX
TYPE_LUT = lib.VX_TYPE_LUT
TYPE_MASK = lib.VX_TYPE_MASK
TYPE_MATRIX = lib.VX_TYPE_MATRIX
TYPE_META_FORMAT = lib.VX_TYPE_META_FORMAT
TYPE_NODE = lib.VX_TYPE_NODE
TYPE_OBJECT_ARRAY = lib.VX_TYPE_OBJECT_ARRAY
TYPE_PARAMETER = lib.VX_TYPE_PARAMETER
TYPE_PYRAMID = lib.VX_TYPE_PYRAMID
TYPE_RECTANGLE = lib.VX_TYPE_RECTANGLE
TYPE_REFERENCE = lib.VX_TYPE_REFERENCE
TYPE_REMAP = lib.VX_TYPE_REMAP
TYPE_SCALAR = lib.VX_TYPE_SCALAR
TYPE_SCALAR_MAX = lib.VX_TYPE_SCALAR_MAX
TYPE_SIZE = lib.VX_TYPE_SIZE
TYPE_THRESHOLD = lib.VX_TYPE_THRESHOLD
TYPE_UINT16 = lib.VX_TYPE_UINT16
TYPE_UINT32 = lib.VX_TYPE_UINT32
TYPE_UINT64 = lib.VX_TYPE_UINT64
TYPE_UINT8 = lib.VX_TYPE_UINT8
TYPE_USER_STRUCT_END = lib.VX_TYPE_USER_STRUCT_END
TYPE_USER_STRUCT_START = lib.VX_TYPE_USER_STRUCT_START
TYPE_VENDOR_OBJECT_END = lib.VX_TYPE_VENDOR_OBJECT_END
TYPE_VENDOR_OBJECT_START = lib.VX_TYPE_VENDOR_OBJECT_START
TYPE_VENDOR_STRUCT_END = lib.VX_TYPE_VENDOR_STRUCT_END
TYPE_VENDOR_STRUCT_START = lib.VX_TYPE_VENDOR_STRUCT_START
VALID_RECT_CALLBACK = lib.VX_VALID_RECT_CALLBACK
VENDOR_MASK = lib.VX_VENDOR_MASK
WRITE_ONLY = lib.VX_WRITE_ONLY

def CreateContext():
    '''
Creates a *vx_context*.
 :details: This creates a top-level object context for OpenVX.
 :note: This is required to do anything else.
 :returns: The reference to the implementation context *vx_context*. Any possible errors  preventing a successful creation should be checked using *vxGetStatus*.
 :ingroup: group_context
 :post: *vxReleaseContext*  
    '''
    return lib.vxCreateContext()
    
def ReleaseContext(context):
    '''
Releases the OpenVX object context.
 :details: All reference counted objects are garbage-collected by the return of this call. No calls are possible using the parameter context after the context has been released until a new reference from *vxCreateContext* is returned. All outstanding references to OpenVX objects from this context are invalid after this call.
 :param context: [in] The pointer to the reference to the context.
 :post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If context is not a *vx_context*.
 :ingroup: group_context
 :pre: *vxCreateContext*  
    '''
    return lib.vxReleaseContext(context)
    
def GetContext(reference):
    '''
Retrieves the context from any reference from within a context.
 :param reference: [in] The reference from which to extract the context.
 :ingroup: group_context
:return: The overall context that created the particular reference. Any possible errors preventing a successful creation should be  checked using *vxGetStatus*.  
    '''
    return lib.vxGetContext(reference)
    
def QueryContext(context, attribute, ptr, size):
    '''
Queries the context for some specific information.
 :param context: [in] The reference to the context.
 :param attribute: [in] The attribute to query. Use a *vx_context_attribute_e*.
 :param ptr: [out] The location at which to store the resulting value.
 :param size: [in] The size in bytes of the container to which *ptr* points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If the context is not a *vx_context*.
:retval: VX_ERROR_INVALID_PARAMETERS If any of the other parameters are incorrect.
:retval: VX_ERROR_NOT_SUPPORTED If the attribute is not supported on this implementation.
 :ingroup: group_context  
    '''
    return lib.vxQueryContext(context, attribute, ptr, size)
    
def SetContextAttribute(context, attribute, ptr, size):
    '''
Sets an attribute on the context.
 :param context: [in] The handle to the overall context.
 :param attribute: [in] The attribute to set from *vx_context_attribute_e*.
 :param ptr: [in] The pointer to the data to which to set the attribute.
 :param size: [in] The size in bytes of the data to which *ptr* points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If the context is not a *vx_context*.
:retval: VX_ERROR_INVALID_PARAMETERS If any of the other parameters are incorrect.
:retval: VX_ERROR_NOT_SUPPORTED If the attribute is not settable.
 :ingroup: group_context  
    '''
    return lib.vxSetContextAttribute(context, attribute, ptr, size)
    
def Hint(reference, hint, data, data_size):
    '''
Provides a generic API to give platform-specific hints to the implementation.
 :param reference: [in] The reference to the object to hint at. This could be *vx_context*, *vx_graph*, *vx_node*, *vx_image*, *vx_array*, or any other reference.
 :param hint: [in] A *vx_hint_e* *hint* to give to a vx_context. This is a platform-specific optimization or implementation mechanism.
 :param data: [in] Optional vendor specific data. 
 :param data_size: [in] Size of the data structure  :p: data.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No error.
:retval: VX_ERROR_INVALID_REFERENCE If context or reference is invalid.
:retval: VX_ERROR_NOT_SUPPORTED If the hint is not supported.
 :ingroup: group_hint  
    '''
    return lib.vxHint(reference, hint, data, data_size)
    
def Directive(reference, directive):
    '''
Provides a generic API to give platform-specific directives to the implementations.
 :param reference: [in] The reference to the object to set the directive on. This could be *vx_context*, *vx_graph*, *vx_node*, *vx_image*, *vx_array*, or any other reference.
 :param directive: [in] The directive to set. See *vx_directive_e*. 
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No error.
:retval: VX_ERROR_INVALID_REFERENCE If context or reference is invalid.
:retval: VX_ERROR_NOT_SUPPORTED If the directive is not supported.
 :note: The performance counter directives are only available for the reference vx_context.  Error VX_ERROR_NOT_SUPPORTED is returned when used with any other reference.
 :ingroup: group_directive  
    '''
    return lib.vxDirective(reference, directive)
    
def GetStatus(reference):
    '''
Provides a generic API to return status values from Object constructors if they fail.
 :note: Users do not need to strictly check every object creator as the errors should properly propagate and be detected during verification time or run-time.
\code vx_image img = vxCreateImage(context, 639, 480, VX_DF_IMAGE_UYVY); vx_status status = vxGetStatus((vx_reference)img); // status == VX_ERROR_INVALID_DIMENSIONS vxReleaseImage(&img);
\endcode
 :pre: Appropriate Object Creator function.
 :post: Appropriate Object Release function.
 :param reference: [in] The reference to check for construction errors.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No error.
:retval: * Some error occurred, please check enumeration list and constructor.
 :ingroup: group_basic_features  
    '''
    return lib.vxGetStatus(reference)
    
def RegisterUserStruct(context, size):
    '''
* Registers user-defined structures to the context.
 :param context: [in] The reference to the implementation context.
 :param size: [in] The size of user struct in bytes.
:return: A *vx_enum* value that is a type given to the User to refer to their custom structure when declaring a *vx_array* of that structure.
:retval: VX_TYPE_INVALID If the namespace of types has been exhausted.
 :note: This call should only be used once within the lifetime of a context for a specific structure. *  :ingroup: group_adv_array  
    '''
    return lib.vxRegisterUserStruct(context, size)
    
def AllocateUserKernelId(context, pKernelEnumId):
    '''
* Allocates and registers user-defined kernel enumeration to a context. The allocated enumeration is from available pool of 4096 enumerations reserved for dynamic allocation from VX_KERNEL_BASE(VX_ID_USER,0).
 :param context: [in] The reference to the implementation context.
 :param pKernelEnumId: [out] pointer to return *vx_enum* for user-defined kernel.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_NO_RESOURCES The enumerations has been exhausted.
 :ingroup: group_user_kernels  
    '''
    return lib.vxAllocateUserKernelId(context, pKernelEnumId)
    
def AllocateUserKernelLibraryId(context, pLibraryId):
    '''
* Allocates and registers user-defined kernel library ID to a context. * The allocated library ID is from available pool of library IDs (1..255) reserved for dynamic allocation. The returned libraryId can be used by user-kernel library developer to specify individual kernel enum IDs in  a header file, shown below:
\code #define MY_KERNEL_ID1(libraryId) (VX_KERNEL_BASE(VX_ID_USER,libraryId) + 0); #define MY_KERNEL_ID2(libraryId) (VX_KERNEL_BASE(VX_ID_USER,libraryId) + 1); #define MY_KERNEL_ID3(libraryId) (VX_KERNEL_BASE(VX_ID_USER,libraryId) + 2);
\endcode
 :param context: [in] The reference to the implementation context.
 :param pLibraryId: [out] pointer to *vx_enum* for user-kernel libraryId.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_NO_RESOURCES The enumerations has been exhausted.
 :ingroup: group_user_kernels  
    '''
    return lib.vxAllocateUserKernelLibraryId(context, pLibraryId)
    
def SetImmediateModeTarget(context, target_enum, target_string):
    '''
Sets the default target of the immediate mode. Upon successful execution of this function any future execution of immediate mode function is attempted on the new default target of the context.
 :param context: [in] The reference to the implementation context.
 :param target_enum: [in] The default immediate mode target enum to be set to the *vx_context* object. Use a *vx_target_e*.
 :param target_string: [in] The target name ASCII string. This contains a valid value  when target_enum is set to *VX_TARGET_STRING*, otherwise it is ignored.
 :ingroup: group_context
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Default target set.
:retval: VX_ERROR_INVALID_REFERENCE If the context is not a *vx_context*.
:retval: VX_ERROR_NOT_SUPPORTED If the specified target is not supported in this context.  
    '''
    return lib.vxSetImmediateModeTarget(context, target_enum, target_string)
    
def CreateImage(context, width, height, color):
    '''
Creates an opaque reference to an image buffer.
 :details: Not guaranteed to exist until the *vx_graph* containing it has been verified.
 :param context: [in] The reference to the implementation context.
 :param width: [in] The image width in pixels.
 :param height: [in] The image height in pixels.
 :param color: [in] The VX_DF_IMAGE (*vx_df_image_e*) code that represents the format of the image and the color space.
 :returns: An image reference *vx_image*. Any possible errors preventing a successful creation should be checked using *vxGetStatus*.
 :see: vxMapImagePatch to obtain direct memory access to the image data.
 :ingroup: group_image  
    '''
    return lib.vxCreateImage(context, width, height, color)
    
def CreateImageFromROI(img, rect):
    '''
Creates an image from another image given a rectangle. This second reference refers to the data in the original image. Updates to this image updates the parent image. The rectangle must be defined within the pixel space of the parent image.
 :param img: [in] The reference to the parent image.
 :param rect: [in] The region of interest rectangle. Must contain points within the parent image pixel space.
 :returns: An image reference *vx_image* to the sub-image. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*.
 :ingroup: group_image  
    '''
    return lib.vxCreateImageFromROI(img, rect)
    
def CreateUniformImage(context, width, height, color, value):
    '''
Creates a reference to an image object that has a singular, uniform value in all pixels. The uniform image created is read-only. 
 :param context: [in] The reference to the implementation context.
 :param width: [in] The image width in pixels.
 :param height: [in] The image height in pixels.
 :param color: [in] The VX_DF_IMAGE (vx_df_image_e) code that represents the format of the image and the color space.
 :param value: [in] The pointer to the pixel value to which to set all pixels. See *vx_pixel_value_t*.
 :returns: An image reference *vx_image*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*. * :see: vxMapImagePatch* to obtain direct memory access to the image data.
 :note: *vxMapImagePatch* and *vxUnmapImagePatch* may be called with a uniform image reference.
 :ingroup: group_image  
    '''
    return lib.vxCreateUniformImage(context, width, height, color, value)
    
def CreateVirtualImage(graph, width, height, color):
    '''
Creates an opaque reference to an image buffer with no direct user access. This function allows setting the image width, height, or format.
 :details: Virtual data objects allow users to connect various nodes within a graph via data references without access to that data, but they also permit the implementation to take maximum advantage of possible optimizations. Use this API to create a data reference to link two or more nodes together when the intermediate data are not required to be accessed by outside entities. This API in particular allows the user to define the image format of the data without requiring the exact dimensions. Virtual objects are scoped within the graph they are declared a part of, and can't be shared outside of this scope. All of the following constructions of virtual images are valid.
\code vx_context context = vxCreateContext(); vx_graph graph = vxCreateGraph(context); vx_image virt[] = { vxCreateVirtualImage(graph, 0, 0, VX_DF_IMAGE_U8), // no specified dimension vxCreateVirtualImage(graph, 320, 240, VX_DF_IMAGE_VIRT), // no specified format vxCreateVirtualImage(graph, 640, 480, VX_DF_IMAGE_U8), // no user access };
\endcode
 :param graph: [in] The reference to the parent graph.
 :param width: [in] The width of the image in pixels. A value of zero informs the interface that the value is unspecified.
 :param height: [in] The height of the image in pixels. A value of zero informs the interface that the value is unspecified.
 :param color: [in] The VX_DF_IMAGE (*vx_df_image_e*) code that represents the format of the image and the color space. A value of *VX_DF_IMAGE_VIRT* informs the interface that the format is unspecified.
 :returns: An image reference *vx_image*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*.
 :note: Passing this reference to *vxMapImagePatch* will return an error.
 :ingroup: group_image  
    '''
    return lib.vxCreateVirtualImage(graph, width, height, color)
    
def CreateImageFromHandle(context, color, addrs, ptrs, memory_type):
    '''
Creates a reference to an image object that was externally allocated.
 :param context: [in] The reference to the implementation context.
 :param color: [in] See the *vx_df_image_e* codes. This mandates the number of planes needed to be valid in the *addrs* and *ptrs* arrays based on the format given.
 :param addrs[]: [in] The array of image patch addressing structures that define the dimension and stride of the array of pointers. See note below. 
 :param ptrs[]: [in] The array of platform-defined references to each plane. See note below.
 :param memory_type: [in] *vx_memory_type_e*. When giving *VX_MEMORY_TYPE_HOST* the *ptrs* array is assumed to be HOST accessible pointers to memory.
 :returns: An image reference *vx_image*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*.
 :note: The user must call vxMapImagePatch prior to accessing the pixels of an image, even if the  image was created via *vxCreateImageFromHandle*. Reads or writes to memory referenced  by ptrs[ ] after calling *vxCreateImageFromHandle* without first calling  *vxMapImagePatch* will result in undefined behavior. The property of addr[] and ptrs[] arrays is kept by the caller (It means that the implementation will  make an internal copy of the provided information. *addr* and *ptrs* can then simply be application's  local variables). Only *dim_x,* *dim_y,* *stride_x* and *stride_y* fields of the *vx_imagepatch_addressing_t* need to be  provided by the application. Other fields (*step_x,* *step_y,* *scale_x* & *scale_y)* are ignored by this function. The layout of the imported memory must follow a row-major order. In other words, *stride_x* should be  sufficiently large so that there is no overlap between data elements corresponding to different  pixels, and *stride_y* >= *stride_x* * *dim_x.* * In order to release the image back to the application we should use *vxSwapImageHandle*. * Import type of the created image is available via the image attribute *vx_image_attribute_e* parameter.  *  :ingroup: group_image  
    '''
    return lib.vxCreateImageFromHandle(context, color, addrs, ptrs, memory_type)
    
def SwapImageHandle(image, new_ptrs, prev_ptrs, num_planes):
    '''
Swaps the image handle of an image previously created from handle. * This function sets the new image handle (i.e. pointer to all image planes)   and returns the previous one. * Once this function call has completed, the application gets back the ownership of the memory referenced by the previous handle. This memory contains up-to-date pixel data, and the application can safely reuse or  release it. * The memory referenced by the new handle must have been allocated consistently with the image properties since the import type, memory layout and dimensions are unchanged (see addrs, color, and memory_type in *vxCreateImageFromHandle*). * All images created from ROI with this image as parent or ancestor will automatically use the memory referenced by the new handle. * The behavior of *vxSwapImageHandle* when called from a user node is undefined.
 :param image: [in] The reference to an image created from handle
 :param new_ptrs[]: [in] pointer to a caller owned array that contains the new image handle (image plane pointers)
 :arg: new_ptrs is non NULL. new_ptrs[i] must be non NULL for each i such as 0 < i < nbPlanes, otherwise, this is an error. The address of the storage memory for image plane i is set to new_ptrs[i]
 :arg: new_ptrs is NULL: the previous image storage memory is reclaimed by the caller, while no new handle is provided.
 :param prev_ptrs[]: [out] pointer to a caller owned array in which the application returns the previous image handle 
 :arg: prev_ptrs is non NULL. prev_ptrs must have at least as many elements as the number of image planes. For each i such as 0 < i < nbPlanes , prev_ptrs[i] is set to the address of the previous storage memory for plane i.
 :arg: prev_ptrs NULL : the previous handle is not returned.
 :param num_planes: [in] Number of planes in the image. This must be set equal to the number of planes of the input image. The number of elements in new_ptrs and prev_ptrs arrays must be equal to or greater than num_planes.  If either array has more than num_planes elements, the extra elements are ignored. If either array is smaller  than num_planes, the results are undefined. 
:return: A *vx_status_e* enumeration.
:retval: VX_ERROR_INVALID_REFERENCE image is not a valid image reference.
:retval: VX_ERROR_INVALID_PARAMETERS The image was not created from handle or the content of new_ptrs is not valid.
:retval: VX_FAILURE The image was already being accessed.
 :ingroup: group_image  
    '''
    return lib.vxSwapImageHandle(image, new_ptrs, prev_ptrs, num_planes)
    
def QueryImage(image, attribute, ptr, size):
    '''
Retrieves various attributes of an image.
 :param image: [in] The reference to the image to query.
 :param attribute: [in] The attribute to query. Use a *vx_image_attribute_e*.
 :param ptr: [out] The location at which to store the resulting value.
 :param size: [in] The size in bytes of the container to which *ptr* points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If the image is not a *vx_image*.
:retval: VX_ERROR_INVALID_PARAMETERS If any of the other parameters are incorrect.
:retval: VX_ERROR_NOT_SUPPORTED If the attribute is not supported on this implementation.
 :ingroup: group_image  
    '''
    return lib.vxQueryImage(image, attribute, ptr, size)
    
def SetImageAttribute(image, attribute, ptr, size):
    '''
Allows setting attributes on the image.
 :param image: [in] The reference to the image on which to set the attribute.
 :param attribute: [in] The attribute to set. Use a *vx_image_attribute_e* enumeration.
 :param ptr: [in] The pointer to the location from which to read the value.
 :param size: [in] The size in bytes of the object pointed to by *ptr.*
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If the image is not a *vx_image*.
:retval: VX_ERROR_INVALID_PARAMETERS If any of the other parameters are incorrect.
 :ingroup: group_image  
    '''
    return lib.vxSetImageAttribute(image, attribute, ptr, size)
    
def ReleaseImage(image):
    '''
Releases a reference to an image object. The object may not be garbage collected until its total reference count is zero. * An implementation may defer the actual object destruction after its total reference count is zero (potentially until context destruction). Thus, releasing an image created from handle  (see *vxCreateImageFromHandle*) and all others objects that may  reference it (nodes, ROI for instance) are not sufficient to get back the ownership of the memory referenced by the current image handle. The only way for this is to call *vxSwapImageHandle*) before releasing the image. *  :param image: [in] The pointer to the image to release.
 :post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If image is not a *vx_image*.
 :ingroup: group_image  
    '''
    return lib.vxReleaseImage(image)
    
def ComputeImagePatchSize(image, rect, plane_index):
    '''
This computes the size needed to retrieve an image patch from an image.
 :param image: [in] The reference to the image from which to extract the patch.
 :param rect: [in] The coordinates. Must be 0 <= start < end <= dimension where dimension is width for x and height for y.
 :param plane_index: [in] The plane index from which to get the data.
:return: vx_size
 :ingroup: group_image  
    '''
    return lib.vxComputeImagePatchSize(image, rect, plane_index)
    
def FormatImagePatchAddress1d(ptr, index, addr):
    '''
* Accesses a specific indexed pixel in an image patch.
 :param ptr: [in] The base pointer of the patch as returned from *vxMapImagePatch*.
 :param index: [in] The 0 based index of the pixel count in the patch. Indexes increase horizontally by 1 then wrap around to the next row.
 :param addr: [in] The pointer to the addressing mode information returned from *vxMapImagePatch*.
:return: void * Returns the pointer to the specified pixel.
 :pre: *vxMapImagePatch*
 :ingroup: group_image  
    '''
    return lib.vxFormatImagePatchAddress1d(ptr, index, addr)
    
def FormatImagePatchAddress2d(ptr, x, y, addr):
    '''
* Accesses a specific pixel at a 2d coordinate in an image patch.
 :param ptr: [in] The base pointer of the patch as returned from *vxMapImagePatch*.
 :param x: [in] The x dimension within the patch.
 :param y: [in] The y dimension within the patch.
 :param addr: [in] The pointer to the addressing mode information returned from *vxMapImagePatch*.
:return: void * Returns the pointer to the specified pixel.
 :pre: *vxMapImagePatch*
 :ingroup: group_image  
    '''
    return lib.vxFormatImagePatchAddress2d(ptr, x, y, addr)
    
def GetValidRegionImage(image, rect):
    '''
Retrieves the valid region of the image as a rectangle.
 :param image: [in] The image from which to retrieve the valid region.
 :param rect: [out] The destination rectangle.
:return: vx_status
:retval: VX_ERROR_INVALID_REFERENCE Invalid image.
:retval: VX_ERROR_INVALID_PARAMETERS Invalid rect.
:retval: VX_SUCCESS Valid image.
 :note: This rectangle can be passed directly to *vxMapImagePatch* to get the full valid region of the image. 
 :ingroup: group_image  
    '''
    return lib.vxGetValidRegionImage(image, rect)
    
def CopyImagePatch(image, image_rect, image_plane_index, user_addr, user_ptr, usage, user_mem_type):
    '''
Allows the application to copy a rectangular patch from/into an image object plane. *  :param image: [in] The reference to the image object that is the source or the * destination of the copy. *  :param image_rect: [in] The coordinates of the image patch. The patch must be within * the bounds of the image. (start_x, start_y) gives the coordinates of the topleft * pixel inside the patch, while (end_x, end_y) gives the coordinates of the bottomright * element out of the patch. Must be 0 <= start < end <= number of pixels in the image dimension. *  :param image_plane_index: [in] The plane index of the image object that is the source or the * destination of the patch copy. *  :param user_addr: [in] The address of a structure describing the layout of the * user memory location pointed by user_ptr. In the structure, only dim_x, dim_y, * stride_x and stride_y fields must be provided, other fields are ignored by the function. * The layout of the user memory must follow a row major order: * stride_x >= pixel size in bytes, and stride_y >= stride_x * dim_x. *  :param user_ptr: [in] The address of the memory location where to store the requested data * if the copy was requested in read mode, or from where to get the data to store into the image * object if the copy was requested in write mode. The accessible memory must be large enough * to contain the specified patch with the specified layout: * accessible memory in bytes >= (end_y - start_y) * stride_y. *  :param usage: [in] This declares the effect of the copy with regard to the image object * using the *vx_accessor_e* enumeration. For uniform images, only VX_READ_ONLY * is supported. For other images, Only VX_READ_ONLY and VX_WRITE_ONLY are supported: *  :arg: VX_READ_ONLY means that data is copied from the image object into the application memory *  :arg: VX_WRITE_ONLY means that data is copied into the image object from the application memory *  :param user_mem_type: [in] A *vx_memory_type_e* enumeration that specifies * the memory type of the memory referenced by the user_addr. * :return: A *vx_status_e* enumeration. * :retval: VX_ERROR_OPTIMIZED_AWAY This is a reference to a virtual image that cannot be * accessed by the application. * :retval: VX_ERROR_INVALID_REFERENCE The image reference is not actually an image reference. * :retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect. *  :note: The application may ask for data outside the bounds of the valid region, but * such data has an undefined value. *  :ingroup: group_image
    '''
    return lib.vxCopyImagePatch(image, image_rect, image_plane_index, user_addr, user_ptr, usage, user_mem_type)
    
def MapImagePatch(image, rect, plane_index, map_id, addr, ptr, usage, mem_type, flags):
    '''
Allows the application to get direct access to a rectangular patch of an image object plane. *  :param image: [in] The reference to the image object that contains the patch to map. *  :param rect: [in] The coordinates of image patch. The patch must be within the * bounds of the image. (start_x, start_y) gives the coordinate of the topleft * element inside the patch, while (end_x, end_y) give the coordinate of * the bottomright element out of the patch. Must be 0 <= start < end. *  :param plane_index: [in] The plane index of the image object to be accessed. *  :param map_id: [out] The address of a vx_map_id variable where the function * returns a map identifier. *  :arg: (*map_id) must eventually be provided as the map_id parameter of a call to * *vxUnmapImagePatch*. *  :param addr: [out] The address of a structure describing the memory layout of the * image patch to access. The function fills the structure pointed by addr with the * layout information that the application must consult to access the pixel data * at address (*ptr). The layout of the mapped memory follows a row-major order: * stride_x>0, stride_y>0 and stride_y >= stride_x * dim_x. * If the image object being accessed was created via * *vxCreateImageFromHandle*, then the returned memory layout will be * the identical to that of the addressing structure provided when * *vxCreateImageFromHandle* was called. *  :param ptr: [out] The address of a pointer that the function sets to the * address where the requested data can be accessed. This returned (*ptr) address * is only valid between the call to this function and the corresponding call to * *vxUnmapImagePatch*. * If image was created via *vxCreateImageFromHandle* then the returned * address (*ptr) will be the address of the patch in the original pixel buffer * provided when image was created. *  :param usage: [in] This declares the access mode for the image patch, using * the *vx_accessor_e* enumeration. For uniform images, only VX_READ_ONLY * is supported. *  :arg: VX_READ_ONLY: after the function call, the content of the memory location * pointed by (*ptr) contains the image patch data. Writing into this memory location * is forbidden and its behavior is undefined. *  :arg: VX_READ_AND_WRITE : after the function call, the content of the memory * location pointed by (*ptr) contains the image patch data; writing into this memory * is allowed only for the location of pixels only and will result in a modification * of the written pixels in the image object once the patch is unmapped. Writing into * a gap between pixels (when addr->stride_x > pixel size in bytes or addr->stride_y > addr->stride_x*addr->dim_x)  * is forbidden and its behavior is undefined. *  :arg: VX_WRITE_ONLY: after the function call, the memory location pointed by (*ptr) * contains undefined data; writing each pixel of the patch is required prior to * unmapping. Pixels not written by the application before unmap will become * undefined after unmap, even if they were well defined before map. Like for * VX_READ_AND_WRITE, writing into a gap between pixels is forbidden and its behavior * is undefined. *  :param mem_type: [in] A *vx_memory_type_e* enumeration that * specifies the type of the memory where the image patch is requested to be mapped. *  :param flags: [in] An integer that allows passing options to the map operation. * Use the *vx_map_flag_e* enumeration. * :return: A *vx_status_e* enumeration. * :retval: VX_ERROR_OPTIMIZED_AWAY This is a reference to a virtual image that cannot be * accessed by the application. * :retval: VX_ERROR_INVALID_REFERENCE The image reference is not actually an image * reference. * :retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect. *  :note: The user may ask for data outside the bounds of the valid region, but * such data has an undefined value. *  :ingroup: group_image *  :post: *vxUnmapImagePatch * with same (*map_id) value.
    '''
    return lib.vxMapImagePatch(image, rect, plane_index, map_id, addr, ptr, usage, mem_type, flags)
    
def UnmapImagePatch(image, map_id):
    '''
Unmap and commit potential changes to a image object patch that were previously mapped. * Unmapping an image patch invalidates the memory location from which the patch could * be accessed by the application. Accessing this memory location after the unmap function * completes has an undefined behavior. *  :param image: [in] The reference to the image object to unmap. *  :param map_id: [out] The unique map identifier that was returned by *vxMapImagePatch* . * :return: A *vx_status_e* enumeration. * :retval: VX_ERROR_INVALID_REFERENCE The image reference is not actually an image reference. * :retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect. *  :ingroup: group_image *  :pre: *vxMapImagePatch* with same map_id value
    '''
    return lib.vxUnmapImagePatch(image, map_id)
    
def CreateImageFromChannel(img, channel):
    '''
Create a sub-image from a single plane channel of another image. * The sub-image refers to the data in the original image. Updates to this image update the parent image and reversely. * The function supports only channels that occupy an entire plane of a multi-planar images, as listed below. Other cases are not supported. VX_CHANNEL_Y from YUV4, IYUV, NV12, NV21 VX_CHANNEL_U from YUV4, IYUV VX_CHANNEL_V from YUV4, IYUV *  :param img: [in] The reference to the parent image.
 :param channel: [in] The *vx_channel_e* channel to use.
 :returns: An image reference *vx_image* to the sub-image. Any possible errors preventing a successful creation should be checked using *vxGetStatus*.
 :ingroup: group_image  
    '''
    return lib.vxCreateImageFromChannel(img, channel)
    
def SetImageValidRectangle(image, rect):
    '''
Sets the valid rectangle for an image according to a supplied rectangle.
 :note: Setting or changing the valid region from within a user node by means other than the call-back, for  example by calling *vxSetImageValidRectangle*, might result in an incorrect valid region calculation  by the framework.
 :param image: [in] The reference to the image.
 :param rect: [in] The value to be set to the image valid rectangle. A NULL indicates that the valid region is the entire image.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE  The image is not a *vx_image*.
:retval: VX_ERROR_INVALID_PARAMETERS The rect does not define a proper valid rectangle. 
 :ingroup: group_image  
    '''
    return lib.vxSetImageValidRectangle(image, rect)
    
def LoadKernels(context, module):
    '''
Loads one or more kernels into the OpenVX context. This is the interface by which OpenVX is extensible. Once the set of kernels is loaded new kernels and their parameters can be queried.
 :note: When all references to loaded kernels are released, the module may be automatically unloaded.
 :param context: [in] The reference to the implementation context.
 :param module: [in] The short name of the module to load. On systems where there are specific naming conventions for modules, the name passed should ignore such conventions. For example:  :c: libxyz.so should be passed as just  :c: xyz and the implementation will <i>do the right thing</i> that the platform requires.
 :note: This API uses the system pre-defined paths for modules.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If the context is not a *vx_context*.
:retval: VX_ERROR_INVALID_PARAMETERS If any of the other parameters are incorrect.
 :ingroup: group_user_kernels
 :see: vxGetKernelByName  
    '''
    return lib.vxLoadKernels(context, module)
    
def UnloadKernels(context, module):
    '''
Unloads all kernels from the OpenVX context that had been loaded from * the module using the vxLoadKernels function. *  :param context: [in] The reference to the implementation context. *  :param module: [in] The short name of the module to unload. On systems where * there are specific naming conventions for modules, the name passed * should ignore such conventions. For example:  :c: libxyz.so should be * passed as just  :c: xyz and the implementation will <i>do the right thing</i> * that the platform requires. *  :note: This API uses the system pre-defined paths for modules. * :return: A *vx_status_e* enumeration. * :retval: VX_SUCCESS No errors. * :retval: VX_ERROR_INVALID_REFERENCE If the context is not a *\ref vx_context*. * :retval: VX_ERROR_INVALID_PARAMETERS If any of the other parameters are incorrect. *  :ingroup: group_user_kernels *  :see: vxLoadKernels
    '''
    return lib.vxUnloadKernels(context, module)
    
def GetKernelByName(context, name):
    '''
Obtains a reference to a kernel using a string to specify the name.
 :details: User Kernels follow a "dotted" heirarchical syntax. For example: "com.company.example.xyz". The following are strings specifying the kernel names: org.khronos.openvx.color_convert org.khronos.openvx.channel_extract org.khronos.openvx.channel_combine org.khronos.openvx.sobel_3x3 org.khronos.openvx.magnitude org.khronos.openvx.phase org.khronos.openvx.scale_image org.khronos.openvx.table_lookup org.khronos.openvx.histogram org.khronos.openvx.equalize_histogram org.khronos.openvx.absdiff org.khronos.openvx.mean_stddev org.khronos.openvx.threshold org.khronos.openvx.integral_image org.khronos.openvx.dilate_3x3 org.khronos.openvx.erode_3x3 org.khronos.openvx.median_3x3 org.khronos.openvx.box_3x3 org.khronos.openvx.gaussian_3x3 org.khronos.openvx.custom_convolution org.khronos.openvx.gaussian_pyramid org.khronos.openvx.accumulate org.khronos.openvx.accumulate_weighted org.khronos.openvx.accumulate_square org.khronos.openvx.minmaxloc org.khronos.openvx.convertdepth org.khronos.openvx.canny_edge_detector org.khronos.openvx.and org.khronos.openvx.or org.khronos.openvx.xor org.khronos.openvx.not org.khronos.openvx.multiply org.khronos.openvx.add org.khronos.openvx.subtract org.khronos.openvx.warp_affine org.khronos.openvx.warp_perspective org.khronos.openvx.harris_corners org.khronos.openvx.fast_corners org.khronos.openvx.optical_flow_pyr_lk org.khronos.openvx.remap org.khronos.openvx.halfscale_gaussian  org.khronos.openvx.laplacian_pyramid org.khronos.openvx.laplacian_reconstruct org.khronos.openvx.non_linear_filter
 :param context: [in] The reference to the implementation context.
 :param name: [in] The string of the name of the kernel to get.
:return: A kernel reference or zero if an error occurred. Any possible errors  preventing a successful creation should be checked using *vxGetStatus*.
:retval: 0 The kernel name is not found in the context.
 :ingroup: group_kernel
 :pre: *vxLoadKernels* if the kernel is not provided by the OpenVX implementation.
 :note: User Kernels should follow a "dotted" heirarchical syntax. For example: "com.company.example.xyz".  
    '''
    return lib.vxGetKernelByName(context, name)
    
def GetKernelByEnum(context, kernel):
    '''
Obtains a reference to the kernel using the *vx_kernel_e* enumeration.
 :details: Enum values above the standard set are assumed to apply to loaded libraries.
 :param context: [in] The reference to the implementation context.
 :param kernel: [in] A value from *vx_kernel_e* or a vendor or client-defined value.
:return: A *vx_kernel*. Any possible errors  preventing a successful creation should be checked using *vxGetStatus*.
:retval: 0 The kernel enumeration is not found in the context.
 :ingroup: group_kernel
 :pre: *vxLoadKernels* if the kernel is not provided by the OpenVX implementation.  
    '''
    return lib.vxGetKernelByEnum(context, kernel)
    
def QueryKernel(kernel, attribute, ptr, size):
    '''
This allows the client to query the kernel to get information about the number of parameters, enum values, etc.
 :param kernel: [in] The kernel reference to query.
 :param attribute: [in] The attribute to query. Use a *vx_kernel_attribute_e*.
 :param ptr: [out] The pointer to the location at which to store the resulting value.
 :param size: [in] The size of the container to which *ptr* points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If the kernel is not a *vx_kernel*.
:retval: VX_ERROR_INVALID_PARAMETERS If any of the other parameters are incorrect.
:retval: VX_ERROR_NOT_SUPPORTED If the attribute value is not supported in this implementation.
 :ingroup: group_kernel  
    '''
    return lib.vxQueryKernel(kernel, attribute, ptr, size)
    
def ReleaseKernel(kernel):
    '''
Release the reference to the kernel. The object may not be garbage collected until its total reference count is zero.
 :param kernel: [in] The pointer to the kernel reference to release.
 :post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If kernel is not a *vx_kernel*.
 :ingroup: group_kernel  
    '''
    return lib.vxReleaseKernel(kernel)
    
def AddUserKernel(context, name, enumeration, func_ptr, numParams, validate, init, deinit):
    '''
Allows users to add custom kernels to the known kernel database in OpenVX at run-time. This would primarily be used by the module function *vxPublishKernels*.
 :param context: [in] The reference to the implementation context.
 :param name: [in] The string to use to match the kernel.
 :param enumeration: [in] The enumerated value of the kernel to be used by clients.
 :param func_ptr: [in] The process-local function pointer to be invoked.
 :param numParams: [in] The number of parameters for this kernel.
 :param validate: [in] The pointer to *vx_kernel_validate_f*, which validates parameters to this kernel.
 :param init: [in] The kernel initialization function.
 :param deinit: [in] The kernel de-initialization function.
 :ingroup: group_user_kernels
:return: *vx_kernel*. Any possible errors  preventing a successful creation should be checked using *vxGetStatus*.
:retval: 0 Indicates that an error occurred when adding the kernel.
:retval: * Kernel added to OpenVX.  
    '''
    return lib.vxAddUserKernel(context, name, enumeration, func_ptr, numParams, validate, init, deinit)
    
def FinalizeKernel(kernel):
    '''
This API is called after all parameters have been added to the kernel and the kernel is  :e: ready to be used. Notice that the reference to the kernel created  by vxAddUserKernel is still valid after the call to vxFinalizeKernel.
 :param kernel: [in] The reference to the loaded kernel from *vxAddUserKernel*.
:return: A *vx_status_e* enumeration. If an error occurs, the kernel is not available for usage by the clients of OpenVX. Typically this is due to a mismatch between the number of parameters requested and given.
 :pre: *vxAddUserKernel* and *vxAddParameterToKernel*
 :ingroup: group_user_kernels  
    '''
    return lib.vxFinalizeKernel(kernel)
    
def AddParameterToKernel(kernel, index, dir, data_type, state):
    '''
Allows users to set the signatures of the custom kernel.
 :param kernel: [in] The reference to the kernel added with *vxAddUserKernel*.
 :param index: [in] The index of the parameter to add.
 :param dir: [in] The direction of the parameter. This must be either *VX_INPUT* or  *VX_OUTPUT*. *VX_BIDIRECTIONAL* is not supported for this function. 
 :param data_type: [in] The type of parameter. This must be a value from *vx_type_e*.
 :param state: [in] The state of the parameter (required or not). This must be a value from *vx_parameter_state_e*.
:return: A *vx_status_e* enumerated value.
:retval: VX_SUCCESS Parameter is successfully set on kernel.
:retval: VX_ERROR_INVALID_REFERENCE The value passed as kernel was not a  :c: vx_kernel.
 :pre: *vxAddUserKernel*
 :ingroup: group_user_kernels  
    '''
    return lib.vxAddParameterToKernel(kernel, index, dir, data_type, state)
    
def RemoveKernel(kernel):
    '''
Removes a *vx_kernel* from the *vx_context*  and releases it. 
 :param kernel: [in] The reference to the kernel to remove. Returned from *vxAddUserKernel*.
 :note: Any kernel enumerated in the base standard cannot be removed; only kernels added through *vxAddUserKernel* can be removed.
:return: A *vx_status_e* enumeration. The function returns to the  application full control over the memory resources provided at the kernel creation time.
:retval: VX_ERROR_INVALID_REFERENCE If an invalid kernel is passed in.
:retval: VX_ERROR_INVALID_PARAMETER If a base kernel is passed in.
:retval: VX_FAILURE If the application has not released all references to the kernel  object OR if the application has not released all references to a node that is using  this kernel OR if the application has not released all references to a graph which  has nodes that is using this kernel.
 :ingroup: group_user_kernels  
    '''
    return lib.vxRemoveKernel(kernel)
    
def SetKernelAttribute(kernel, attribute, ptr, size):
    '''
Sets kernel attributes.
 :param kernel: [in] The reference to the kernel.
 :param attribute: [in] The enumeration of the attributes. See *vx_kernel_attribute_e*.
 :param ptr: [in] The pointer to the location from which to read the attribute.
 :param size: [in] The size in bytes of the data area indicated by *ptr* in bytes.
 :note: After a kernel has been passed to *vxFinalizeKernel*, no attributes can be altered.
:return: A *vx_status_e* enumeration.
 :ingroup: group_user_kernels  
    '''
    return lib.vxSetKernelAttribute(kernel, attribute, ptr, size)
    
def GetKernelParameterByIndex(kernel, index):
    '''
Retrieves a *vx_parameter* from a *vx_kernel*.
 :param kernel: [in] The reference to the kernel.
 :param index: [in] The index of the parameter.
:return: A *vx_parameter*.Any possible errors  preventing a successful creation should be checked using *vxGetStatus*.
:retval: 0 Either the kernel or index is invalid.
:retval: * The parameter reference.
 :ingroup: group_parameter  
    '''
    return lib.vxGetKernelParameterByIndex(kernel, index)
    
def CreateGraph(context):
    '''
Creates an empty graph.
 :param context: [in] The reference to the implementation context.
 :returns: A graph reference *vx_graph*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*.
 :ingroup: group_graph  
    '''
    return lib.vxCreateGraph(context)
    
def ReleaseGraph(graph):
    '''
Releases a reference to a graph. The object may not be garbage collected until its total reference count is zero. Once the reference count is zero, all node references in the graph are automatically released as well. Data referenced by those nodes may not be released as the user may have external references to the data.
 :param graph: [in] The pointer to the graph to release.
 :post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If graph is not a *vx_graph*.
 :ingroup: group_graph  
    '''
    return lib.vxReleaseGraph(graph)
    
def VerifyGraph(graph):
    '''
Verifies the state of the graph before it is executed. This is useful to catch programmer errors and contract errors. If not verified, the graph verifies before being processed.
 :pre: Memory for data objects is not guarenteed to exist before this call.  :post: After this call data objects exist unless the implementation optimized them out.
 :param graph: [in] The reference to the graph to verify.
:return: A status code for graphs with more than one error; it is undefined which error will be returned. Register a log callback using *vxRegisterLogCallback* to receive each specific error in the graph.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If graph is not a *vx_graph*.
:retval: VX_ERROR_MULTIPLE_WRITERS If the graph contains more than one writer to any data object.
:retval: VX_ERROR_INVALID_NODE If a node in the graph is invalid or failed be created.
:retval: VX_ERROR_INVALID_GRAPH If the graph contains cycles or some other invalid topology.
:retval: VX_ERROR_INVALID_TYPE If any parameter on a node is given the wrong type.
:retval: VX_ERROR_INVALID_VALUE If any value of any parameter is out of bounds of specification.
:retval: VX_ERROR_INVALID_FORMAT If the image format is not compatible.
 :ingroup: group_graph
 :see: vxProcessGraph  
    '''
    return lib.vxVerifyGraph(graph)
    
def ProcessGraph(graph):
    '''
This function causes the synchronous processing of a graph. If the graph has not been verified, then the implementation verifies the graph immediately. If verification fails this function returns a status identical to what *vxVerifyGraph* would return. After the graph verfies successfully then processing occurs. If the graph was previously verified via *vxVerifyGraph* or *vxProcessGraph* then the graph is processed. This function blocks until the graph is completed.
 :param graph: [in] The graph to execute.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Graph has been processed.
:retval: VX_FAILURE A catastrophic error occurred during processing.
:retval: * See *vxVerifyGraph*.
 :pre: *vxVerifyGraph* must return *VX_SUCCESS* before this function will pass.
 :ingroup: group_graph
 :see: vxVerifyGraph  
    '''
    return lib.vxProcessGraph(graph)
    
def ScheduleGraph(graph):
    '''
Schedules a graph for future execution.
 :param graph: [in] The graph to schedule.
:return: A *vx_status_e* enumeration.
:retval: VX_ERROR_NO_RESOURCES The graph cannot be scheduled now.
:retval: VX_ERROR_NOT_SUFFICIENT The graph is not verified and has failed forced verification.
:retval: VX_SUCCESS The graph has been scheduled.
 :pre: *vxVerifyGraph* must return *VX_SUCCESS* before this function will pass.
 :ingroup: group_graph  
    '''
    return lib.vxScheduleGraph(graph)
    
def WaitGraph(graph):
    '''
Waits for a specific graph to complete. If the graph has been scheduled multiple  times since the last call to vxWaitGraph, then vxWaitGraph returns only when the last  scheduled execution completes.
 :param graph: [in] The graph to wait on.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS The graph has successfully completed execution and its outputs are the  valid results of the most recent execution. 
:retval: VX_FAILURE An error occurred or the graph was never scheduled. Output data of the  graph is undefined. 
 :pre: *vxScheduleGraph*
 :ingroup: group_graph  
    '''
    return lib.vxWaitGraph(graph)
    
def QueryGraph(graph, attribute, ptr, size):
    '''
Allows the user to query attributes of the Graph.
 :param graph: [in] The reference to the created graph.
 :param attribute: [in] The *vx_graph_attribute_e* type needed.
 :param ptr: [out] The location at which to store the resulting value.
 :param size: [in] The size in bytes of the container to which *ptr* points.
:return: A *vx_status_e* enumeration.
 :ingroup: group_graph  
    '''
    return lib.vxQueryGraph(graph, attribute, ptr, size)
    
def SetGraphAttribute(graph, attribute, ptr, size):
    '''
Allows the attributes of the Graph to be set to the provided value.
 :param graph: [in] The reference to the graph.
 :param attribute: [in] The *vx_graph_attribute_e* type needed.
 :param ptr: [in] The location from which to read the value.
 :param size: [in] The size in bytes of the container to which *ptr* points.
:return: A *vx_status_e* enumeration.
 :ingroup: group_graph  
    '''
    return lib.vxSetGraphAttribute(graph, attribute, ptr, size)
    
def AddParameterToGraph(graph, parameter):
    '''
Adds the given parameter extracted from a *vx_node* to the graph.
 :param graph: [in] The graph reference that contains the node.
 :param parameter: [in] The parameter reference to add to the graph from the node.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Parameter added to Graph.
:retval: VX_ERROR_INVALID_REFERENCE The parameter is not a valid *vx_parameter*.
:retval: VX_ERROR_INVALID_PARAMETER The parameter is of a node not in this graph.
 :ingroup: group_graph_parameters  
    '''
    return lib.vxAddParameterToGraph(graph, parameter)
    
def SetGraphParameterByIndex(graph, index, value):
    '''
Sets a reference to the parameter on the graph. The implementation must set this parameter on the originating node as well.
 :param graph: [in] The graph reference.
 :param index: [in] The parameter index.
 :param value: [in] The reference to set to the parameter.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Parameter set to Graph.
:retval: VX_ERROR_INVALID_REFERENCE The value is not a valid *vx_reference*.
:retval: VX_ERROR_INVALID_PARAMETER The parameter index is out of bounds or the dir parameter is incorrect.
 :ingroup: group_graph_parameters  
    '''
    return lib.vxSetGraphParameterByIndex(graph, index, value)
    
def GetGraphParameterByIndex(graph, index):
    '''
Retrieves a *vx_parameter* from a *vx_graph*.
 :param graph: [in] The graph.
 :param index: [in] The index of the parameter.
:return: *vx_parameter* reference. Any possible errors  preventing a successful creation should be checked using *vxGetStatus*.
:retval: 0 if the index is out of bounds.
:retval: * The parameter reference.
 :ingroup: group_graph_parameters  
    '''
    return lib.vxGetGraphParameterByIndex(graph, index)
    
def IsGraphVerified(graph):
    '''
Returns a Boolean to indicate the state of graph verification.
 :param graph: [in] The reference to the graph to check.
:return: A *vx_bool* value.
:retval: vx_true_e The graph is verified.
:retval: vx_false_e The graph is not verified. It must be verified before execution either through *vxVerifyGraph* or automatically through *vxProcessGraph* or *vxScheduleGraph*.
 :ingroup: group_graph  
    '''
    return lib.vxIsGraphVerified(graph)
    
def CreateGenericNode(graph, kernel):
    '''
Creates a reference to a node object for a given kernel.
 :details: This node has no references assigned as parameters after completion. The client is then required to set these parameters manually by *vxSetParameterByIndex*. When clients supply their own node creation functions (for use with User Kernels), this is the API to use along with the parameter setting API.
 :param graph: [in] The reference to the graph in which this node exists.
 :param kernel: [in] The kernel reference to associate with this new node.
 :returns: A node reference *vx_node*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*.
 :note: A call to this API sets all parameters to NULL. 
 :ingroup: group_adv_node
 :post: Call *vxSetParameterByIndex* for as many parameters as needed to be set.  
    '''
    return lib.vxCreateGenericNode(graph, kernel)
    
def QueryNode(node, attribute, ptr, size):
    '''
Allows a user to query information out of a node.
 :param node: [in] The reference to the node to query.
 :param attribute: [in] Use *vx_node_attribute_e* value to query for information.
 :param ptr: [out] The location at which to store the resulting value.
 :param size: [in] The size in bytesin bytes of the container to which *ptr* points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Successful
:retval: VX_ERROR_INVALID_PARAMETERS The type or size is incorrect.
 :ingroup: group_node  
    '''
    return lib.vxQueryNode(node, attribute, ptr, size)
    
def SetNodeAttribute(node, attribute, ptr, size):
    '''
Allows a user to set attribute of a node before Graph Validation.
 :param node: [in] The reference to the node to set.
 :param attribute: [in] Use *vx_node_attribute_e* value to set the desired attribute.
 :param ptr: [in] The pointer to the desired value of the attribute.
 :param size: [in] The size in bytes of the objects to which *ptr* points.
 :note: Some attributes are inherited from the *vx_kernel*, which was used to create the node. Some of these can be overridden using this API, notably
VX_NODE_LOCAL_DATA_SIZE and VX_NODE_LOCAL_DATA_PTR.
 :ingroup: group_node
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS The attribute was set.
:retval: VX_ERROR_INVALID_REFERENCE node is not a vx_node.
:retval: VX_ERROR_INVALID_PARAMETER size is not correct for the type needed.  
    '''
    return lib.vxSetNodeAttribute(node, attribute, ptr, size)
    
def ReleaseNode(node):
    '''
Releases a reference to a Node object. The object may not be garbage collected until its total reference count is zero.
 :param node: [in] The pointer to the reference of the node to release.
 :ingroup: group_node
 :post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If node is not a *vx_node*.  
    '''
    return lib.vxReleaseNode(node)
    
def RemoveNode(node):
    '''
Removes a Node from its parent Graph and releases it.
 :param node: [in] The pointer to the node to remove and release.
 :ingroup: group_node
 :post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If node is not a *vx_node*.  
    '''
    return lib.vxRemoveNode(node)
    
def AssignNodeCallback(node, callback):
    '''
Assigns a callback to a node. If a callback already exists in this node, this function must return an error and the user may clear the callback by passing a NULL pointer as the callback.
 :param node: [in] The reference to the node.
 :param callback: [in] The callback to associate with completion of this specific node.
 :warning: This must be used with <b><i>extreme</i></b> caution as it can \e ruin optimizations in the power/performance efficiency of a graph.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Callback assigned.
:retval: VX_ERROR_INVALID_REFERENCE The value passed as node was not a *vx_node*.
 :ingroup: group_node_callback  
    '''
    return lib.vxAssignNodeCallback(node, callback)
    
def RetrieveNodeCallback(node):
    '''
Retrieves the current node callback function pointer set on the node.
 :param node: [in] The reference to the *vx_node* object.
 :ingroup: group_node_callback
:return: vx_nodecomplete_f The pointer to the callback function.
:retval: NULL No callback is set.
:retval: * The node callback function.  
    '''
    return lib.vxRetrieveNodeCallback(node)
    
def SetNodeTarget(node, target_enum, target_string):
    '''
Sets the node target to the provided value. A success invalidates the graph  that the node belongs to (*vxVerifyGraph* must be called before the next execution)
 :param node: [in] The reference to the *vx_node* object.
 :param target_enum: [in] The target enum to be set to the *vx_node* object. Use a *vx_target_e*.
 :param target_string: [in] The target name ASCII string. This contains a valid value  when target_enum is set to *VX_TARGET_STRING*, otherwise it is ignored.
 :ingroup: group_node
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Node target set.
:retval: VX_ERROR_INVALID_REFERENCE If node is not a *vx_node*.
:retval: VX_ERROR_NOT_SUPPORTED If the node kernel is not supported by the specified target.  
    '''
    return lib.vxSetNodeTarget(node, target_enum, target_string)
    
def ReplicateNode(graph, first_node, replicate, number_of_parameters):
    '''
Creates replicas of the same node first_node to process a set of objects stored in *vx_pyramid* or *vx_object_array*. first_node needs to have as parameter levels 0 of a *vx_pyramid* or the index 0 of a *vx_object_array*.  Replica nodes are not accessible by the application through any means. An application request for removal of  first_node from the graph will result in removal of all replicas. Any change of parameter or attribute of  first_node will be propagated to the replicas. *vxVerifyGraph* shall enforce consistency of parameters and attributes  in the replicas.
 :param graph: [in] The reference to the graph. 
 :param first_node: [in] The reference to the node in the graph that will be replicated.
 :param replicate: [in] an array of size equal to the number of node parameters, vx_true_e for the parameters  that should be iterated over (should be a reference to a vx_pyramid or a vx_object_array),  vx_false_e for the parameters that should be the same across replicated nodes and for optional  parameters that are not used. Should be vx_true_e for all output and bidirectional parameters.
 :param number_of_parameters: [in] number of elements in the replicate array
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If the first_node is not a *vx_node*, or it is not the first child of a vx_pyramid.
:retval: VX_ERROR_NOT_COMPATIBLE At least one of replicated parameters is not of level 0 of a pyramid or at index 0 of an object array.
:retval: VX_FAILURE If the node does not belong to the graph, or the number of objects in the parent objects of inputs and output are not the same.
 :ingroup: group_node  
    '''
    return lib.vxReplicateNode(graph, first_node, replicate, number_of_parameters)
    
def GetParameterByIndex(node, index):
    '''
Retrieves a *vx_parameter* from a *vx_node*.
 :param node: [in] The node from which to extract the parameter.
 :param index: [in] The index of the parameter to which to get a reference.
:return: *vx_parameter*. Any possible errors  preventing a successful creation should be checked using *vxGetStatus*.
 :ingroup: group_parameter  
    '''
    return lib.vxGetParameterByIndex(node, index)
    
def ReleaseParameter(param):
    '''
Releases a reference to a parameter object. The object may not be garbage collected until its total reference count is zero.
 :param param: [in] The pointer to the parameter to release.
 :ingroup: group_parameter
 :post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If param is not a *vx_parameter*.  
    '''
    return lib.vxReleaseParameter(param)
    
def SetParameterByIndex(node, index, value):
    '''
Sets the specified parameter data for a kernel on the node.
 :param node: [in] The node that contains the kernel.
 :param index: [in] The index of the parameter desired.
 :param value: [in] The desired value of the parameter.
 :note: A user may not provide a NULL value for a mandatory parameter of this API.
:return: A *vx_status_e* enumeration.
 :ingroup: group_parameter
 :see: vxSetParameterByReference  
    '''
    return lib.vxSetParameterByIndex(node, index, value)
    
def SetParameterByReference(parameter, value):
    '''
Associates a parameter reference and a data reference with a kernel on a node.
 :param parameter: [in] The reference to the kernel parameter.
 :param value: [in] The value to associate with the kernel parameter.
 :note: A user may not provide a NULL value for a mandatory parameter of this API.
:return: A *vx_status_e* enumeration.
 :ingroup: group_parameter
 :see: vxGetParameterByIndex  
    '''
    return lib.vxSetParameterByReference(parameter, value)
    
def QueryParameter(param, attribute, ptr, size):
    '''
Allows the client to query a parameter to determine its meta-information.
 :param param: [in] The reference to the parameter.
 :param attribute: [in] The attribute to query. Use a *vx_parameter_attribute_e*.
 :param ptr: [out] The location at which to store the resulting value.
 :param size: [in] The size in bytes of the container to which *ptr* points.
:return: A *vx_status_e* enumeration.
 :ingroup: group_parameter  
    '''
    return lib.vxQueryParameter(param, attribute, ptr, size)
    
def CreateScalar(context, data_type, ptr):
    '''
Creates a reference to a scalar object. Also see sub_node_parameters.
 :param context: [in] The reference to the system context.
 :param data_type: [in] The *vx_type_e* of the scalar. Must be greater than *VX_TYPE_INVALID* and less than *VX_TYPE_SCALAR_MAX*.
 :param ptr: [in] The pointer to the initial value of the scalar.
 :ingroup: group_scalar
 :returns: A scaler reference *vx_scalar*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*.  
    '''
    return lib.vxCreateScalar(context, data_type, ptr)
    
def ReleaseScalar(scalar):
    '''
Releases a reference to a scalar object. The object may not be garbage collected until its total reference count is zero.
 :param scalar: [in] The pointer to the scalar to release.
 :ingroup: group_scalar
 :post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If scalar is not a *vx_scalar*.  
    '''
    return lib.vxReleaseScalar(scalar)
    
def QueryScalar(scalar, attribute, ptr, size):
    '''
Queries attributes from a scalar.
 :param scalar: [in] The scalar object.
 :param attribute: [in] The enumeration to query. Use a *vx_scalar_attribute_e* enumeration.
 :param ptr: [out] The location at which to store the resulting value.
 :param size: [in] The size of the container to which *ptr* points.
:return: A *vx_status_e* enumeration.
 :ingroup: group_scalar  
    '''
    return lib.vxQueryScalar(scalar, attribute, ptr, size)
    
def CopyScalar(scalar, user_ptr, usage, user_mem_type):
    '''
Allows the application to copy from/into a scalar object.
 :param scalar: [in] The reference to the scalar object that is the source or the destination of the copy.
 :param user_ptr: [in] The address of the memory location where to store the requested data if the copy was requested in read mode, or from where to get the data to store into the scalar object if the copy was requested in write mode. In the user memory, the scalar is a variable of the type corresponding to *VX_SCALAR_TYPE*. The accessible memory must be large enough to contain this variable.
 :param usage: [in] This declares the effect of the copy with regard to the scalar object using the *vx_accessor_e* enumeration. Only VX_READ_ONLY and VX_WRITE_ONLY are supported:
 :arg: VX_READ_ONLY means that data are copied from the scalar object into the user memory.
 :arg: VX_WRITE_ONLY means that data are copied into the scalar object from the user memory.
 :param user_mem_type: [in] A *vx_memory_type_e* enumeration that specifies the memory type of the memory referenced by the user_addr.
:return: A *vx_status_e* enumeration.
:retval: VX_ERROR_INVALID_REFERENCE The scalar reference is not actually a scalar reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
 :ingroup: group_scalar  
    '''
    return lib.vxCopyScalar(scalar, user_ptr, usage, user_mem_type)
    
def QueryReference(ref, attribute, ptr, size):
    '''
Queries any reference type for some basic information like count or type.
 :param ref: [in] The reference to query.
 :param attribute: [in] The value for which to query. Use *vx_reference_attribute_e*.
 :param ptr: [out] The location at which to store the resulting value.
 :param size: [in] The size in bytes of the container to which ptr points.
:return: A *vx_status_e* enumeration.
 :ingroup: group_reference  
    '''
    return lib.vxQueryReference(ref, attribute, ptr, size)
    
def ReleaseReference(ref_ptr):
    '''
Releases a reference. The reference may potentially refer to multiple OpenVX objects of different types. This function can be used instead of calling a specific release function for each individual object type  (e.g. vxRelease<object>). The object will not be destroyed until its total reference count is zero.
 :note: After returning from this function the reference is zeroed.
 :param ref_ptr: [in] The pointer to the reference of the object to release.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If the reference is not valid.
 :ingroup: group_reference  
    '''
    return lib.vxReleaseReference(ref_ptr)
    
def RetainReference(ref):
    '''
* Increments the reference counter of an object This function is used to express the fact that the OpenVX object is referenced multiple times by an application. Each time this function is called for an object, the application will need to release the object one additional time before it can be destructed
 :param ref: [in] The reference to retain.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE if reference is not valid.
 :ingroup: group_reference  
    '''
    return lib.vxRetainReference(ref)
    
def SetReferenceName(ref, name):
    '''
Name a reference
 :ingroup: group_reference * This function is used to associate a name to a referenced object. This name can be used by the OpenVX implementation in log messages and any other reporting mechanisms.   * The OpenVX implementation will not check if the name is unique in the reference scope (context or graph). Several references can then have the same name. *  :param ref: [in] The reference to the object to be named.
 :param name: [in] Pointer to the ' :0': terminated string that identifies the referenced object. The string is copied by the function so that it stays the property of the caller. NULL means that the reference is not named. The length of the string shall be lower than VX_MAX_REFERENCE_NAME bytes.
:return: A vx_status_e enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If reference is not valid.  
    '''
    return lib.vxSetReferenceName(ref, name)
    
def QueryDelay(delay, attribute, ptr, size):
    '''
Queries a *vx_delay* object attribute.
 :param delay: [in] A pointer to a delay object.
 :param attribute: [in] The attribute to query. Use a *vx_delay_attribute_e* enumeration.
 :param ptr: [out] The location at which to store the resulting value.
 :param size: [in] The size of the container to which *ptr* points.
:return: A *vx_status_e* enumeration.
 :ingroup: group_delay  
    '''
    return lib.vxQueryDelay(delay, attribute, ptr, size)
    
def ReleaseDelay(delay):
    '''
Releases a reference to a delay object. The object may not be garbage collected until its total reference count is zero.
 :param delay: [in] The pointer to the delay to release.
 :post: After returning from this function the reference is zeroed.
 :ingroup: group_delay
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If delay is not a *vx_delay*.  
    '''
    return lib.vxReleaseDelay(delay)
    
def CreateDelay(context, exemplar, slots):
    '''
Creates a Delay object.
 :details: This function uses a subset of the attributes defining the metadata of  the exemplar, ignoring the object. It does not alter the exemplar or keep or release  the reference to the exemplar. For the definition of supported attributes see vxSetMetaFormatAttribute. *  :param context: [in] The reference to the system context.
 :param exemplar: [in] The exemplar object.
 :param slots: [in] The number of reference in the delay.
 :returns: A delay reference *vx_delay*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*.
 :ingroup: group_delay  
    '''
    return lib.vxCreateDelay(context, exemplar, slots)
    
def GetReferenceFromDelay(delay, index):
    '''
Retrieves a reference from a delay object.
 :param delay: [in] The reference to the delay object.
 :param index: [in] An index into the delay from which to extract the reference.
:return: *vx_reference*. Any possible errors  preventing a successful creation should be checked using *vxGetStatus*.
 :note: The delay index is in the range \f$ [-count+1,0] \f$. 0 is always the
 :e: current object.
 :ingroup: group_delay
 :note: A reference from a delay object must not be given to its associated release API (e.g. *vxReleaseImage*) unless *vxRetainReference* is used.   
    '''
    return lib.vxGetReferenceFromDelay(delay, index)
    
def AgeDelay(delay):
    '''
Ages the internal delay ring by one. This means that once this API is called the reference from index 0 will go to index -1 and so forth until
 :f$: -count+1 \f$ is reached. This last object will become 0. Once the delay has been aged, it updates the reference in any associated nodes. Here  :f$: count \f$ is the number of slots in delay ring.
 :param: [in] delay
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Delay was aged.
:retval: VX_ERROR_INVALID_REFERENCE The value passed as delay was not a *vx_delay*.
 :ingroup: group_delay  
    '''
    return lib.vxAgeDelay(delay)
    
def RegisterAutoAging(graph, delay):
    '''
Register a delay for auto-aging. * This function registers a delay object to be auto-aged by the graph. This delay object will be automatically aged after each successful completion of this graph. Aging of a delay object cannot be called during graph execution.  A graph abandoned due to a node callback will trigger an auto-aging. * If a delay is registered for auto-aging multiple times in a same graph, the delay will be only aged a single time at each graph completion. If a delay is registered for auto-aging in multiple graphs, this delay will aged automatically after each successful completion of any of these graphs. *  :param graph: [in] The graph to which the delay is registered for auto-aging.
 :param delay: [in] The delay to automatically age. * :return: A vx_status_e enumeration.
:retval: VX_SUCCESS                   No errors.
:retval: VX_ERROR_INVALID_REFERENCE   If the  :p: graph or \p delay is not a valid reference
 :ingroup: group_graph  
    '''
    return lib.vxRegisterAutoAging(graph, delay)
    
def AddLogEntry(ref, status, message):
    '''
Adds a line to the log.
 :param ref: [in] The reference to add the log entry against. Some valid value must be provided.
 :param status: [in] The status code. *VX_SUCCESS* status entries are ignored and not added.
 :param message: [in] The human readable message to add to the log.
 :param ...: [in] a list of variable arguments to the message.
 :note: Messages may not exceed *VX_MAX_LOG_MESSAGE_LEN* bytes and will be truncated in the log if they exceed this limit.
 :ingroup: group_log  
    '''
    return lib.vxAddLogEntry(ref, status, message)
    
def RegisterLogCallback(context, callback, reentrant):
    '''
Registers a callback facility to the OpenVX implementation to receive error logs.
 :param context: [in] The overall context to OpenVX.
 :param callback: [in] The callback function. If NULL, the previous callback is removed.
 :param reentrant: [in] If reentrancy flag is *vx_true_e*, then the callback may be entered from multiple simultaneous tasks or threads (if the host OS supports this).
 :ingroup: group_log  
    '''
    return lib.vxRegisterLogCallback(context, callback, reentrant)
    
def CreateLUT(context, data_type, count):
    '''
Creates LUT object of a given type. The value of *VX_LUT_OFFSET* is equal to 0  for data_type = *VX_TYPE_UINT8*, and (vx_uint32)(count/2) for *VX_TYPE_INT16*.
 :param context: [in] The reference to the context.
 :param data_type: [in] The type of data stored in the LUT.
 :param count: [in] The number of entries desired.
 :if: OPENVX_STRICT_1_0
 :note: For OpenVX 1.0, data_type can only be VX_TYPE_UINT8 or VX_TYPE_INT16. If data_type  is VX_TYPE_UINT8, count should be not greater than 256. If data_type is VX_TYPE_INT16,  count should not be greater than 65536.
\endif
 :returns: An LUT reference *vx_lut*. Any possible errors preventing a successful creation should be checked using *vxGetStatus*.
 :ingroup: group_lut  
    '''
    return lib.vxCreateLUT(context, data_type, count)
    
def ReleaseLUT(lut):
    '''
Releases a reference to a LUT object. The object may not be garbage collected until its total reference count is zero.
 :param lut: [in] The pointer to the LUT to release.
 :post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If lut is not a *vx_lut*.
 :ingroup: group_lut  
    '''
    return lib.vxReleaseLUT(lut)
    
def QueryLUT(lut, attribute, ptr, size):
    '''
Queries attributes from a LUT.
 :param lut: [in] The LUT to query.
 :param attribute: [in] The attribute to query. Use a *vx_lut_attribute_e* enumeration.
 :param ptr: [out] The location at which to store the resulting value.
 :param size: [in] The size in bytes of the container to which *ptr* points.
:return: A *vx_status_e* enumeration.
 :ingroup: group_lut  
    '''
    return lib.vxQueryLUT(lut, attribute, ptr, size)
    
def CopyLUT(lut, user_ptr, usage, user_mem_type):
    '''
Allows the application to copy from/into a LUT object.
 :param lut: [in] The reference to the LUT object that is the source or the destination of the copy.
 :param user_ptr: [in] The address of the memory location where to store the requested data if the copy was requested in read mode, or from where to get the data to store into the LUT object if the copy was requested in write mode. In the user memory, the LUT is represented as a array with elements of the type corresponding to *VX_LUT_TYPE*, and with a number of elements equal to the value returned via *VX_LUT_COUNT*. The accessible memory must be large enough to contain this array: accessible memory in bytes >= sizeof(data_element) * count.
 :param usage: [in] This declares the effect of the copy with regard to the LUT object using the *vx_accessor_e* enumeration. Only VX_READ_ONLY and VX_WRITE_ONLY are supported:
 :arg: VX_READ_ONLY means that data are copied from the LUT object into the user memory.
 :arg: VX_WRITE_ONLY means that data are copied into the LUT object from the user memory.
 :param user_mem_type: [in] A *vx_memory_type_e* enumeration that specifies the memory type of the memory referenced by the user_addr.
:return: A *vx_status_e* enumeration.
:retval: VX_ERROR_INVALID_REFERENCE The LUT reference is not actually a LUT reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
 :ingroup: group_lut  
    '''
    return lib.vxCopyLUT(lut, user_ptr, usage, user_mem_type)
    
def MapLUT(lut, map_id, ptr, usage, mem_type, flags):
    '''
Allows the application to get direct access to LUT object.
 :param lut: [in] The reference to the LUT object to map.
 :param map_id: [out] The address of a vx_map_id variable where the function returns a map identifier.
 :arg: (*map_id) must eventually be provided as the map_id parameter of a call to *vxUnmapLUT*.
 :param ptr: [out] The address of a pointer that the function sets to the address where the requested data can be accessed. In the mapped memory area, the LUT data are structured as an array with elements of the type corresponding to *VX_LUT_TYPE*, with a number of elements equal to the value returned via *VX_LUT_COUNT*. Accessing the memory out of the bound of this array is forbidden and has an undefined behavior. The returned (*ptr) address is only valid between the call to the function and the corresponding call to *vxUnmapLUT*.
 :param usage: [in] This declares the access mode for the LUT, using the *vx_accessor_e* enumeration.
 :arg: VX_READ_ONLY: after the function call, the content of the memory location pointed by (*ptr) contains the LUT data. Writing into this memory location is forbidden and its behavior is undefined.
 :arg: VX_READ_AND_WRITE : after the function call, the content of the memory location pointed by (*ptr) contains the LUT data; writing into this memory is allowed only for the location of entries and will result in a modification of the affected entries in the LUT object once the LUT is unmapped.
 :arg: VX_WRITE_ONLY: after the function call, the memory location pointed by(*ptr) contains undefined data; writing each entry of LUT is required prior to unmapping. Entries not written by the application before unmap will become undefined after unmap, even if they were well defined before map.
 :param mem_type: [in] A *vx_memory_type_e* enumeration that specifies the type of the memory where the LUT is requested to be mapped.
 :param flags: [in] An integer that allows passing options to the map operation. Use 0 for this option.
:return: A *vx_status_e* enumeration.
:retval: VX_ERROR_INVALID_REFERENCE The LUT reference is not actually a LUT reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
 :ingroup: group_lut
 :post: *vxUnmapLUT * with same (*map_id) value.  
    '''
    return lib.vxMapLUT(lut, map_id, ptr, usage, mem_type, flags)
    
def UnmapLUT(lut, map_id):
    '''
Unmap and commit potential changes to LUT object that was previously mapped. Unmapping a LUT invalidates the memory location from which the LUT data could be accessed by the application. Accessing this memory location after the unmap function completes has an undefined behavior.
 :param lut: [in] The reference to the LUT object to unmap.
 :param map_id: [out] The unique map identifier that was returned when calling *vxMapLUT* .
:return: A *vx_status_e* enumeration.
:retval: VX_ERROR_INVALID_REFERENCE The LUT reference is not actually a LUT reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
 :ingroup: group_lut
 :pre: *vxMapLUT* returning the same map_id value  
    '''
    return lib.vxUnmapLUT(lut, map_id)
    
def CreateDistribution(context, numBins, offset, range):
    '''
Creates a reference to a 1D Distribution of a consecutive interval [offset, offset + range - 1]  defined by a start offset and valid range, divided equally into numBins parts.
 :param context: [in] The reference to the overall context.
 :param numBins: [in] The number of bins in the distribution.
 :param offset: [in] The start offset into the range value that marks the begining of the 1D Distribution.
 :param range: [in] The total number of the consecutive values of the distribution interval. 
 :returns: A distribution reference *vx_distribution*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*.
 :ingroup: group_distribution  
    '''
    return lib.vxCreateDistribution(context, numBins, offset, range)
    
def ReleaseDistribution(distribution):
    '''
Releases a reference to a distribution object. The object may not be garbage collected until its total reference count is zero.
 :param distribution: [in] The reference to the distribution to release.
 :post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If distribution is not a *vx_distribution*.
 :ingroup: group_distribution  
    '''
    return lib.vxReleaseDistribution(distribution)
    
def QueryDistribution(distribution, attribute, ptr, size):
    '''
Queries a Distribution object.
 :param distribution: [in] The reference to the distribution to query.
 :param attribute: [in] The attribute to query. Use a *vx_distribution_attribute_e* enumeration.
 :param ptr: [out] The location at which to store the resulting value.
 :param size: [in] The size in bytes of the container to which *ptr* points.
:return: A *vx_status_e* enumeration.
 :ingroup: group_distribution  
    '''
    return lib.vxQueryDistribution(distribution, attribute, ptr, size)
    
def CopyDistribution(distribution, user_ptr, usage, user_mem_type):
    '''
Allows the application to copy from/into a distribution object. *  :param distribution: [in] The reference to the distribution object that is the source or the * destination of the copy. *  :param user_ptr: [in] The address of the memory location where to store the requested data * if the copy was requested in read mode, or from where to get the data to store into the distribution * object if the copy was requested in write mode. In the user memory, the distribution is * represented as a *vx_uint32* array with a number of elements equal to the value returned via * *VX_DISTRIBUTION_BINS*. The accessible memory must be large enough * to contain this vx_uint32 array: * accessible memory in bytes >= sizeof(vx_uint32) * num_bins. *  :param usage: [in] This declares the effect of the copy with regard to the distribution object * using the *vx_accessor_e* enumeration. Only VX_READ_ONLY and VX_WRITE_ONLY * are supported: *  :arg: VX_READ_ONLY means that data are copied from the distribution object into the user memory. *  :arg: VX_WRITE_ONLY means that data are copied into the distribution object from the user memory. *  :param user_mem_type: [in] A *vx_memory_type_e* enumeration that specifies * the memory type of the memory referenced by the user_addr. * :return: A *vx_status_e* enumeration. * :retval: VX_ERROR_INVALID_REFERENCE The distribution reference is not actually a distribution reference. * :retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect. *  :ingroup: group_distribution
    '''
    return lib.vxCopyDistribution(distribution, user_ptr, usage, user_mem_type)
    
def MapDistribution(distribution, map_id, ptr, usage, mem_type, flags):
    '''
Allows the application to get direct access to distribution object. *  :param distribution: [in] The reference to the distribution object to map. *  :param map_id: [out] The address of a vx_map_id variable where the function * returns a map identifier. *  :arg: (*map_id) must eventually be provided as the map_id parameter of a call to * *vxUnmapDistribution*. *  :param ptr: [out] The address of a pointer that the function sets to the * address where the requested data can be accessed. In the mapped memory area, * data are structured as a vx_uint32 array with a number of elements equal to * the value returned via *VX_DISTRIBUTION_BINS*. Each * element of this array corresponds to a bin of the distribution, with a range-major * ordering. Accessing the memory out of the bound of this array * is forbidden and has an undefined behavior. The returned (*ptr) address * is only valid between the call to the function and the corresponding call to * *vxUnmapDistribution*. *  :param usage: [in] This declares the access mode for the distribution, using * the *vx_accessor_e* enumeration. *  :arg: VX_READ_ONLY: after the function call, the content of the memory location * pointed by (*ptr) contains the distribution data. Writing into this memory location * is forbidden and its behavior is undefined. *  :arg: VX_READ_AND_WRITE : after the function call, the content of the memory * location pointed by (*ptr) contains the distribution data; writing into this memory * is allowed only for the location of bins and will result in a modification of the * affected bins in the distribution object once the distribution is unmapped. *  :arg: VX_WRITE_ONLY: after the function call, the memory location pointed by (*ptr) * contains undefined data; writing each bin of distribution is required prior to * unmapping. Bins not written by the application before unmap will become * undefined after unmap, even if they were well defined before map. *  :param mem_type: [in] A *vx_memory_type_e* enumeration that * specifies the type of the memory where the distribution is requested to be mapped. *  :param flags: [in] An integer that allows passing options to the map operation. * Use 0 for this option. * :return: A *vx_status_e* enumeration. * :retval: VX_ERROR_INVALID_REFERENCE The distribution reference is not actually a distribution * reference. * :retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect. *  :ingroup: group_distribution *  :post: *vxUnmapDistribution * with same (*map_id) value.
    '''
    return lib.vxMapDistribution(distribution, map_id, ptr, usage, mem_type, flags)
    
def UnmapDistribution(distribution, map_id):
    '''
Unmap and commit potential changes to distribution object that was previously mapped. * Unmapping a distribution invalidates the memory location from which the distribution data * could be accessed by the application. Accessing this memory location after the unmap * function completes has an undefined behavior. *  :param distribution: [in] The reference to the distribution object to unmap. *  :param map_id: [out] The unique map identifier that was returned when calling * *vxMapDistribution* . * :return: A *vx_status_e* enumeration. * :retval: VX_ERROR_INVALID_REFERENCE The distribution reference is not actually a distribution reference. * :retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect. *  :ingroup: group_distribution *  :pre: *vxMapDistribution* returning the same map_id value
    '''
    return lib.vxUnmapDistribution(distribution, map_id)
    
def CreateThreshold(c, thresh_type, data_type):
    '''
Creates a reference to a threshold object of a given type.
 :param c: [in] The reference to the overall context.
 :param thresh_type: [in] The type of threshold to create.
 :param data_type: [in] The data type of the threshold's value(s).
 :returns: An threshold reference *vx_threshold*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*.
 :ingroup: group_threshold  
    '''
    return lib.vxCreateThreshold(c, thresh_type, data_type)
    
def ReleaseThreshold(thresh):
    '''
Releases a reference to a threshold object. The object may not be garbage collected until its total reference count is zero.
 :param thresh: [in] The pointer to the threshold to release.
 :post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If thresh is not a *vx_threshold*.
 :ingroup: group_threshold  
    '''
    return lib.vxReleaseThreshold(thresh)
    
def SetThresholdAttribute(thresh, attribute, ptr, size):
    '''
Sets attributes on the threshold object.
 :param thresh: [in] The threshold object to set.
 :param attribute: [in] The attribute to modify. Use a *vx_threshold_attribute_e* enumeration.
 :param ptr: [in] The pointer to the value to which to set the attribute.
 :param size: [in] The size of the data pointed to by *ptr.*
:return: A *vx_status_e* enumeration.
 :ingroup: group_threshold  
    '''
    return lib.vxSetThresholdAttribute(thresh, attribute, ptr, size)
    
def QueryThreshold(thresh, attribute, ptr, size):
    '''
Queries an attribute on the threshold object.
 :param thresh: [in] The threshold object to set.
 :param attribute: [in] The attribute to query. Use a *vx_threshold_attribute_e* enumeration.
 :param ptr: [out] The location at which to store the resulting value.
 :param size: [in] The size of the container to which *ptr* points.
:return: A *vx_status_e* enumeration.
 :ingroup: group_threshold  
    '''
    return lib.vxQueryThreshold(thresh, attribute, ptr, size)
    
def CreateMatrix(c, data_type, columns, rows):
    '''
Creates a reference to a matrix object.
 :param c: [in] The reference to the overall context.
 :param data_type: [in] The unit format of the matrix. *VX_TYPE_UINT8* or *VX_TYPE_INT32* or *VX_TYPE_FLOAT32*.
 :param columns: [in] The first dimensionality.
 :param rows: [in] The second dimensionality.
 :returns: An matrix reference *vx_matrix*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*.
 :ingroup: group_matrix  
    '''
    return lib.vxCreateMatrix(c, data_type, columns, rows)
    
def ReleaseMatrix(mat):
    '''
Releases a reference to a matrix object. The object may not be garbage collected until its total reference count is zero.
 :param mat: [in] The matrix reference to release.
 :post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If mat is not a *vx_matrix*.
 :ingroup: group_matrix  
    '''
    return lib.vxReleaseMatrix(mat)
    
def QueryMatrix(mat, attribute, ptr, size):
    '''
Queries an attribute on the matrix object.
 :param mat: [in] The matrix object to set.
 :param attribute: [in] The attribute to query. Use a *vx_matrix_attribute_e* enumeration.
 :param ptr: [out] The location at which to store the resulting value.
 :param size: [in] The size in bytes of the container to which *ptr* points.
:return: A *vx_status_e* enumeration.
 :ingroup: group_matrix  
    '''
    return lib.vxQueryMatrix(mat, attribute, ptr, size)
    
def CopyMatrix(matrix, user_ptr, usage, user_mem_type):
    '''
Allows the application to copy from/into a matrix object. *  :param matrix: [in] The reference to the matrix object that is the source or the * destination of the copy. *  :param user_ptr: [in] The address of the memory location where to store the requested data * if the copy was requested in read mode, or from where to get the data to store into the matrix * object if the copy was requested in write mode. In the user memory, the matrix is * structured as a row-major 2D array with elements of the type corresponding to * *VX_MATRIX_TYPE*, with a number of rows corresponding to * *VX_MATRIX_ROWS* and a number of columns corresponding to * *VX_MATRIX_COLUMNS*. The accessible memory must be large * enough to contain this 2D array: * accessible memory in bytes >= sizeof(data_element) * rows * columns. *  :param usage: [in] This declares the effect of the copy with regard to the matrix object * using the *vx_accessor_e* enumeration. Only VX_READ_ONLY and VX_WRITE_ONLY * are supported: *  :arg: VX_READ_ONLY means that data are copied from the matrix object into the user memory. *  :arg: VX_WRITE_ONLY means that data are copied into the matrix object from the user memory. *  :param user_mem_type: [in] A *vx_memory_type_e* enumeration that specifies * the memory type of the memory referenced by the user_addr. * :return: A *vx_status_e* enumeration. * :retval: VX_ERROR_INVALID_REFERENCE The matrix reference is not actually a matrix reference. * :retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect. *  :ingroup: group_matrix
    '''
    return lib.vxCopyMatrix(matrix, user_ptr, usage, user_mem_type)
    
def CreateMatrixFromPattern(context, pattern, columns, rows):
    '''
Creates a reference to a matrix object from a boolean pattern. * The matrix created by this function is of type *vx_uint8*, with the value 0 representing False,  and the value 255 representing True. It supports patterns described below. See *vx_pattern_e*. - VX_PATTERN_BOX is a matrix with dimensions equal to the given number of rows and columns, and all cells equal to 255.   Dimensions of 3x3 and 5x5 must be supported. - VX_PATTERN_CROSS is a matrix with dimensions equal to the given number of rows and columns, which both must be odd numbers.   All cells in the center row and center column are equal to 255, and the rest are equal to zero.   Dimensions of 3x3 and 5x5 must be supported. - VX_PATTERN_DISK is an RxC matrix, where R and C are odd and cell (c, r) is 255 if: \n (r-R/2 + 0.5)^2 / (R/2)^2 + (c-C/2 + 0.5)^2/(C/2)^2 is less than or equal to 1, :n: and 0 otherwise. - VX_PATTERN_OTHER is any other pattern than the above (matrix created is still binary, with a value of 0 or 255). * If the matrix was created via *vxCreateMatrixFromPattern*, this attribute must be set to the  appropriate pattern enum. Otherwise the attribute must be set to VX_PATTERN_OTHER. The vx_matrix objects returned by this function are read-only. The behavior when attempting to modify such a matrix is undefined. *  :param context: [in] The reference to the overall context.
 :param pattern: [in] The pattern of the matrix. See *VX_MATRIX_PATTERN*. 
 :param columns: [in] The first dimensionality.
 :param rows: [in] The second dimensionality.
 :returns: An matrix reference *vx_matrix* of type *vx_uint8*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*.
 :ingroup: group_matrix  
    '''
    return lib.vxCreateMatrixFromPattern(context, pattern, columns, rows)
    
def CreateConvolution(context, columns, rows):
    '''
Creates a reference to a convolution matrix object.
 :param context: [in] The reference to the overall context.
 :param columns: [in] The columns dimension of the convolution. Must be odd and greater than or equal to 3 and less than the value returned from *VX_CONTEXT_CONVOLUTION_MAX_DIMENSION*.
 :param rows: [in] The rows dimension of the convolution. Must be odd and greater than or equal to 3 and less than the value returned from *VX_CONTEXT_CONVOLUTION_MAX_DIMENSION*.
 :returns: A convolution reference *vx_convolution*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*.
 :ingroup: group_convolution  
    '''
    return lib.vxCreateConvolution(context, columns, rows)
    
def ReleaseConvolution(conv):
    '''
Releases the reference to a convolution matrix. The object may not be garbage collected until its total reference count is zero.
 :param conv: [in] The pointer to the convolution matrix to release.
 :post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If conv is not a *vx_convolution*.
 :ingroup: group_convolution  
    '''
    return lib.vxReleaseConvolution(conv)
    
def QueryConvolution(conv, attribute, ptr, size):
    '''
Queries an attribute on the convolution matrix object.
 :param conv: [in] The convolution matrix object to set.
 :param attribute: [in] The attribute to query. Use a *vx_convolution_attribute_e* enumeration.
 :param ptr: [out] The location at which to store the resulting value.
 :param size: [in] The size in bytes of the container to which *ptr* points.
:return: A *vx_status_e* enumeration.
 :ingroup: group_convolution  
    '''
    return lib.vxQueryConvolution(conv, attribute, ptr, size)
    
def SetConvolutionAttribute(conv, attribute, ptr, size):
    '''
Sets attributes on the convolution object.
 :param conv: [in] The coordinates object to set.
 :param attribute: [in] The attribute to modify. Use a *vx_convolution_attribute_e* enumeration.
 :param ptr: [in] The pointer to the value to which to set the attribute.
 :param size: [in] The size in bytes of the data pointed to by *ptr.*
:return: A *vx_status_e* enumeration.
 :ingroup: group_convolution  
    '''
    return lib.vxSetConvolutionAttribute(conv, attribute, ptr, size)
    
def CopyConvolutionCoefficients(conv, user_ptr, usage, user_mem_type):
    '''
Allows the application to copy coefficients from/into a convolution object.
 :param conv: [in] The reference to the convolution object that is the source or the destination of the copy.
 :param user_ptr: [in] The address of the memory location where to store the requested coefficient data if the copy was requested in read mode, or from where to get the coefficient data to store into the convolution object if the copy was requested in write mode. In the user memory, the convolution coefficient data is structured as a row-major 2D array with elements of the type corresponding to *VX_TYPE_CONVOLUTION*, with a number of rows corresponding to *VX_CONVOLUTION_ROWS* and a number of columns corresponding to *VX_CONVOLUTION_COLUMNS*. The accessible memory must be large enough to contain this 2D array: accessible memory in bytes >= sizeof(data_element) * rows * columns.
 :param usage: [in] This declares the effect of the copy with regard to the convolution object using the *vx_accessor_e* enumeration. Only VX_READ_ONLY and VX_WRITE_ONLY are supported:
 :arg: VX_READ_ONLY means that data are copied from the convolution object into the user memory.
 :arg: VX_WRITE_ONLY means that data are copied into the convolution object from the user memory.
 :param user_mem_type: [in] A *vx_memory_type_e* enumeration that specifies the memory type of the memory referenced by the user_addr.
:return: A *vx_status_e* enumeration.
:retval: VX_ERROR_INVALID_REFERENCE The convolution reference is not actually a convolution reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
 :ingroup: group_convolution  
    '''
    return lib.vxCopyConvolutionCoefficients(conv, user_ptr, usage, user_mem_type)
    
def CreatePyramid(context, levels, scale, width, height, format):
    '''
Creates a reference to a pyramid object of the supplied number of levels.
 :param context: [in] The reference to the overall context.
 :param levels: [in] The number of levels desired. This is required to be a non-zero value.
 :param scale: [in] Used to indicate the scale between pyramid levels. This is required to be a non-zero positive value.
 :if: OPENVX_STRICT_1_0 Only permissible values are *VX_SCALE_PYRAMID_HALF* or *VX_SCALE_PYRAMID_ORB*.
\endif
 :param width: [in] The width of the 0th level image in pixels.
 :param height: [in] The height of the 0th level image in pixels.
 :param format: [in] The format of all images in the pyramid. NV12, NV21, IYUV, UYVY and YUYV formats are not supported.
 :returns: A pyramid reference *vx_pyramid* to the sub-image. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*.
 :ingroup: group_pyramid  
    '''
    return lib.vxCreatePyramid(context, levels, scale, width, height, format)
    
def CreateVirtualPyramid(graph, levels, scale, width, height, format):
    '''
Creates a reference to a virtual pyramid object of the supplied number of levels.
 :details: Virtual Pyramids can be used to connect Nodes together when the contents of the pyramids will not be accessed by the user of the API. All of the following constructions are valid:
\code vx_context context = vxCreateContext(); vx_graph graph = vxCreateGraph(context); vx_pyramid virt[] = { vxCreateVirtualPyramid(graph, 4, VX_SCALE_PYRAMID_HALF, 0, 0, VX_DF_IMAGE_VIRT), // no dimension and format specified for level 0 vxCreateVirtualPyramid(graph, 4, VX_SCALE_PYRAMID_HALF, 640, 480, VX_DF_IMAGE_VIRT), // no format specified. vxCreateVirtualPyramid(graph, 4, VX_SCALE_PYRAMID_HALF, 640, 480, VX_DF_IMAGE_U8), // no access };
\endcode
 :param graph: [in] The reference to the parent graph.
 :param levels: [in] The number of levels desired. This is required to be a non-zero value.
 :param scale: [in] Used to indicate the scale between pyramid levels. This is required to be a non-zero positive value.
 :if: OPENVX_STRICT_1_0 Only permissible values are *VX_SCALE_PYRAMID_HALF* or *VX_SCALE_PYRAMID_ORB*.
\endif
 :param width: [in] The width of the 0th level image in pixels. This may be set to zero to indicate to the interface that the value is unspecified.
 :param height: [in] The height of the 0th level image in pixels. This may be set to zero to indicate to the interface that the value is unspecified.
 :param format: [in] The format of all images in the pyramid. This may be set to *VX_DF_IMAGE_VIRT* to indicate that the format is unspecified.
 :returns: A pyramid reference *vx_pyramid*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*.
 :note: Images extracted with *vxGetPyramidLevel* behave as Virtual Images and cause *vxMapImagePatch* to return errors.
 :ingroup: group_pyramid  
    '''
    return lib.vxCreateVirtualPyramid(graph, levels, scale, width, height, format)
    
def ReleasePyramid(pyr):
    '''
Releases a reference to a pyramid object. The object may not be garbage collected until its total reference count is zero.
 :param pyr: [in] The pointer to the pyramid to release.
 :ingroup: group_pyramid
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If pyr is not a *vx_pyramid*.
 :post: After returning from this function the reference is zeroed.  
    '''
    return lib.vxReleasePyramid(pyr)
    
def QueryPyramid(pyr, attribute, ptr, size):
    '''
Queries an attribute from an image pyramid.
 :param pyr: [in] The pyramid to query.
 :param attribute: [in] The attribute for which to query. Use a *vx_pyramid_attribute_e* enumeration.
 :param ptr: [out] The location at which to store the resulting value.
 :param size: [in] The size in bytes of the container to which *ptr* points.
:return: A *vx_status_e* enumeration.
 :ingroup: group_pyramid  
    '''
    return lib.vxQueryPyramid(pyr, attribute, ptr, size)
    
def GetPyramidLevel(pyr, index):
    '''
Retrieves a level of the pyramid as a *vx_image*, which can be used elsewhere in OpenVX. A call to vxReleaseImage is necessary to release an image for each  call of vxGetPyramidLevel.
 :param pyr: [in] The pyramid object.
 :param index: [in] The index of the level, such that index is less than levels.
:return: A *vx_image* reference. Any possible errors  preventing a successful creation should be checked using *vxGetStatus*.
:retval: 0 Indicates that the index or the object is invalid.
 :ingroup: group_pyramid  
    '''
    return lib.vxGetPyramidLevel(pyr, index)
    
def CreateRemap(context, src_width, src_height, dst_width, dst_height):
    '''
Creates a remap table object.
 :param context: [in] The reference to the overall context.
 :param src_width: [in] Width of the source image in pixel.
 :param src_height: [in] Height of the source image in pixels.
 :param dst_width: [in] Width of the destination image in pixels.
 :param dst_height: [in] Height of the destination image in pixels.
 :ingroup: group_remap
 :returns: A remap reference *vx_remap*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*.  
    '''
    return lib.vxCreateRemap(context, src_width, src_height, dst_width, dst_height)
    
def ReleaseRemap(table):
    '''
Releases a reference to a remap table object. The object may not be garbage collected until its total reference count is zero.
 :param table: [in] The pointer to the remap table to release.
 :post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If table is not a *vx_remap*.
 :ingroup: group_remap  
    '''
    return lib.vxReleaseRemap(table)
    
def SetRemapPoint(table, dst_x, dst_y, src_x, src_y):
    '''
Assigns a destination pixel mapping to the source pixel.
 :param table: [in] The remap table reference.
 :param dst_x: [in] The destination x coordinate.
 :param dst_y: [in] The destination y coordinate.
 :param src_x: [in] The source x coordinate in float representation to allow interpolation.
 :param src_y: [in] The source y coordinate in float representation to allow interpolation.
 :ingroup: group_remap
:return: A *vx_status_e* enumeration.  
    '''
    return lib.vxSetRemapPoint(table, dst_x, dst_y, src_x, src_y)
    
def GetRemapPoint(table, dst_x, dst_y, src_x, src_y):
    '''
Retrieves the source pixel point from a destination pixel.
 :param table: [in] The remap table reference.
 :param dst_x: [in] The destination x coordinate.
 :param dst_y: [in] The destination y coordinate.
 :param src_x: [out] The pointer to the location to store the source x coordinate in float representation to allow interpolation.
 :param src_y: [out] The pointer to the location to store the source y coordinate in float representation to allow interpolation.
 :ingroup: group_remap
:return: A *vx_status_e* enumeration.  
    '''
    return lib.vxGetRemapPoint(table, dst_x, dst_y, src_x, src_y)
    
def QueryRemap(r, attribute, ptr, size):
    '''
Queries attributes from a Remap table.
 :param r: [in] The remap to query.
 :param attribute: [in] The attribute to query. Use a *vx_remap_attribute_e* enumeration.
 :param ptr: [out] The location at which to store the resulting value.
 :param size: [in] The size in bytes of the container to which *ptr* points.
:return: A *vx_status_e* enumeration.
 :ingroup: group_remap  
    '''
    return lib.vxQueryRemap(r, attribute, ptr, size)
    
def CreateArray(context, item_type, capacity):
    '''
* Creates a reference to an Array object. * User must specify the Array capacity (i.e., the maximal number of items that the array can hold). *  :param context: [in] The reference to the overall Context.
 :param item_type: [in] The type of objects to hold. Types allowed are: plain scalar types (i.e.  type with enum below *VX_TYPE_SCALAR_MAX*), *VX_TYPE_RECTANGLE*, *VX_TYPE_KEYPOINT*, *VX_TYPE_COORDINATES2D*, *VX_TYPE_COORDINATES3D* and  user registered structures. Use:
 :arg: *VX_TYPE_RECTANGLE* for *vx_rectangle_t*.
 :arg: *VX_TYPE_KEYPOINT* for *vx_keypoint_t*.
 :arg: *VX_TYPE_COORDINATES2D* for *vx_coordinates2d_t*.
 :arg: *VX_TYPE_COORDINATES3D* for *vx_coordinates3d_t*.
 :arg: *vx_enum* returned from *vxRegisterUserStruct*.
 :param capacity: [in] The maximal number of items that the array can hold. *  :returns: An array reference *vx_array*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*. *  :ingroup: group_array  
    '''
    return lib.vxCreateArray(context, item_type, capacity)
    
def CreateVirtualArray(graph, item_type, capacity):
    '''
* Creates an opaque reference to a virtual Array with no direct user access. * Virtual Arrays are useful when item type or capacity are unknown ahead of time and the Array is used as internal graph edge. Virtual arrays are scoped within the parent graph only. * All of the following constructions are allowed.
\code vx_context context = vxCreateContext(); vx_graph graph = vxCreateGraph(context); vx_array virt[] = { vxCreateVirtualArray(graph, 0, 0), // totally unspecified vxCreateVirtualArray(graph, VX_TYPE_KEYPOINT, 0), // unspecified capacity vxCreateVirtualArray(graph, VX_TYPE_KEYPOINT, 1000), // no access };
\endcode *  :param graph: [in] The reference to the parent graph.
 :param item_type: [in] The type of objects to hold. Types allowed are: plain scalar types (i.e.  type with enum below *VX_TYPE_SCALAR_MAX*), *VX_TYPE_RECTANGLE*, *VX_TYPE_KEYPOINT*, *VX_TYPE_COORDINATES2D*, *VX_TYPE_COORDINATES3D* and  user registered structures.  This may to set to zero to indicate an unspecified item type.
 :param capacity: [in] The maximal number of items that the array can hold. This may be to set to zero to indicate an unspecified capacity.
 :see: vxCreateArray for a type list.
 :returns: A array reference *vx_array*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*. *  :ingroup: group_array  
    '''
    return lib.vxCreateVirtualArray(graph, item_type, capacity)
    
def ReleaseArray(arr):
    '''
* Releases a reference of an Array object. The object may not be garbage collected until its total reference count is zero. After returning from this function the reference is zeroed.
 :param arr: [in] The pointer to the Array to release.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If arr is not a *vx_array*.
 :ingroup: group_array  
    '''
    return lib.vxReleaseArray(arr)
    
def QueryArray(arr, attribute, ptr, size):
    '''
* Queries the Array for some specific information. *  :param arr: [in] The reference to the Array.
 :param attribute: [in] The attribute to query. Use a *vx_array_attribute_e*.
 :param ptr: [out] The location at which to store the resulting value.
 :param size: [in] The size in bytes of the container to which *ptr* points. * :return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS                   No errors.
:retval: VX_ERROR_INVALID_REFERENCE   If the *arr* is not a *vx_array*.
:retval: VX_ERROR_NOT_SUPPORTED       If the *attribute* is not a value supported on this implementation.
:retval: VX_ERROR_INVALID_PARAMETERS  If any of the other parameters are incorrect. *  :ingroup: group_array  
    '''
    return lib.vxQueryArray(arr, attribute, ptr, size)
    
def AddArrayItems(arr, count, ptr, stride):
    '''
* Adds items to the Array. * This function increases the container size. * By default, the function does not reallocate memory, so if the container is already full (number of elements is equal to capacity) or it doesn't have enough space, the function returns *VX_FAILURE* error code. *  :param arr: [in] The reference to the Array.
 :param count: [in] The total number of elements to insert.
 :param ptr: [in] The location from which to read the input values.
 :param stride: [in] The number of bytes between the beginning of two consecutive elements. * :return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS                   No errors.
:retval: VX_ERROR_INVALID_REFERENCE   If the *arr* is not a *vx_array*.
:retval: VX_FAILURE                   If the Array is full.
:retval: VX_ERROR_INVALID_PARAMETERS  If any of the other parameters are incorrect. *  :ingroup: group_array  
    '''
    return lib.vxAddArrayItems(arr, count, ptr, stride)
    
def TruncateArray(arr, new_num_items):
    '''
* Truncates an Array (remove items from the end). *  :param arr: [in,out] The reference to the Array.
 :param new_num_items: [in] The new number of items for the Array. * :return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS                   No errors.
:retval: VX_ERROR_INVALID_REFERENCE   If the *arr* is not a *vx_array*.
:retval: VX_ERROR_INVALID_PARAMETERS  The *new_size* is greater than the current size. *  :ingroup: group_array  
    '''
    return lib.vxTruncateArray(arr, new_num_items)
    
def CopyArrayRange(array, range_start, range_end, user_stride, user_ptr, usage, user_mem_type):
    '''
Allows the application to copy a range from/into an array object. *  :param array: [in] The reference to the array object that is the source or the * destination of the copy. *  :param range_start: [in] The index of the first item of the array object to copy. *  :param range_end: [in] The index of the item following the last item of the * array object to copy. (range_end range_start) items are copied from index * range_start included. The range must be within the bounds of the array: * 0 <= range_start < range_end <= number of items in the array. *  :param user_stride: [in] The number of bytes between the beginning of two consecutive * items in the user memory pointed by user_ptr. The layout of the user memory must * follow an item major order: * user_stride >= element size in bytes. *  :param user_ptr: [in] The address of the memory location where to store the requested data * if the copy was requested in read mode, or from where to get the data to store into the array * object if the copy was requested in write mode. The accessible memory must be large enough * to contain the specified range with the specified stride: * accessible memory in bytes >= (range_end range_start) * user_stride. *  :param usage: [in] This declares the effect of the copy with regard to the array object * using the *vx_accessor_e* enumeration. Only VX_READ_ONLY and VX_WRITE_ONLY * are supported: *  :arg: VX_READ_ONLY means that data are copied from the array object into the user memory. *  :arg: VX_WRITE_ONLY means that data are copied into the array object from the user memory. *  :param user_mem_type: [in] A *vx_memory_type_e* enumeration that specifies * the memory type of the memory referenced by the user_addr. * :return: A *vx_status_e* enumeration. * :retval: VX_ERROR_OPTIMIZED_AWAY This is a reference to a virtual array that cannot be * accessed by the application. * :retval: VX_ERROR_INVALID_REFERENCE The array reference is not actually an array reference. * :retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect. *  :ingroup: group_array
    '''
    return lib.vxCopyArrayRange(array, range_start, range_end, user_stride, user_ptr, usage, user_mem_type)
    
def MapArrayRange(array, range_start, range_end, map_id, stride, ptr, usage, mem_type, flags):
    '''
Allows the application to get direct access to a range of an array object. *  :param array: [in] The reference to the array object that contains the range to map. *  :param range_start: [in] The index of the first item of the array object to map. *  :param range_end: [in] The index of the item following the last item of the * array object to map. (range_end range_start) items are mapped, starting from index * range_start included. The range must be within the bounds of the array: * Must be 0 <= range_start < range_end <= number of items. *  :param map_id: [out] The address of a vx_map_id variable where the function * returns a map identifier. *  :arg: (*map_id) must eventually be provided as the map_id parameter of a call to * *vxUnmapArrayRange*. *  :param stride: [out] The address of a vx_size variable where the function * returns the memory layout of the mapped array range. The function sets (*stride) * to the number of bytes between the beginning of two consecutive items. * The application must consult (*stride) to access the array items starting from * address (*ptr). The layout of the mapped array follows an item major order: * (*stride) >= item size in bytes. *  :param ptr: [out] The address of a pointer that the function sets to the * address where the requested data can be accessed. The returned (*ptr) address * is only valid between the call to the function and the corresponding call to * *vxUnmapArrayRange*. *  :param usage: [in] This declares the access mode for the array range, using * the *vx_accessor_e* enumeration. *  :arg: VX_READ_ONLY: after the function call, the content of the memory location * pointed by (*ptr) contains the array range data. Writing into this memory location * is forbidden and its behavior is undefined. *  :arg: VX_READ_AND_WRITE : after the function call, the content of the memory * location pointed by (*ptr) contains the array range data; writing into this memory * is allowed only for the location of items and will result in a modification of the * affected items in the array object once the range is unmapped. Writing into * a gap between items (when (*stride) > item size in bytes) is forbidden and its * behavior is undefined. *  :arg: VX_WRITE_ONLY: after the function call, the memory location pointed by (*ptr) * contains undefined data; writing each item of the range is required prior to * unmapping. Items not written by the application before unmap will become * undefined after unmap, even if they were well defined before map. Like for * VX_READ_AND_WRITE, writing into a gap between items is forbidden and its behavior * is undefined. *  :param mem_type: [in] A *vx_memory_type_e* enumeration that * specifies the type of the memory where the array range is requested to be mapped. *  :param flags: [in] An integer that allows passing options to the map operation. * Use the *vx_map_flag_e* enumeration. * :return: A *vx_status_e* enumeration. * :retval: VX_ERROR_OPTIMIZED_AWAY This is a reference to a virtual array that cannot be * accessed by the application. * :retval: VX_ERROR_INVALID_REFERENCE The array reference is not actually an array * reference. * :retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect. *  :ingroup: group_array *  :post: *vxUnmapArrayRange * with same (*map_id) value.
    '''
    return lib.vxMapArrayRange(array, range_start, range_end, map_id, stride, ptr, usage, mem_type, flags)
    
def UnmapArrayRange(array, map_id):
    '''
Unmap and commit potential changes to an array object range that was previously mapped. * Unmapping an array range invalidates the memory location from which the range could * be accessed by the application. Accessing this memory location after the unmap function * completes has an undefined behavior. *  :param array: [in] The reference to the array object to unmap. *  :param map_id: [out] The unique map identifier that was returned when calling * *vxMapArrayRange* . * :return: A *vx_status_e* enumeration. * :retval: VX_ERROR_INVALID_REFERENCE The array reference is not actually an array reference. * :retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect. *  :ingroup: group_array *  :pre: *vxMapArrayRange* returning the same map_id value
    '''
    return lib.vxUnmapArrayRange(array, map_id)
    
def CreateObjectArray(context, exemplar, count):
    '''
* Creates a reference to an ObjectArray of count objects. * It uses the metadata of the exemplar to determine the object attributes,  ignoring the object data. It does not alter the exemplar or keep or release  the reference to the exemplar. For the definition of supported attributes see  *vxSetMetaFormatAttribute*. In case the exemplar is a virtual object  it must be of immutable metadata, thus it is not allowed to be dimensionless or formatless.  *  :param context: [in] The reference to the overall Context.
 :param exemplar: [in] The exemplar object that defines the metadata of the created objects in the ObjectArray. 
 :param count: [in] Number of Objects to create in the ObjectArray.   *  :returns: An ObjectArray reference *vx_object_array*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*. Data objects are not initialized by this function. *  :ingroup: group_object_array  
    '''
    return lib.vxCreateObjectArray(context, exemplar, count)
    
def CreateVirtualObjectArray(graph, exemplar, count):
    '''
* Creates an opaque reference to a virtual ObjectArray with no direct user access. * This function creates an ObjectArray of count objects with similar behavior as  *vxCreateObjectArray*. The only difference is that the objects that are  created are virtual in the given graph. *  :param graph: [in] Reference to the graph where to create the virtual ObjectArray.  
 :param exemplar: [in] The exemplar object that defines the type of object in the ObjectArray.  Only exemplar type of *vx_image*, *vx_array* and  *vx_pyramid* are allowed.  
 :param count: [in] Number of Objects to create in the ObjectArray. 
 :returns: A ObjectArray reference *vx_object_array*. Any possible errors preventing a  successful creation should be checked using *vxGetStatus*.
 :ingroup: group_object_array  
    '''
    return lib.vxCreateVirtualObjectArray(graph, exemplar, count)
    
def GetObjectArrayItem(arr, index):
    '''
* Retrieves the reference to the OpenVX Object in location index of the ObjectArray.  * This is a vx_reference, which can be used elsewhere in OpenVX. A call to vxRelease<Object> or *vxReleaseReference* is necessary to release the Object for each call to this function.  *  :param arr: [in] The ObjectArray.
 :param index: [in] The index of the object in the ObjectArray.
:return: A reference to an OpenVX data object. 
 :ingroup: group_object_array  
    '''
    return lib.vxGetObjectArrayItem(arr, index)
    
def ReleaseObjectArray(arr):
    '''
* Releases a reference of an ObjectArray object. * The object may not be garbage collected until its total reference and its contained objects  count is zero. After returning from this function the reference is zeroed/cleared. *  :param arr: [in] The pointer to the ObjectArray to release.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If arr is not a *vx_object_array*.
 :ingroup: group_object_array  
    '''
    return lib.vxReleaseObjectArray(arr)
    
def QueryObjectArray(arr, attribute, ptr, size):
    '''
* Queries an atribute from the ObjectArray.  *  :param arr: [in] The reference to the ObjectArray.
 :param attribute: [in] The attribute to query. Use a *vx_object_array_attribute_e*.
 :param ptr: [out] The location at which to store the resulting value.
 :param size: [in] The size in bytes of the container to which *ptr* points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS                   No errors.
:retval: VX_ERROR_INVALID_REFERENCE   If the *arr* is not a *vx_object_array*.
:retval: VX_ERROR_NOT_SUPPORTED       If the *attribute* is not a value supported on this implementation.
:retval: VX_ERROR_INVALID_PARAMETERS  If any of the other parameters are incorrect. *  :ingroup: group_object_array  
    '''
    return lib.vxQueryObjectArray(arr, attribute, ptr, size)
    
def SetMetaFormatAttribute(meta, attribute, ptr, size):
    '''
This function allows a user to set the attributes of a *vx_meta_format* object in a kernel output validator. * The vx_meta_format object contains two types of information : data object meta data and  some specific information that defines how the valid region of an image changes * The meta data attributes that can be set are identified by this list: - vx_image : VX_IMAGE_FORMAT, VX_IMAGE_HEIGHT, VX_IMAGE_WIDTH - vx_array : VX_ARRAY_CAPACITY, VX_ARRAY_ITEMTYPE - vx_pyramid : VX_PYRAMID_FORMAT, VX_PYRAMID_HEIGHT, VX_PYRAMID_WIDTH, VX_PYRAMID_LEVELS, VX_PYRAMID_SCALE - vx_scalar : VX_SCALAR_TYPE - vx_matrix : VX_MATRIX_TYPE, VX_MATRIX_ROWS, VX_MATRIX_COLUMNS - vx_distribution : VX_DISTRIBUTION_BINS, VX_DISTRIBUTION_OFFSET, VX_DISTRIBUTION_RANGE - vx_remap : VX_REMAP_SOURCE_WIDTH, VX_REMAP_SOURCE_HEIGHT, VX_REMAP_DESTINATION_WIDTH, VX_REMAP_DESTINATION_HEIGHT - vx_lut : VX_LUT_TYPE, VX_LUT_COUNT - vx_threshold : VX_THRESHOLD_TYPE - VX_VALID_RECT_CALLBACK
 :note: For vx_image, a specific attribute can be used to specify the valid region evolution. This information is not a meta data. *  :param meta: [in] The reference to the vx_meta_format struct to set 
 :param attribute: [in] Use the subset of data object attributes that define the meta data of this object or attributes from *vx_meta_format*.
 :param ptr: [in] The input pointer of the value to set on the meta format object.
 :param size: [in] The size in bytes of the object to which *ptr* points.
 :ingroup: group_user_kernels
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS The attribute was set.
:retval: VX_ERROR_INVALID_REFERENCE meta was not a *vx_meta_format*.
:retval: VX_ERROR_INVALID_PARAMETER size was not correct for the type needed.
:retval: VX_ERROR_NOT_SUPPORTED the object attribute was not supported on the meta format object.
:retval: VX_ERROR_INVALID_TYPE attribute type did not match known meta format type.  
    '''
    return lib.vxSetMetaFormatAttribute(meta, attribute, ptr, size)
    
def SetMetaFormatFromReference(meta, exemplar):
    '''
Set a meta format object from an exemplar data object reference * This function sets a vx_meta_format object from the meta data of the exemplar *  :param meta: [in] The meta format object to set
 :param exemplar: [in] The exemplar data object.
 :ingroup: group_user_kernels
:return: A vx_status_e enumeration.
:retval: VX_SUCCESS The meta format was correctly set.
:retval: VX_ERROR_INVALID_REFERENCE the reference was not a reference to a data object  
    '''
    return lib.vxSetMetaFormatFromReference(meta, exemplar)
    
def ColorConvertNode(graph, input, output):
    '''
[Graph] Creates a color conversion node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input image from which to convert.
 :param output: [out] The output image to which to convert.
 :see: *VX_KERNEL_COLOR_CONVERT*
 :ingroup: group_vision_function_colorconvert
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxColorConvertNode(graph, input, output)
    
def ChannelExtractNode(graph, input, channel, output):
    '''
[Graph] Creates a channel extract node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input image. Must be one of the defined vx_df_image_e multi-channel formats.
 :param channel: [in] The *vx_channel_e* channel to extract.
 :param output: [out] The output image. Must be *VX_DF_IMAGE_U8*. * :see: VX_KERNEL_CHANNEL_EXTRACT*
 :ingroup: group_vision_function_channelextract
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxChannelExtractNode(graph, input, channel, output)
    
def ChannelCombineNode(graph, plane0, plane1, plane2, plane3, output):
    '''
[Graph] Creates a channel combine node.
 :param graph: [in] The graph reference.
 :param plane0: [in] The plane that forms channel 0. Must be *VX_DF_IMAGE_U8*.
 :param plane1: [in] The plane that forms channel 1. Must be *VX_DF_IMAGE_U8*.
 :param plane2: [in] [optional] The plane that forms channel 2. Must be *VX_DF_IMAGE_U8*.
 :param plane3: [in] [optional] The plane that forms channel 3. Must be *VX_DF_IMAGE_U8*.
 :param output: [out] The output image. The format of the image must be defined, even if the image is virtual.
 :see: *VX_KERNEL_CHANNEL_COMBINE*
 :ingroup: group_vision_function_channelcombine
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxChannelCombineNode(graph, plane0, plane1, plane2, plane3, output)
    
def PhaseNode(graph, grad_x, grad_y, orientation):
    '''
[Graph] Creates a Phase node.
 :param graph: [in] The reference to the graph.
 :param grad_x: [in] The input x image. This must be in *VX_DF_IMAGE_S16* format.
 :param grad_y: [in] The input y image. This must be in *VX_DF_IMAGE_S16* format.
 :param orientation: [out] The phase image. This is in *VX_DF_IMAGE_U8* format.
 :see: *VX_KERNEL_PHASE*
 :ingroup: group_vision_function_phase
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxPhaseNode(graph, grad_x, grad_y, orientation)
    
def Sobel3x3Node(graph, input, output_x, output_y):
    '''
[Graph] Creates a Sobel3x3 node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param output_x: [out] [optional] The output gradient in the x direction in *VX_DF_IMAGE_S16*.
 :param output_y: [out] [optional] The output gradient in the y direction in *VX_DF_IMAGE_S16*.
 :see: *VX_KERNEL_SOBEL_3x3*
 :ingroup: group_vision_function_sobel3x3
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxSobel3x3Node(graph, input, output_x, output_y)
    
def MagnitudeNode(graph, grad_x, grad_y, mag):
    '''
[Graph] Create a Magnitude node.
 :param graph: [in] The reference to the graph.
 :param grad_x: [in] The input x image. This must be in *VX_DF_IMAGE_S16* format.
 :param grad_y: [in] The input y image. This must be in *VX_DF_IMAGE_S16* format.
 :param mag: [out] The magnitude image. This is in *VX_DF_IMAGE_S16* format.
 :see: *VX_KERNEL_MAGNITUDE*
 :ingroup: group_vision_function_magnitude
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxMagnitudeNode(graph, grad_x, grad_y, mag)
    
def ScaleImageNode(graph, src, dst, type):
    '''
[Graph] Creates a Scale Image Node.
 :param graph: [in] The reference to the graph.
 :param src: [in] The source image of type *VX_DF_IMAGE_U8*.
 :param dst: [out] The destination image of type *VX_DF_IMAGE_U8*.
 :param type: [in] The interpolation type to use.  :see: vx_interpolation_type_e.
 :ingroup: group_vision_function_scale_image
 :note: The destination image must have a defined size and format. The border modes  *VX_NODE_BORDER* value *VX_BORDER_UNDEFINED*,  *VX_BORDER_REPLICATE* and *VX_BORDER_CONSTANT* are supported.
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxScaleImageNode(graph, src, dst, type)
    
def TableLookupNode(graph, input, lut, output):
    '''
[Graph] Creates a Table Lookup node. If a value from the input image is not present in the lookup table, the result is undefined.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
 :param lut: [in] The LUT which is of type *VX_TYPE_UINT8* or *VX_TYPE_INT16*.
 :param output: [out] The output image of the same type as the input image.
 :ingroup: group_vision_function_lut
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*.  
    '''
    return lib.vxTableLookupNode(graph, input, lut, output)
    
def HistogramNode(graph, input, distribution):
    '''
[Graph] Creates a Histogram node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input image in *VX_DF_IMAGE_U8*.
 :param distribution: [out] The output distribution.
 :ingroup: group_vision_function_histogram
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxHistogramNode(graph, input, distribution)
    
def EqualizeHistNode(graph, input, output):
    '''
[Graph] Creates a Histogram Equalization node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The grayscale input image in *VX_DF_IMAGE_U8*.
 :param output: [out] The grayscale output image of type *VX_DF_IMAGE_U8* with equalized brightness and contrast.
 :ingroup: group_vision_function_equalize_hist
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxEqualizeHistNode(graph, input, output)
    
def AbsDiffNode(graph, in1, in2, out):
    '''
[Graph] Creates an AbsDiff node.
 :param graph: [in] The reference to the graph.
 :param in1: [in] An input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
 :param in2: [in] An input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
 :param out: [out] The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
 :ingroup: group_vision_function_absdiff
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxAbsDiffNode(graph, in1, in2, out)
    
def MeanStdDevNode(graph, input, mean, stddev):
    '''
[Graph] Creates a mean value and standard deviation node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input image. *VX_DF_IMAGE_U8* is supported.
 :param mean: [out] The *VX_TYPE_FLOAT32* average pixel value.
 :param stddev: [out] The *VX_TYPE_FLOAT32* standard deviation of the pixel values.
 :ingroup: group_vision_function_meanstddev
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxMeanStdDevNode(graph, input, mean, stddev)
    
def ThresholdNode(graph, input, thresh, output):
    '''
[Graph] Creates a Threshold node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input image. *VX_DF_IMAGE_U8* is supported.
 :param thresh: [in] The thresholding object that defines the parameters of the operation. The *VX_THRESHOLD_TRUE_VALUE* and *VX_THRESHOLD_FALSE_VALUE* are taken into account. 
 :param output: [out] The output Boolean image with values either *VX_THRESHOLD_TRUE_VALUE* or  *VX_THRESHOLD_FALSE_VALUE* from the  :e: thresh parameter.
 :ingroup: group_vision_function_threshold
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxThresholdNode(graph, input, thresh, output)
    
def IntegralImageNode(graph, input, output):
    '''
[Graph] Creates an Integral Image Node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param output: [out] The output image in *VX_DF_IMAGE_U32* format.
 :ingroup: group_vision_function_integral_image
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxIntegralImageNode(graph, input, output)
    
def Erode3x3Node(graph, input, output):
    '''
[Graph] Creates an Erosion Image Node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param output: [out] The output image in *VX_DF_IMAGE_U8* format.
 :ingroup: group_vision_function_erode_image
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxErode3x3Node(graph, input, output)
    
def Dilate3x3Node(graph, input, output):
    '''
[Graph] Creates a Dilation Image Node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param output: [out] The output image in *VX_DF_IMAGE_U8* format.
 :ingroup: group_vision_function_dilate_image
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxDilate3x3Node(graph, input, output)
    
def Median3x3Node(graph, input, output):
    '''
[Graph] Creates a Median Image Node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param output: [out] The output image in *VX_DF_IMAGE_U8* format.
 :ingroup: group_vision_function_median_image
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxMedian3x3Node(graph, input, output)
    
def Box3x3Node(graph, input, output):
    '''
[Graph] Creates a Box Filter Node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param output: [out] The output image in *VX_DF_IMAGE_U8* format.
 :ingroup: group_vision_function_box_image
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxBox3x3Node(graph, input, output)
    
def Gaussian3x3Node(graph, input, output):
    '''
[Graph] Creates a Gaussian Filter Node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param output: [out] The output image in *VX_DF_IMAGE_U8* format.
 :ingroup: group_vision_function_gaussian_image
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxGaussian3x3Node(graph, input, output)
    
def NonLinearFilterNode(graph, function, input, mask, output):
    '''
[Graph] Creates a Non-linear Filter Node.
 :param graph: [in] The reference to the graph.
 :param function: [in] The non-linear filter function. See *vx_non_linear_filter_e*.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param mask: [in] The mask to be applied to the Non-linear function. *VX_MATRIX_ORIGIN* attribute is used  to place the mask appropriately when computing the resulting image. See *vxCreateMatrixFromPattern*.  
 :param output: [out] The output image in *VX_DF_IMAGE_U8* format.
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus* 
 :ingroup: group_vision_function_nonlinear_filter  
    '''
    return lib.vxNonLinearFilterNode(graph, function, input, mask, output)
    
def ConvolveNode(graph, input, conv, output):
    '''
[Graph] Creates a custom convolution node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param conv: [in] The *vx_int16* convolution matrix.
 :param output: [out] The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
 :ingroup: group_vision_function_custom_convolution
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*   
    '''
    return lib.vxConvolveNode(graph, input, conv, output)
    
def GaussianPyramidNode(graph, input, gaussian):
    '''
[Graph] Creates a node for a Gaussian Image Pyramid.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param gaussian: [out] The Gaussian pyramid with *VX_DF_IMAGE_U8* to construct.
 :ingroup: group_vision_function_gaussian_pyramid
 :see: group_pyramid
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxGaussianPyramidNode(graph, input, gaussian)
    
def LaplacianPyramidNode(graph, input, laplacian, output):
    '''
[Graph] Creates a node for a Laplacian Image Pyramid.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param laplacian: [out] The Laplacian pyramid with *VX_DF_IMAGE_S16* to construct.
 :param output: [out] The lowest resolution image of type *VX_DF_IMAGE_S16* necessary to reconstruct the input image from the pyramid.
 :ingroup: group_vision_function_laplacian_pyramid
 :see: group_pyramid
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxLaplacianPyramidNode(graph, input, laplacian, output)
    
def LaplacianReconstructNode(graph, laplacian, input, output):
    '''
[Graph] Reconstructs an image from a Laplacian Image pyramid.
 :param graph: [in] The reference to the graph.
 :param laplacian: [in] The Laplacian pyramid with *VX_DF_IMAGE_S16* format.
 :param input: [in] The lowest resolution image of type *VX_DF_IMAGE_S16* for the Laplacian pyramid
 :param output: [out] The output image of type *VX_DF_IMAGE_U8* with the highest possible resolution reconstructed from the Laplacian pyramid.
 :ingroup: group_vision_function_laplacian_reconstruct
 :see: group_pyramid
:return: *vx_node*.
:retval: 0 Node could not be created.
:retval: * Node handle.  
    '''
    return lib.vxLaplacianReconstructNode(graph, laplacian, input, output)
    
def AccumulateImageNode(graph, input, accum):
    '''
[Graph] Creates an accumulate node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param accum: [in,out] The accumulation image in *VX_DF_IMAGE_S16*.
 :ingroup: group_vision_function_accumulate
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxAccumulateImageNode(graph, input, accum)
    
def AccumulateWeightedImageNode(graph, input, alpha, accum):
    '''
[Graph] Creates a weighted accumulate node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param alpha: [in] The input *VX_TYPE_FLOAT32* scalar value with a value in the range of  :f$: 0.0 \le \alpha \le 1.0 \f$.
 :param accum: [in,out] The *VX_DF_IMAGE_U8* accumulation image.
 :ingroup: group_vision_function_accumulate_weighted
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxAccumulateWeightedImageNode(graph, input, alpha, accum)
    
def AccumulateSquareImageNode(graph, input, shift, accum):
    '''
[Graph] Creates an accumulate square node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param shift: [in] The input *VX_TYPE_UINT32* with a value in the range of  :f$: 0 \le shift \le 15 \f$.
 :param accum: [in,out] The accumulation image in *VX_DF_IMAGE_S16*.
 :ingroup: group_vision_function_accumulate_square
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxAccumulateSquareImageNode(graph, input, shift, accum)
    
def MinMaxLocNode(graph, input, minVal, maxVal, minLoc, maxLoc, minCount, maxCount):
    '''
[Graph] Creates a min,max,loc node.
 :param graph: [in] The reference to create the graph.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
 :param minVal: [out] The minimum value in the image, which corresponds to the type of the input.
 :param maxVal: [out] The maximum value in the image, which corresponds to the type of the input.
 :param minLoc: [out] The minimum *VX_TYPE_COORDINATES2D* locations (optional). If the input image has several minimums, the kernel will return up to the capacity of the array.
 :param maxLoc: [out] The maximum *VX_TYPE_COORDINATES2D* locations (optional). If the input image has several maximums, the kernel will return up to the capacity of the array.
 :param minCount: [out] The total number of detected minimums in image (optional). Use a *VX_TYPE_UINT32* scalar.
 :param maxCount: [out] The total number of detected maximums in image (optional). Use a *VX_TYPE_UINT32* scalar.
 :ingroup: group_vision_function_minmaxloc
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxMinMaxLocNode(graph, input, minVal, maxVal, minLoc, maxLoc, minCount, maxCount)
    
def AndNode(graph, in1, in2, out):
    '''
[Graph] Creates a bitwise AND node.
 :param graph: [in] The reference to the graph.
 :param in1: [in] A *VX_DF_IMAGE_U8* input image.
 :param in2: [in] A *VX_DF_IMAGE_U8* input image.
 :param out: [out] The *VX_DF_IMAGE_U8* output image.
 :ingroup: group_vision_function_and
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxAndNode(graph, in1, in2, out)
    
def OrNode(graph, in1, in2, out):
    '''
[Graph] Creates a bitwise INCLUSIVE OR node.
 :param graph: [in] The reference to the graph.
 :param in1: [in] A *VX_DF_IMAGE_U8* input image.
 :param in2: [in] A *VX_DF_IMAGE_U8* input image.
 :param out: [out] The *VX_DF_IMAGE_U8* output image.
 :ingroup: group_vision_function_or
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxOrNode(graph, in1, in2, out)
    
def XorNode(graph, in1, in2, out):
    '''
[Graph] Creates a bitwise EXCLUSIVE OR node.
 :param graph: [in] The reference to the graph.
 :param in1: [in] A *VX_DF_IMAGE_U8* input image.
 :param in2: [in] A *VX_DF_IMAGE_U8* input image.
 :param out: [out] The *VX_DF_IMAGE_U8* output image.
 :ingroup: group_vision_function_xor
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxXorNode(graph, in1, in2, out)
    
def NotNode(graph, input, output):
    '''
[Graph] Creates a bitwise NOT node.
 :param graph: [in] The reference to the graph.
 :param input: [in] A *VX_DF_IMAGE_U8* input image.
 :param output: [out] The *VX_DF_IMAGE_U8* output image.
 :ingroup: group_vision_function_not
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxNotNode(graph, input, output)
    
def MultiplyNode(graph, in1, in2, scale, overflow_policy, rounding_policy, out):
    '''
[Graph] Creates an pixelwise-multiplication node.
 :param graph: [in] The reference to the graph.
 :param in1: [in] An input image, *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
 :param in2: [in] An input image, *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
 :param scale: [in] A non-negative *VX_TYPE_FLOAT32* multiplied to each product before overflow handling.
 :param overflow_policy: [in] A *VX_TYPE_ENUM* of the *vx_convert_policy_e* enumeration.
 :param rounding_policy: [in] A *VX_TYPE_ENUM* of the *vx_round_policy_e* enumeration.
 :param out: [out] The output image, a *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* image.
 :ingroup: group_vision_function_mult
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxMultiplyNode(graph, in1, in2, scale, overflow_policy, rounding_policy, out)
    
def AddNode(graph, in1, in2, policy, out):
    '''
[Graph] Creates an arithmetic addition node.
 :param graph: [in] The reference to the graph.
 :param in1: [in] An input image, *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
 :param in2: [in] An input image, *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
 :param policy: [in] A *VX_TYPE_ENUM* of the vx_convert_policy_e enumeration.
 :param out: [out] The output image, a *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* image.
 :ingroup: group_vision_function_add
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxAddNode(graph, in1, in2, policy, out)
    
def SubtractNode(graph, in1, in2, policy, out):
    '''
[Graph] Creates an arithmetic subtraction node.
 :param graph: [in] The reference to the graph.
 :param in1: [in] An input image, *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*, the minuend.
 :param in2: [in] An input image, *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*, the subtrahend.
 :param policy: [in] A *VX_TYPE_ENUM* of the vx_convert_policy_e enumeration.
 :param out: [out] The output image, a *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* image.
 :ingroup: group_vision_function_sub
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxSubtractNode(graph, in1, in2, policy, out)
    
def ConvertDepthNode(graph, input, output, policy, shift):
    '''
[Graph] Creates a bit-depth conversion node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input image.
 :param output: [out] The output image.
 :param policy: [in] A *VX_TYPE_ENUM* of the *vx_convert_policy_e* enumeration.
 :param shift: [in] A scalar containing a *VX_TYPE_INT32* of the shift value.
 :ingroup: group_vision_function_convertdepth
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxConvertDepthNode(graph, input, output, policy, shift)
    
def CannyEdgeDetectorNode(graph, input, hyst, gradient_size, norm_type, output):
    '''
[Graph] Creates a Canny Edge Detection Node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param hyst: [in] The double threshold for hysteresis. The threshold data_type shall be either *VX_TYPE_UINT8*  or *VX_TYPE_INT16*. The *VX_THRESHOLD_TRUE_VALUE* and *VX_THRESHOLD_FALSE_VALUE*  of *vx_threshold* are ignored.
 :param gradient_size: [in] The size of the Sobel filter window, must support at least 3, 5, and 7.
 :param norm_type: [in] A flag indicating the norm used to compute the gradient, *VX_NORM_L1* or VX_NORM_L2.
 :param output: [out] The output image in *VX_DF_IMAGE_U8* format with values either  *VX_THRESHOLD_TRUE_VALUE* or *VX_THRESHOLD_FALSE_VALUE* from hyst parameter.
 :ingroup: group_vision_function_canny
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxCannyEdgeDetectorNode(graph, input, hyst, gradient_size, norm_type, output)
    
def WarpAffineNode(graph, input, matrix, type, output):
    '''
[Graph] Creates an Affine Warp Node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param matrix: [in] The affine matrix. Must be 2x3 of type VX_TYPE_FLOAT32.
 :param type: [in] The interpolation type from *vx_interpolation_type_e*. *VX_INTERPOLATION_AREA* is not supported.
 :param output: [out] The output *VX_DF_IMAGE_U8* image.
 :ingroup: group_vision_function_warp_affine
 :note: The border modes *VX_NODE_BORDER* value *VX_BORDER_UNDEFINED* and *VX_BORDER_CONSTANT* are supported.
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxWarpAffineNode(graph, input, matrix, type, output)
    
def WarpPerspectiveNode(graph, input, matrix, type, output):
    '''
[Graph] Creates a Perspective Warp Node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param matrix: [in] The perspective matrix. Must be 3x3 of type *VX_TYPE_FLOAT32*.
 :param type: [in] The interpolation type from *vx_interpolation_type_e*. *VX_INTERPOLATION_AREA* is not supported.
 :param output: [out] The output *VX_DF_IMAGE_U8* image.
 :ingroup: group_vision_function_warp_perspective
 :note: The border modes *VX_NODE_BORDER* value *VX_BORDER_UNDEFINED* and  *VX_BORDER_CONSTANT* are supported.
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxWarpPerspectiveNode(graph, input, matrix, type, output)
    
def HarrisCornersNode(graph, input, strength_thresh, min_distance, sensitivity, gradient_size, block_size, corners, num_corners):
    '''
[Graph] Creates a Harris Corners Node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param strength_thresh: [in] The *VX_TYPE_FLOAT32* minimum threshold with which to eliminate Harris Corner scores (computed using the normalized Sobel kernel).
 :param min_distance: [in] The *VX_TYPE_FLOAT32* radial Euclidean distance for non-maximum suppression.
 :param sensitivity: [in] The *VX_TYPE_FLOAT32* scalar sensitivity threshold  :f$: k \f$ from the Harris-Stephens equation.
 :param gradient_size: [in] The gradient window size to use on the input. The implementation must support at least 3, 5, and 7.
 :param block_size: [in] The block window size used to compute the Harris Corner score. The implementation must support at least 3, 5, and 7.
 :param corners: [out] The array of *VX_TYPE_KEYPOINT* objects. The order of the keypoints in this array is implementation dependent.
 :param num_corners: [out] The total number of detected corners in image (optional). Use a VX_TYPE_SIZE scalar.
 :ingroup: group_vision_function_harris
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxHarrisCornersNode(graph, input, strength_thresh, min_distance, sensitivity, gradient_size, block_size, corners, num_corners)
    
def FastCornersNode(graph, input, strength_thresh, nonmax_suppression, corners, num_corners):
    '''
[Graph] Creates a FAST Corners Node.
 :param graph: [in] The reference to the graph.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param strength_thresh: [in] Threshold on difference between intensity of the central pixel and pixels on Bresenham's circle of radius 3 (*VX_TYPE_FLOAT32* scalar).
 :param nonmax_suppression: [in] If true, non-maximum suppression is applied to detected corners before being placed in the *vx_array* of *VX_TYPE_KEYPOINT* objects.
 :param corners: [out] Output corner *vx_array* of *VX_TYPE_KEYPOINT*. The order of the  keypoints in this array is implementation dependent.
 :param num_corners: [out] The total number of detected corners in image (optional). Use a VX_TYPE_SIZE scalar.
 :ingroup: group_vision_function_fast
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxFastCornersNode(graph, input, strength_thresh, nonmax_suppression, corners, num_corners)
    
def OpticalFlowPyrLKNode(graph, old_images, new_images, old_points, new_points_estimates, new_points, termination, epsilon, num_iterations, use_initial_estimate, window_dimension):
    '''
[Graph] Creates a Lucas Kanade Tracking Node.
 :param graph: [in] The reference to the graph.
 :param old_images: [in] Input of first (old) image pyramid in *VX_DF_IMAGE_U8*.
 :param new_images: [in] Input of destination (new) image pyramid *VX_DF_IMAGE_U8*.
 :param old_points: [in] An array of key points in a *vx_array* of *VX_TYPE_KEYPOINT*; those key points are defined at the *old_images* high resolution pyramid.
 :param new_points_estimates: [in] An array of estimation on what is the output key points in a *vx_array* of *VX_TYPE_KEYPOINT*; those keypoints are defined at the *new_images* high resolution pyramid.
 :param new_points: [out] An output array of key points in a *vx_array* of *VX_TYPE_KEYPOINT*; those key points are defined at the *new_images* high resolution pyramid.
 :param termination: [in] The termination can be *VX_TERM_CRITERIA_ITERATIONS* or *VX_TERM_CRITERIA_EPSILON* or *VX_TERM_CRITERIA_BOTH*.
 :param epsilon: [in] The *vx_float32* error for terminating the algorithm.
 :param num_iterations: [in] The number of iterations. Use a *VX_TYPE_UINT32* scalar.
 :param use_initial_estimate: [in] Use a *VX_TYPE_BOOL* scalar.
 :param window_dimension: [in] The size of the window on which to perform the algorithm. See  *VX_CONTEXT_OPTICAL_FLOW_MAX_WINDOW_DIMENSION*
 :ingroup: group_vision_function_opticalflowpyrlk
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxOpticalFlowPyrLKNode(graph, old_images, new_images, old_points, new_points_estimates, new_points, termination, epsilon, num_iterations, use_initial_estimate, window_dimension)
    
def RemapNode(graph, input, table, policy, output):
    '''
[Graph] Creates a Remap Node.
 :param graph: [in] The reference to the graph that will contain the node.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param table: [in] The remap table object.
 :param policy: [in] An interpolation type from *vx_interpolation_type_e*. *VX_INTERPOLATION_AREA* is not supported.
 :param output: [out] The output *VX_DF_IMAGE_U8* image.
 :note: The border modes *VX_NODE_BORDER* value *VX_BORDER_UNDEFINED* and  *VX_BORDER_CONSTANT* are supported.
:return: A *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*  
 :ingroup: group_vision_function_remap  
    '''
    return lib.vxRemapNode(graph, input, table, policy, output)
    
def HalfScaleGaussianNode(graph, input, output, kernel_size):
    '''
[Graph] Performs a Gaussian Blur on an image then half-scales it. The interpolation mode used is nearest-neighbor.
 :details: The output image size is determined by:
\f[ W_{output} =  :frac{W_{input}: + 1}{2} \\ , H_{output} =  :frac{H_{input}: + 1}{2}
\f]
 :param graph: [in] The reference to the graph.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param output: [out] The output *VX_DF_IMAGE_U8* image.
 :param kernel_size: [in] The input size of the Gaussian filter. Supported values are 1, 3 and 5. 
 :ingroup: group_vision_function_scale_image
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*    
    '''
    return lib.vxHalfScaleGaussianNode(graph, input, output, kernel_size)
    