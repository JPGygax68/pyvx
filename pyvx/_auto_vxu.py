from pyvx.backend import lib, ffi

def ColorConvert(context, input, output):
    '''
[Immediate] Invokes an immediate Color Conversion.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image.
 :param output: [out] The output image.
 :ingroup: group_vision_function_colorconvert
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuColorConvert(context, input, output)
    
def ChannelExtract(context, input, channel, output):
    '''
[Immediate] Invokes an immediate Channel Extract.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image. Must be one of the defined *vx_df_image_e* multi-channel formats.
 :param channel: [in] The *vx_channel_e* enumeration to extract.
 :param output: [out] The output image. Must be *VX_DF_IMAGE_U8*.
 :ingroup: group_vision_function_channelextract
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuChannelExtract(context, input, channel, output)
    
def ChannelCombine(context, plane0, plane1, plane2, plane3, output):
    '''
[Immediate] Invokes an immediate Channel Combine.
 :param context: [in] The reference to the overall context.
 :param plane0: [in] The plane that forms channel 0. Must be *VX_DF_IMAGE_U8*.
 :param plane1: [in] The plane that forms channel 1. Must be *VX_DF_IMAGE_U8*.
 :param plane2: [in] [optional] The plane that forms channel 2. Must be *VX_DF_IMAGE_U8*.
 :param plane3: [in] [optional] The plane that forms channel 3. Must be *VX_DF_IMAGE_U8*.
 :param output: [out] The output image.
 :ingroup: group_vision_function_channelcombine
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuChannelCombine(context, plane0, plane1, plane2, plane3, output)
    
def Sobel3x3(context, input, output_x, output_y):
    '''
[Immediate] Invokes an immediate Sobel 3x3.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param output_x: [out] [optional] The output gradient in the x direction in *VX_DF_IMAGE_S16*.
 :param output_y: [out] [optional] The output gradient in the y direction in *VX_DF_IMAGE_S16*.
 :ingroup: group_vision_function_sobel3x3
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuSobel3x3(context, input, output_x, output_y)
    
def Magnitude(context, grad_x, grad_y, mag):
    '''
[Immediate] Invokes an immediate Magnitude.
 :param context: [in] The reference to the overall context.
 :param grad_x: [in] The input x image. This must be in *VX_DF_IMAGE_S16* format.
 :param grad_y: [in] The input y image. This must be in *VX_DF_IMAGE_S16* format.
 :param mag: [out] The magnitude image. This will be in *VX_DF_IMAGE_S16* format.
 :ingroup: group_vision_function_magnitude
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuMagnitude(context, grad_x, grad_y, mag)
    
def Phase(context, grad_x, grad_y, orientation):
    '''
[Immediate] Invokes an immediate Phase.
 :param context: [in] The reference to the overall context.
 :param grad_x: [in] The input x image. This must be in *VX_DF_IMAGE_S16* format.
 :param grad_y: [in] The input y image. This must be in *VX_DF_IMAGE_S16* format.
 :param orientation: [out] The phase image. This will be in *VX_DF_IMAGE_U8* format.
 :ingroup: group_vision_function_phase
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuPhase(context, grad_x, grad_y, orientation)
    
def ScaleImage(context, src, dst, type):
    '''
[Immediate] Scales an input image to an output image.
 :param context: [in] The reference to the overall context.
 :param src: [in] The source image of type *VX_DF_IMAGE_U8*.
 :param dst: [out] The destintation image of type *VX_DF_IMAGE_U8*.
 :param type: [in] The interpolation type.  :see: vx_interpolation_type_e.
 :ingroup: group_vision_function_scale_image
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuScaleImage(context, src, dst, type)
    
def TableLookup(context, input, lut, output):
    '''
[Immediate] Processes the image through the LUT.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
 :param lut: [in] The LUT which is of type *VX_TYPE_UINT8* or *VX_TYPE_INT16*.
 :param output: [out] The output image of type *VX_DF_IMAGE_U8*
 :ingroup: group_vision_function_lut
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuTableLookup(context, input, lut, output)
    
def Histogram(context, input, distribution):
    '''
[Immediate] Generates a distribution from an image.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image in *VX_DF_IMAGE_U8*
 :param distribution: [out] The output distribution.
 :ingroup: group_vision_function_histogram
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuHistogram(context, input, distribution)
    
def EqualizeHist(context, input, output):
    '''
[Immediate] Equalizes the Histogram of a grayscale image.
 :param context: [in] The reference to the overall context.
 :param input: [in] The grayscale input image in *VX_DF_IMAGE_U8*
 :param output: [out] The grayscale output image of type *VX_DF_IMAGE_U8* with equalized brightness and contrast.
 :ingroup: group_vision_function_equalize_hist
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuEqualizeHist(context, input, output)
    
def AbsDiff(context, in1, in2, out):
    '''
[Immediate] Computes the absolute difference between two images.
 :param context: [in] The reference to the overall context.
 :param in1: [in] An input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
 :param in2: [in] An input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
 :param out: [out] The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
 :ingroup: group_vision_function_absdiff
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuAbsDiff(context, in1, in2, out)
    
def MeanStdDev(context, input, mean, stddev):
    '''
[Immediate] Computes the mean value and standard deviation.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image. *VX_DF_IMAGE_U8* is supported.
 :param mean: [out] The average pixel value.
 :param stddev: [out] The standard deviation of the pixel values.
 :ingroup: group_vision_function_meanstddev
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuMeanStdDev(context, input, mean, stddev)
    
def Threshold(context, input, thresh, output):
    '''
[Immediate] Threshold's an input image and produces a *VX_DF_IMAGE_U8*  * boolean image.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image. *VX_DF_IMAGE_U8* is supported.
 :param thresh: [in] The thresholding object that defines the parameters of the operation. The *VX_THRESHOLD_TRUE_VALUE* and *VX_THRESHOLD_FALSE_VALUE* are taken into account.
 :param output: [out] The output Boolean image with values either *VX_THRESHOLD_TRUE_VALUE* or  *VX_THRESHOLD_FALSE_VALUE* from the  :e: thresh parameter.
 :ingroup: group_vision_function_threshold
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuThreshold(context, input, thresh, output)
    
def IntegralImage(context, input, output):
    '''
[Immediate] Computes the integral image of the input.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param output: [out] The output image in *VX_DF_IMAGE_U32* format.
 :ingroup: group_vision_function_integral_image
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuIntegralImage(context, input, output)
    
def Erode3x3(context, input, output):
    '''
[Immediate] Erodes an image by a 3x3 window.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param output: [out] The output image in *VX_DF_IMAGE_U8* format.
 :ingroup: group_vision_function_erode_image
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuErode3x3(context, input, output)
    
def Dilate3x3(context, input, output):
    '''
[Immediate] Dilates an image by a 3x3 window.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param output: [out] The output image in *VX_DF_IMAGE_U8* format.
 :ingroup: group_vision_function_dilate_image
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuDilate3x3(context, input, output)
    
def Median3x3(context, input, output):
    '''
[Immediate] Computes a median filter on the image by a 3x3 window.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param output: [out] The output image in *VX_DF_IMAGE_U8* format.
 :ingroup: group_vision_function_median_image
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuMedian3x3(context, input, output)
    
def Box3x3(context, input, output):
    '''
[Immediate] Computes a box filter on the image by a 3x3 window.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param output: [out] The output image in *VX_DF_IMAGE_U8* format.
 :ingroup: group_vision_function_box_image
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuBox3x3(context, input, output)
    
def Gaussian3x3(context, input, output):
    '''
[Immediate] Computes a gaussian filter on the image by a 3x3 window.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param output: [out] The output image in *VX_DF_IMAGE_U8* format.
 :ingroup: group_vision_function_gaussian_image
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuGaussian3x3(context, input, output)
    
def NonLinearFilter(context, function, input, mask, output):
    '''
[Immediate] Creates a Non-linear Filter Node.
 :param context: [in] The reference to the overall context.
 :param function: [in] The non-linear filter function. See *vx_non_linear_filter_e*.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param mask: [in] The mask to be applied to the Non-linear function. *VX_MATRIX_ORIGIN* attribute is used  to place the mask appropriately when computing the resulting image. See *vxCreateMatrixFromPattern*.  
 :param output: [out] The output image in *VX_DF_IMAGE_U8* format.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.
 :ingroup: group_vision_function_nonlinear_filter  
    '''
    return lib.vxuNonLinearFilter(context, function, input, mask, output)
    
def Convolve(context, input, conv, output):
    '''
[Immediate] Computes a convolution on the input image with the supplied matrix.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param conv: [in] The *vx_int16* convolution matrix.
 :param output: [out] The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
 :ingroup: group_vision_function_custom_convolution
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuConvolve(context, input, conv, output)
    
def GaussianPyramid(context, input, gaussian):
    '''
[Immediate] Computes a Gaussian pyramid from an input image.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image in *VX_DF_IMAGE_U8*
 :param gaussian: [out] The Gaussian pyramid with *VX_DF_IMAGE_U8* to construct.
 :ingroup: group_vision_function_gaussian_pyramid
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuGaussianPyramid(context, input, gaussian)
    
def LaplacianPyramid(context, input, laplacian, output):
    '''
[Immediate] Computes a Laplacian pyramid from an input image.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* format.
 :param laplacian: [out] The Laplacian pyramid with *VX_DF_IMAGE_S16* to construct.
 :param output: [out] The lowest resolution image of type *VX_DF_IMAGE_S16* necessary to reconstruct the input image from the pyramid.
 :ingroup: group_vision_function_laplacian_pyramid
 :see: group_pyramid
:return: A *vx_status* enumeration.
:retval: VX_SUCCESS Success.
:retval: * An error occured. See *vx_status_e*  
    '''
    return lib.vxuLaplacianPyramid(context, input, laplacian, output)
    
def LaplacianReconstruct(context, laplacian, input, output):
    '''
[Immediate] Reconstructs an image from a Laplacian Image pyramid.
 :param context: [in] The reference to the overall context.
 :param laplacian: [in] The Laplacian pyramid with *VX_DF_IMAGE_S16* format.
 :param input: [in] The lowest resolution image of type *VX_DF_IMAGE_S16* for the Laplacian pyramid
 :param output: [out] The output image of type *VX_DF_IMAGE_U8* with the highest possible resolution reconstructed from the Laplacian pyramid.
 :ingroup: group_vision_function_laplacian_reconstruct
 :see: group_pyramid
:return: A *vx_status* enumeration.
:retval: VX_SUCCESS Success.
:retval: * An error occured. See *vx_status_e*  
    '''
    return lib.vxuLaplacianReconstruct(context, laplacian, input, output)
    
def AccumulateImage(context, input, accum):
    '''
[Immediate] Computes an accumulation.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param accum: [in,out] The accumulation image in *VX_DF_IMAGE_S16*
 :ingroup: group_vision_function_accumulate
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuAccumulateImage(context, input, accum)
    
def AccumulateWeightedImage(context, input, alpha, accum):
    '''
[Immediate] Computes a weighted accumulation.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param alpha: [in] A *VX_TYPE_FLOAT32* type, the input value with the range  :f$: 0.0 \le \alpha \le 1.0 \f$.
 :param accum: [in,out] The *VX_DF_IMAGE_U8* accumulation image.
 :ingroup: group_vision_function_accumulate_weighted
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuAccumulateWeightedImage(context, input, alpha, accum)
    
def AccumulateSquareImage(context, input, shift, accum):
    '''
[Immediate] Computes a squared accumulation.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param shift: [in] A *VX_TYPE_UINT32* type, the input value with the range  :f$: 0 \le shift \le 15 \f$.
 :param accum: [in,out] The accumulation image in *VX_DF_IMAGE_S16*
 :ingroup: group_vision_function_accumulate_square
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuAccumulateSquareImage(context, input, shift, accum)
    
def MinMaxLoc(context, input, minVal, maxVal, minLoc, maxLoc, minCount, maxCount):
    '''
[Immediate] Computes the minimum and maximum values of the image.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
 :param minVal: [out] The minimum value in the image, which corresponds to the type of the input.
 :param maxVal: [out] The maximum value in the image, which corresponds to the type of the input.
 :param minLoc: [out] The minimum *VX_TYPE_COORDINATES2D* locations (optional). If the input image has several minimums, the kernel will return up to the capacity of the array.
 :param maxLoc: [out] The maximum *VX_TYPE_COORDINATES2D* locations (optional). If the input image has several maximums, the kernel will return up to the capacity of the array.
 :param minCount: [out] The total number of detected minimums in image (optional). Use a *VX_TYPE_UINT32* scalar.
 :param maxCount: [out] The total number of detected maximums in image (optional). Use a *VX_TYPE_UINT32* scalar.
 :ingroup: group_vision_function_minmaxloc
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuMinMaxLoc(context, input, minVal, maxVal, minLoc, maxLoc, minCount, maxCount)
    
def ConvertDepth(context, input, output, policy, shift):
    '''
[Immediate] Converts the input images bit-depth into the output image.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input image.
 :param output: [out] The output image.
 :param policy: [in] A *VX_TYPE_ENUM* of the *vx_convert_policy_e* enumeration.
 :param shift: [in] A scalar containing a *VX_TYPE_INT32* of the shift value.
 :ingroup: group_vision_function_convertdepth
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*..  
    '''
    return lib.vxuConvertDepth(context, input, output, policy, shift)
    
def CannyEdgeDetector(context, input, hyst, gradient_size, norm_type, output):
    '''
[Immediate] Computes Canny Edges on the input image into the output image.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param hyst: [in] The double threshold for hysteresis. The threshold data_type shall be either *VX_TYPE_UINT8*  or *VX_TYPE_INT16*. The *VX_THRESHOLD_TRUE_VALUE* and *VX_THRESHOLD_FALSE_VALUE*  of *vx_threshold* are ignored.
 :param gradient_size: [in] The size of the Sobel filter window, must support at least 3, 5 and 7.
 :param norm_type: [in] A flag indicating the norm used to compute the gradient, VX_NORM_L1 or VX_NORM_L2.
 :param output: [out] The output image in *VX_DF_IMAGE_U8* format with values either  *VX_THRESHOLD_TRUE_VALUE* or *VX_THRESHOLD_FALSE_VALUE* from hyst parameter.
 :ingroup: group_vision_function_canny
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuCannyEdgeDetector(context, input, hyst, gradient_size, norm_type, output)
    
def HalfScaleGaussian(context, input, output, kernel_size):
    '''
[Immediate] Performs a Gaussian Blur on an image then half-scales it. The interpolation mode used is nearest-neighbor.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param output: [out] The output *VX_DF_IMAGE_U8* image.
 :param kernel_size: [in] The input size of the Gaussian filter. Supported values are 1, 3 and 5.
 :ingroup: group_vision_function_scale_image
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuHalfScaleGaussian(context, input, output, kernel_size)
    
def And(context, in1, in2, out):
    '''
[Immediate] Computes the bitwise and between two images.
 :param context: [in] The reference to the overall context.
 :param in1: [in] A *VX_DF_IMAGE_U8* input image
 :param in2: [in] A *VX_DF_IMAGE_U8* input image
 :param out: [out] The *VX_DF_IMAGE_U8* output image.
 :ingroup: group_vision_function_and
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuAnd(context, in1, in2, out)
    
def Or(context, in1, in2, out):
    '''
[Immediate] Computes the bitwise inclusive-or between two images.
 :param context: [in] The reference to the overall context.
 :param in1: [in] A *VX_DF_IMAGE_U8* input image
 :param in2: [in] A *VX_DF_IMAGE_U8* input image
 :param out: [out] The *VX_DF_IMAGE_U8* output image.
 :ingroup: group_vision_function_or
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuOr(context, in1, in2, out)
    
def Xor(context, in1, in2, out):
    '''
[Immediate] Computes the bitwise exclusive-or between two images.
 :param context: [in] The reference to the overall context.
 :param in1: [in] A *VX_DF_IMAGE_U8* input image
 :param in2: [in] A *VX_DF_IMAGE_U8* input image
 :param out: [out] The *VX_DF_IMAGE_U8* output image.
 :ingroup: group_vision_function_xor
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuXor(context, in1, in2, out)
    
def Not(context, input, output):
    '''
[Immediate] Computes the bitwise not of an image.
 :param context: [in] The reference to the overall context.
 :param input: [in] The *VX_DF_IMAGE_U8* input image
 :param output: [out] The *VX_DF_IMAGE_U8* output image.
 :ingroup: group_vision_function_not
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuNot(context, input, output)
    
def Multiply(context, in1, in2, scale, overflow_policy, rounding_policy, out):
    '''
[Immediate] Performs elementwise multiplications on pixel values in the input images and a scale.
 :param context: [in] The reference to the overall context.
 :param in1: [in] A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* input image.
 :param in2: [in] A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* input image.
 :param scale: [in] A non-negative *VX_TYPE_FLOAT32* multiplied to each product before overflow handling.
 :param overflow_policy: [in] A *vx_convert_policy_e* enumeration.
 :param rounding_policy: [in] A *vx_round_policy_e* enumeration.
 :param out: [out] The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
 :ingroup: group_vision_function_mult
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuMultiply(context, in1, in2, scale, overflow_policy, rounding_policy, out)
    
def Add(context, in1, in2, policy, out):
    '''
[Immediate] Performs arithmetic addition on pixel values in the input images.
 :param context: [in] The reference to the overall context.
 :param in1: [in] A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* input image.
 :param in2: [in] A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* input image.
 :param policy: [in] A vx_convert_policy_e enumeration.
 :param out: [out] The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
 :ingroup: group_vision_function_add
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuAdd(context, in1, in2, policy, out)
    
def Subtract(context, in1, in2, policy, out):
    '''
[Immediate] Performs arithmetic subtraction on pixel values in the input images.
 :param context: [in] The reference to the overall context.
 :param in1: [in] A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* input image, the minuend.
 :param in2: [in] A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* input image, the subtrahend.
 :param policy: [in] A vx_convert_policy_e enumeration.
 :param out: [out] The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
 :ingroup: group_vision_function_sub
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuSubtract(context, in1, in2, policy, out)
    
def WarpAffine(context, input, matrix, type, output):
    '''
[Immediate] Performs an Affine warp on an image.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param matrix: [in] The affine matrix. Must be 2x3 of type VX_TYPE_FLOAT32.
 :param type: [in] The interpolation type from vx_interpolation_type_e.
VX_INTERPOLATION_AREA is not supported.
 :param output: [out] The output *VX_DF_IMAGE_U8* image.
 :ingroup: group_vision_function_warp_affine
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuWarpAffine(context, input, matrix, type, output)
    
def WarpPerspective(context, input, matrix, type, output):
    '''
[Immediate] Performs an Perspective warp on an image.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param matrix: [in] The perspective matrix. Must be 3x3 of type VX_TYPE_FLOAT32.
 :param type: [in] The interpolation type from vx_interpolation_type_e.
VX_INTERPOLATION_AREA is not supported.
 :param output: [out] The output *VX_DF_IMAGE_U8* image.
 :ingroup: group_vision_function_warp_perspective
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuWarpPerspective(context, input, matrix, type, output)
    
def HarrisCorners(context, input, strength_thresh, min_distance, sensitivity, gradient_size, block_size, corners, num_corners):
    '''
[Immediate] Computes the Harris Corners over an image and produces the array of scored points.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param strength_thresh: [in] The *VX_TYPE_FLOAT32* minimum threshold which to eliminate Harris Corner scores (computed using the normalized Sobel kernel).
 :param min_distance: [in] The *VX_TYPE_FLOAT32* radial Euclidean distance for non-maximum suppression.
 :param sensitivity: [in] The *VX_TYPE_FLOAT32* scalar sensitivity threshold  :f$: k \f$ from the Harris-Stephens equation.
 :param gradient_size: [in] The gradient window size to use on the input. The implementation must support at least 3, 5, and 7.
 :param block_size: [in] The block window size used to compute the harris corner score. The implementation must support at least 3, 5, and 7.
 :param corners: [out] The array of *VX_TYPE_KEYPOINT* structs. The order of the keypoints in this array is implementation dependent.
 :param num_corners: [out] The total number of detected corners in image (optional). Use a VX_TYPE_SIZE scalar
 :ingroup: group_vision_function_harris
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuHarrisCorners(context, input, strength_thresh, min_distance, sensitivity, gradient_size, block_size, corners, num_corners)
    
def FastCorners(context, input, strength_thresh, nonmax_suppression, corners, num_corners):
    '''
[Immediate] Computes corners on an image using FAST algorithm and produces the array of feature points.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param strength_thresh: [in] Threshold on difference between intensity of the central pixel and pixels on Bresenham's circle of radius 3 (*VX_TYPE_FLOAT32* scalar)
 :param nonmax_suppression: [in] If true, non-maximum suppression is applied to detected corners before being places in the *vx_array* of *VX_TYPE_KEYPOINT* structs.
 :param corners: [out] Output corner *vx_array* of *VX_TYPE_KEYPOINT*. The order of the keypoints in this array is implementation dependent.
 :param num_corners: [out] The total number of detected corners in image (optional). Use a VX_TYPE_SIZE scalar.
 :ingroup: group_vision_function_fast
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: *          An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuFastCorners(context, input, strength_thresh, nonmax_suppression, corners, num_corners)
    
def OpticalFlowPyrLK(context, old_images, new_images, old_points, new_points_estimates, new_points, termination, epsilon, num_iterations, use_initial_estimate, window_dimension):
    '''
[Immediate] Computes an optical flow on two images.
 :param context: [in] The reference to the overall context.
 :param old_images: [in] Input of first (old) image pyramid in *VX_DF_IMAGE_U8*.
 :param new_images: [in] Input of destination (new) image pyramid in *VX_DF_IMAGE_U8*
 :param old_points: [in] an array of key points in a vx_array of *VX_TYPE_KEYPOINT* those key points are defined at the old_images high resolution pyramid
 :param new_points_estimates: [in] an array of estimation on what is the output key points in a *vx_array* of *VX_TYPE_KEYPOINT* those keypoints are defined at the new_images high resolution pyramid
 :param new_points: [out] an output array of key points in a *vx_array* of *VX_TYPE_KEYPOINT* those key points are defined at the new_images high resolution pyramid
 :param termination: [in] termination can be *VX_TERM_CRITERIA_ITERATIONS* or *VX_TERM_CRITERIA_EPSILON* or *VX_TERM_CRITERIA_BOTH*
 :param epsilon: [in] is the *vx_float32* error for terminating the algorithm
 :param num_iterations: [in] is the number of iterations. Use a *VX_TYPE_UINT32* scalar.
 :param use_initial_estimate: [in] Can be set to either *vx_false_e* or *vx_true_e*.
 :param window_dimension: [in] The size of the window on which to perform the algorithm. See  *VX_CONTEXT_OPTICAL_FLOW_MAX_WINDOW_DIMENSION* *  :ingroup: group_vision_function_opticalflowpyrlk
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval: * An error occurred. See *vx_status_e*.  
    '''
    return lib.vxuOpticalFlowPyrLK(context, old_images, new_images, old_points, new_points_estimates, new_points, termination, epsilon, num_iterations, use_initial_estimate, window_dimension)
    
def Remap(context, input, table, policy, output):
    '''
[Immediate] Remaps an output image from an input image.
 :param context: [in] The reference to the overall context.
 :param input: [in] The input *VX_DF_IMAGE_U8* image.
 :param table: [in] The remap table object.
 :param policy: [in] The interpolation policy from vx_interpolation_type_e.
VX_INTERPOLATION_AREA is not supported.
 :param output: [out] The output *VX_DF_IMAGE_U8* image.
:return: A *vx_status_e* enumeration.
 :ingroup: group_vision_function_remap  
    '''
    return lib.vxuRemap(context, input, table, policy, output)
    