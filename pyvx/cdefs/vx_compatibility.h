/*
 * Copyright (c) 2012-2016 The Khronos Group Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and/or associated documentation files (the
 * "Materials"), to deal in the Materials without restriction, including
 * without limitation the rights to use, copy, modify, merge, publish,
 * distribute, sublicense, and/or sell copies of the Materials, and to
 * permit persons to whom the Materials are furnished to do so, subject to
 * the following conditions:
 *
 * The above copyright notice and this permission notice shall be included
 * in all copies or substantial portions of the Materials.
 *
 * MODIFICATIONS TO THIS FILE MAY MEAN IT NO LONGER ACCURATELY REFLECTS
 * KHRONOS STANDARDS. THE UNMODIFIED, NORMATIVE VERSIONS OF KHRONOS
 * SPECIFICATIONS AND HEADER INFORMATION ARE LOCATED AT
 *    https://www.khronos.org/registry/
 *
 * THE MATERIALS ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 * IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
 * CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
 * TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
 * MATERIALS OR THE USE OR OTHER DEALINGS IN THE MATERIALS.
 */

#ifndef VX_1_0_1_NAMING_COMPATIBILITY
#define VX_1_0_1_NAMING_COMPATIBILITY

/**
 * \file
 * \brief OpenVX Deprecated API
 */

/**
 * \ingroup nvx_deprecated
 * \brief The border mode list.
 * \deprecated Use \ref vx_border_e instead.
 */
#define vx_border_mode_e           vx_border_e

/**
 * \ingroup nvx_deprecated
 * \brief The unsupported border mode policy list.
 * \deprecated Use \ref vx_border_policy_e instead.
 */
#define vx_border_mode_policy_e    vx_border_policy_e

/**
 * \ingroup nvx_deprecated
 * \brief The border mode behavior of a node that supports borders.
 * \deprecated Use \ref vx_border_t instead.
 */
#define _vx_border_mode_t          _vx_border_t

/**
 * \ingroup nvx_deprecated
 * \brief The border mode behavior of a node that supports borders.
 * \deprecated Use \ref vx_border_t instead.
 */
#define vx_border_mode_t           vx_border_t

/**
 * \ingroup nvx_deprecated
 * \brief The border mode list.
 * \deprecated Use \ref VX_ENUM_BORDER instead.
 */
#define VX_ENUM_BORDER_MODE         VX_ENUM_BORDER

/**
 * \ingroup nvx_deprecated
 * \brief No defined border mode behavior is given.
 * \deprecated Use \ref VX_BORDER_UNDEFINED instead.
 */
#define VX_BORDER_MODE_UNDEFINED    VX_BORDER_UNDEFINED

/**
 * \ingroup nvx_deprecated
 * \brief For nodes that support this behavior, a constant value is
 *        \e filled-in when accessing out-of-bounds pixels.
 * \deprecated Use \ref VX_BORDER_CONSTANT instead.
 */
#define VX_BORDER_MODE_CONSTANT     VX_BORDER_CONSTANT

/**
 * \ingroup nvx_deprecated
 * \brief For nodes that support this behavior, a replication of the nearest
 *        edge pixels value is given for out-of-bounds pixels.
 * \deprecated Use \ref VX_BORDER_REPLICATE instead.
 */
#define VX_BORDER_MODE_REPLICATE    VX_BORDER_REPLICATE

/**
 * \ingroup nvx_deprecated
 * \brief Unsupported Border Mode Policy List.
 * \deprecated Use \ref VX_ENUM_BORDER_POLICY instead.
 */
#define VX_ENUM_BORDER_MODE_POLICY       VX_ENUM_BORDER_POLICY

/**
 * \ingroup nvx_deprecated
 * \brief Use VX_BORDER_UNDEFINED instead of unsupported border modes.
 * \deprecated Use \ref VX_BORDER_POLICY_DEFAULT_TO_UNDEFINED instead.
 */
#define VX_BORDER_MODE_UNSUPPORTED_POLICY_DEFAULT_TO_UNDEFINED  VX_BORDER_POLICY_DEFAULT_TO_UNDEFINED

/**
 * \ingroup nvx_deprecated
 * \brief Return VX_ERROR_NOT_SUPPORTED for unsupported border modes.
 * \deprecated Use \ref VX_BORDER_POLICY_RETURN_ERROR instead.
 */
#define VX_BORDER_MODE_UNSUPPORTED_POLICY_RETURN_ERROR          VX_BORDER_POLICY_RETURN_ERROR

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief Queries the unique vendor ID.
 * \deprecated Use \ref VX_CONTEXT_VENDOR_ID instead.
 */
#define VX_CONTEXT_ATTRIBUTE_VENDOR_ID                          VX_CONTEXT_VENDOR_ID

/**
 * \ingroup nvx_deprecated
 * \brief Queries the OpenVX Version Number.
 * \deprecated Use \ref VX_CONTEXT_VERSION instead.
 */
#define VX_CONTEXT_ATTRIBUTE_VERSION                            VX_CONTEXT_VERSION

/**
 * \ingroup nvx_deprecated
 * \brief Queries the context for the number of \e unique kernels.
 * \deprecated Use \ref VX_CONTEXT_UNIQUE_KERNELS instead.
 */
#define VX_CONTEXT_ATTRIBUTE_UNIQUE_KERNELS                     VX_CONTEXT_UNIQUE_KERNELS

/**
 * \ingroup nvx_deprecated
 * \brief Queries the context for the number of active modules.
 * \deprecated Use \ref VX_CONTEXT_MODULES instead.
 */
#define VX_CONTEXT_ATTRIBUTE_MODULES                            VX_CONTEXT_MODULES

/**
 * \ingroup nvx_deprecated
 * \brief Queries the context for the number of active references.
 * \deprecated Use \ref VX_CONTEXT_REFERENCES instead.
 */
#define VX_CONTEXT_ATTRIBUTE_REFERENCES                         VX_CONTEXT_REFERENCES

/**
 * \ingroup nvx_deprecated
 * \brief Queries the context for it's implementation name.
 * \deprecated Use \ref VX_CONTEXT_IMPLEMENTATION instead.
 */
#define VX_CONTEXT_ATTRIBUTE_IMPLEMENTATION                     VX_CONTEXT_IMPLEMENTATION

/**
 * \ingroup nvx_deprecated
 * \brief Queries the number of bytes in the extensions string.
 * \deprecated Use \ref VX_CONTEXT_IMPLEMENTATION instead.
 */
#define VX_CONTEXT_ATTRIBUTE_EXTENSIONS_SIZE                    VX_CONTEXT_EXTENSIONS_SIZE

/**
 * \ingroup nvx_deprecated
 * \brief Retrieves the extensions string.
 * \deprecated Use \ref VX_CONTEXT_EXTENSIONS instead.
 */
#define VX_CONTEXT_ATTRIBUTE_EXTENSIONS                         VX_CONTEXT_EXTENSIONS

/**
 * \ingroup nvx_deprecated
 * \brief The maximum width or height of a convolution matrix.
 * \deprecated Use \ref VX_CONTEXT_CONVOLUTION_MAX_DIMENSION instead.
 */
#define VX_CONTEXT_ATTRIBUTE_CONVOLUTION_MAXIMUM_DIMENSION      VX_CONTEXT_CONVOLUTION_MAX_DIMENSION

/**
 * \ingroup nvx_deprecated
 * \brief The maximum window dimension of the OpticalFlowPyrLK kernel.
 * \deprecated Use \ref VX_CONTEXT_OPTICAL_FLOW_MAX_WINDOW_DIMENSION instead.
 */
#define VX_CONTEXT_ATTRIBUTE_OPTICAL_FLOW_WINDOW_MAXIMUM_DIMENSION      VX_CONTEXT_OPTICAL_FLOW_MAX_WINDOW_DIMENSION

/**
 * \ingroup nvx_deprecated
 * \brief The border mode for immediate mode functions.
 * \deprecated Use \ref VX_CONTEXT_IMMEDIATE_BORDER instead.
 */
#define VX_CONTEXT_ATTRIBUTE_IMMEDIATE_BORDER_MODE                      VX_CONTEXT_IMMEDIATE_BORDER

/**
 * \ingroup nvx_deprecated
 * \brief Returns the table of all unique the kernels that exist in the context.
 * \deprecated Use \ref VX_CONTEXT_UNIQUE_KERNEL_TABLE instead.
 */
#define VX_CONTEXT_ATTRIBUTE_UNIQUE_KERNEL_TABLE                        VX_CONTEXT_UNIQUE_KERNEL_TABLE

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief Queries a kernel for the number of parameters the kernel supports.
 * \deprecated Use \ref VX_KERNEL_PARAMETERS instead.
 */
#define VX_KERNEL_ATTRIBUTE_PARAMETERS      VX_KERNEL_PARAMETERS

/**
 * \ingroup nvx_deprecated
 * \brief Queries the name of the kernel.
 * \deprecated Use \ref VX_KERNEL_NAME instead.
 */
#define VX_KERNEL_ATTRIBUTE_NAME            VX_KERNEL_NAME

/**
 * \ingroup nvx_deprecated
 * \brief Queries the enum of the kernel.
 * \deprecated Use \ref VX_KERNEL_ENUM instead.
 */
#define VX_KERNEL_ATTRIBUTE_ENUM            VX_KERNEL_ENUM

/**
 * \ingroup nvx_deprecated
 * \brief The local data area allocated with each kernel when it becomes a node.
 * \deprecated Use \ref VX_KERNEL_LOCAL_DATA_SIZE instead.
 */
#define VX_KERNEL_ATTRIBUTE_LOCAL_DATA_SIZE VX_KERNEL_LOCAL_DATA_SIZE

/*
#define VX_KERNEL_ATTRIBUTE_LOCAL_DATA_PTR  (VX_ATTRIBUTE_BASE(VX_ID_KHRONOS, VX_TYPE_KERNEL) + 0x4)
*/

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief Queries the status of node execution.
 * \deprecated Use \ref VX_NODE_STATUS instead.
 */
#define VX_NODE_ATTRIBUTE_STATUS            VX_NODE_STATUS

/**
 * \ingroup nvx_deprecated
 * \brief Queries the performance of the node execution.
 * \deprecated Use \ref VX_NODE_PERFORMANCE instead.
 */
#define VX_NODE_ATTRIBUTE_PERFORMANCE       VX_NODE_PERFORMANCE

/**
 * \ingroup nvx_deprecated
 * \brief Gets or sets the border mode of the node.
 * \deprecated Use \ref VX_NODE_BORDER instead.
 */
#define VX_NODE_ATTRIBUTE_BORDER_MODE       VX_NODE_BORDER

/**
 * \ingroup nvx_deprecated
 * \brief Indicates the size of the kernel local memory area.
 * \deprecated Use \ref VX_NODE_LOCAL_DATA_SIZE instead.
 */
#define VX_NODE_ATTRIBUTE_LOCAL_DATA_SIZE   VX_NODE_LOCAL_DATA_SIZE

/**
 * \ingroup nvx_deprecated
 * \brief Indicates the pointer kernel local memory area.
 * \deprecated Use \ref VX_NODE_LOCAL_DATA_SIZE instead.
 */
#define VX_NODE_ATTRIBUTE_LOCAL_DATA_PTR    VX_NODE_LOCAL_DATA_PTR

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief Queries a parameter for its index value on the kernel with which it is associated.
 * \deprecated Use \ref VX_PARAMETER_INDEX instead.
 */
#define VX_PARAMETER_ATTRIBUTE_INDEX        VX_PARAMETER_INDEX

/**
 * \ingroup nvx_deprecated
 * \brief Queries a parameter for its direction value on the kernel with which it is associated.
 * \deprecated Use \ref VX_PARAMETER_DIRECTION instead.
 */
#define VX_PARAMETER_ATTRIBUTE_DIRECTION    VX_PARAMETER_DIRECTION

/**
 * \ingroup nvx_deprecated
 * \brief Queries a parameter for its type, \ref vx_type_e is returned.
 * \deprecated Use \ref VX_PARAMETER_TYPE instead.
 */
#define VX_PARAMETER_ATTRIBUTE_TYPE         VX_PARAMETER_TYPE

/**
 * \ingroup nvx_deprecated
 * \brief Queries a parameter for its state.
 * \deprecated Use \ref VX_PARAMETER_STATE instead.
 */
#define VX_PARAMETER_ATTRIBUTE_STATE        VX_PARAMETER_STATE

/**
 * \ingroup nvx_deprecated
 * \brief Use to extract the reference contained in the parameter.
 * \deprecated Use \ref VX_PARAMETER_REF instead.
 */
#define VX_PARAMETER_ATTRIBUTE_REF          VX_PARAMETER_REF

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief Queries an image for its width.
 * \deprecated Use \ref VX_IMAGE_WIDTH instead.
 */
#define VX_IMAGE_ATTRIBUTE_WIDTH            VX_IMAGE_WIDTH

/**
 * \ingroup nvx_deprecated
 * \brief Queries an image for its height.
 * \deprecated Use \ref VX_IMAGE_HEIGHT instead.
 */
#define VX_IMAGE_ATTRIBUTE_HEIGHT           VX_IMAGE_HEIGHT

/**
 * \ingroup nvx_deprecated
 * \brief Queries an image for its format.
 * \deprecated Use \ref VX_IMAGE_FORMAT instead.
 */
#define VX_IMAGE_ATTRIBUTE_FORMAT           VX_IMAGE_FORMAT

/**
 * \ingroup nvx_deprecated
 * \brief Queries an image for its number of planes.
 * \deprecated Use \ref VX_IMAGE_FORMAT instead.
 */
#define VX_IMAGE_ATTRIBUTE_PLANES           VX_IMAGE_PLANES

/**
 * \ingroup nvx_deprecated
 * \brief Queries an image for its color space (see \ref vx_color_space_e).
 * \deprecated Use \ref VX_IMAGE_SPACE instead.
 */
#define VX_IMAGE_ATTRIBUTE_SPACE            VX_IMAGE_SPACE

/**
 * \ingroup nvx_deprecated
 * \brief Queries an image for its channel range (see \ref vx_channel_range_e).
 * \deprecated Use \ref VX_IMAGE_RANGE instead.
 */
#define VX_IMAGE_ATTRIBUTE_RANGE            VX_IMAGE_RANGE

/**
 * \ingroup nvx_deprecated
 * \brief Queries an image for its total number of bytes.
 * \deprecated Use \ref VX_IMAGE_SIZE instead.
 */
#define VX_IMAGE_ATTRIBUTE_SIZE             VX_IMAGE_SIZE

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief Queries the type of atomic that is contained in the scalar.
 * \deprecated Use \ref VX_SCALAR_TYPE instead.
 */
#define VX_SCALAR_ATTRIBUTE_TYPE            VX_SCALAR_TYPE

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief Returns the number of nodes in a graph.
 * \deprecated Use \ref VX_GRAPH_NUMNODES instead.
 */
#define VX_GRAPH_ATTRIBUTE_NUMNODES         VX_GRAPH_NUMNODES

/**
 * \ingroup nvx_deprecated
 * \brief Returns the overall status of the graph.
 * \deprecated Use \ref VX_GRAPH_STATE instead.
 */
#define VX_GRAPH_ATTRIBUTE_STATUS           (VX_ATTRIBUTE_BASE(VX_ID_KHRONOS, VX_TYPE_GRAPH) + 0x1)

/**
 * \ingroup nvx_deprecated
 * \brief Returns the overall performance of the graph.
 * \deprecated Use \ref VX_GRAPH_PERFORMANCE instead.
 */
#define VX_GRAPH_ATTRIBUTE_PERFORMANCE      VX_GRAPH_PERFORMANCE

/**
 * \ingroup nvx_deprecated
 * \brief Returns the number of explicitly declared parameters on the graph.
 * \deprecated Use \ref VX_GRAPH_NUMPARAMETERS instead.
 */
#define VX_GRAPH_ATTRIBUTE_NUMPARAMETERS    VX_GRAPH_NUMPARAMETERS

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief Indicates the value type of the LUT.
 * \deprecated Use \ref VX_LUT_TYPE instead.
 */
#define VX_LUT_ATTRIBUTE_TYPE               VX_LUT_TYPE

/**
 * \ingroup nvx_deprecated
 * \brief Indicates the number of elements in the LUT.
 * \deprecated Use \ref VX_LUT_COUNT instead.
 */
#define VX_LUT_ATTRIBUTE_COUNT              VX_LUT_COUNT

/**
 * \ingroup nvx_deprecated
 * \brief Indicates the total size of the LUT in bytes.
 * \deprecated Use \ref VX_LUT_SIZE instead.
 */
#define VX_LUT_ATTRIBUTE_SIZE               VX_LUT_SIZE

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief Indicates the number of dimensions in the distribution.
 * \deprecated Use \ref VX_DISTRIBUTION_DIMENSIONS instead.
 */
#define VX_DISTRIBUTION_ATTRIBUTE_DIMENSIONS    VX_DISTRIBUTION_DIMENSIONS

/**
 * \ingroup nvx_deprecated
 * \brief Indicates the start of the values to use (inclusive).
 * \deprecated Use \ref VX_DISTRIBUTION_OFFSET instead.
 */
#define VX_DISTRIBUTION_ATTRIBUTE_OFFSET        VX_DISTRIBUTION_OFFSET

/**
 * \ingroup nvx_deprecated
 * \brief Indicates the total number of the consecutive values of the distribution interval.
 * \deprecated Use \ref VX_DISTRIBUTION_RANGE instead.
 */
#define VX_DISTRIBUTION_ATTRIBUTE_RANGE         VX_DISTRIBUTION_RANGE

/**
 * \ingroup nvx_deprecated
 * \brief Indicates the number of bins.
 * \deprecated Use \ref VX_DISTRIBUTION_BINS instead.
 */
#define VX_DISTRIBUTION_ATTRIBUTE_BINS          VX_DISTRIBUTION_BINS

/**
 * \ingroup nvx_deprecated
 * \brief Indicates the width of a bin.
 * \deprecated Use \ref VX_DISTRIBUTION_WINDOW instead.
 */
#define VX_DISTRIBUTION_ATTRIBUTE_WINDOW        VX_DISTRIBUTION_WINDOW

/**
 * \ingroup nvx_deprecated
 * \brief Indicates the total size of the distribution in bytes.
 * \deprecated Use \ref VX_DISTRIBUTION_SIZE instead.
 */
#define VX_DISTRIBUTION_ATTRIBUTE_SIZE          VX_DISTRIBUTION_SIZE

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief The value type of the threshold.
 * \deprecated Use \ref VX_THRESHOLD_TYPE instead.
 */
#define VX_THRESHOLD_ATTRIBUTE_TYPE             VX_THRESHOLD_TYPE

/**
 * \ingroup nvx_deprecated
 * \brief The value of the single threshold.
 * \deprecated Use \ref VX_THRESHOLD_THRESHOLD_VALUE instead.
 */
#define VX_THRESHOLD_ATTRIBUTE_THRESHOLD_VALUE  VX_THRESHOLD_THRESHOLD_VALUE

/**
 * \ingroup nvx_deprecated
 * \brief The value of the lower threshold.
 * \deprecated Use \ref VX_THRESHOLD_THRESHOLD_LOWER instead.
 */
#define VX_THRESHOLD_ATTRIBUTE_THRESHOLD_LOWER  VX_THRESHOLD_THRESHOLD_LOWER

/**
 * \ingroup nvx_deprecated
 * \brief The value of the higher threshold.
 * \deprecated Use \ref VX_THRESHOLD_THRESHOLD_UPPER instead.
 */
#define VX_THRESHOLD_ATTRIBUTE_THRESHOLD_UPPER  VX_THRESHOLD_THRESHOLD_UPPER

/**
 * \ingroup nvx_deprecated
 * \brief The value of the TRUE threshold (default value is 255).
 * \deprecated Use \ref VX_THRESHOLD_TRUE_VALUE instead.
 */
#define VX_THRESHOLD_ATTRIBUTE_TRUE_VALUE       VX_THRESHOLD_TRUE_VALUE

/**
 * \ingroup nvx_deprecated
 * \brief The value of the FALSE threshold (default value is 0).
 * \deprecated Use \ref VX_THRESHOLD_FALSE_VALUE instead.
 */
#define VX_THRESHOLD_ATTRIBUTE_FALSE_VALUE      VX_THRESHOLD_FALSE_VALUE

/**
 * \ingroup nvx_deprecated
 * \brief The data type of the threshold's value.
 * \deprecated Use \ref VX_THRESHOLD_DATA_TYPE instead.
 */
#define VX_THRESHOLD_ATTRIBUTE_DATA_TYPE        VX_THRESHOLD_DATA_TYPE

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief The value type of the matrix.
 * \deprecated Use \ref VX_MATRIX_TYPE instead.
 */
#define VX_MATRIX_ATTRIBUTE_TYPE            VX_MATRIX_TYPE

/**
 * \ingroup nvx_deprecated
 * \brief The M dimension of the matrix.
 * \deprecated Use \ref VX_MATRIX_ROWS instead.
 */
#define VX_MATRIX_ATTRIBUTE_ROWS            VX_MATRIX_ROWS

/**
 * \ingroup nvx_deprecated
 * \brief The N dimension of the matrix.
 * \deprecated Use \ref VX_MATRIX_COLUMNS instead.
 */
#define VX_MATRIX_ATTRIBUTE_COLUMNS         VX_MATRIX_COLUMNS

/**
 * \ingroup nvx_deprecated
 * \brief The total size of the matrix in bytes.
 * \deprecated Use \ref VX_MATRIX_SIZE instead.
 */
#define VX_MATRIX_ATTRIBUTE_SIZE            VX_MATRIX_SIZE

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief The number of rows of the convolution matrix.
 * \deprecated Use \ref VX_CONVOLUTION_ROWS instead.
 */
#define VX_CONVOLUTION_ATTRIBUTE_ROWS       VX_CONVOLUTION_ROWS

/**
 * \ingroup nvx_deprecated
 * \brief The number of columns of the convolution matrix.
 * \deprecated Use \ref VX_CONVOLUTION_COLUMNS instead.
 */
#define VX_CONVOLUTION_ATTRIBUTE_COLUMNS    VX_CONVOLUTION_COLUMNS

/**
 * \ingroup nvx_deprecated
 * \brief The scale of the convolution matrix.
 * \deprecated Use \ref VX_CONVOLUTION_SCALE instead.
 */
#define VX_CONVOLUTION_ATTRIBUTE_SCALE      VX_CONVOLUTION_SCALE

/**
 * \ingroup nvx_deprecated
 * \brief The total size of the convolution matrix in bytes.
 * \deprecated Use \ref VX_CONVOLUTION_SCALE instead.
 */
#define VX_CONVOLUTION_ATTRIBUTE_SIZE       VX_CONVOLUTION_SIZE

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief The number of levels of the pyramid.
 * \deprecated Use \ref VX_PYRAMID_LEVELS instead.
 */
#define VX_PYRAMID_ATTRIBUTE_LEVELS         VX_PYRAMID_LEVELS

/**
 * \ingroup nvx_deprecated
 * \brief The scale factor between each level of the pyramid.
 * \deprecated Use \ref VX_PYRAMID_SCALE instead.
 */
#define VX_PYRAMID_ATTRIBUTE_SCALE          VX_PYRAMID_SCALE

/**
 * \ingroup nvx_deprecated
 * \brief The width of the 0th image in pixels.
 * \deprecated Use \ref VX_PYRAMID_WIDTH instead.
 */
#define VX_PYRAMID_ATTRIBUTE_WIDTH          VX_PYRAMID_WIDTH

/**
 * \ingroup nvx_deprecated
 * \brief The height of the 0th image in pixels.
 * \deprecated Use \ref VX_PYRAMID_HEIGHT instead.
 */
#define VX_PYRAMID_ATTRIBUTE_HEIGHT         VX_PYRAMID_HEIGHT

/**
 * \ingroup nvx_deprecated
 * \brief The \ref vx_df_image_e format of the image.
 * \deprecated Use \ref VX_PYRAMID_FORMAT instead.
 */
#define VX_PYRAMID_ATTRIBUTE_FORMAT         VX_PYRAMID_FORMAT

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief The source width.
 * \deprecated Use \ref VX_REMAP_SOURCE_WIDTH instead.
 */
#define VX_REMAP_ATTRIBUTE_SOURCE_WIDTH         VX_REMAP_SOURCE_WIDTH

/**
 * \ingroup nvx_deprecated
 * \brief The source height.
 * \deprecated Use \ref VX_REMAP_SOURCE_HEIGHT instead.
 */
#define VX_REMAP_ATTRIBUTE_SOURCE_HEIGHT        VX_REMAP_SOURCE_HEIGHT

/**
 * \ingroup nvx_deprecated
 * \brief The destination width.
 * \deprecated Use \ref VX_REMAP_DESTINATION_WIDTH instead.
 */
#define VX_REMAP_ATTRIBUTE_DESTINATION_WIDTH    VX_REMAP_DESTINATION_WIDTH

/**
 * \ingroup nvx_deprecated
 * \brief The destination height.
 * \deprecated Use \ref VX_REMAP_DESTINATION_HEIGHT instead.
 */
#define VX_REMAP_ATTRIBUTE_DESTINATION_HEIGHT   VX_REMAP_DESTINATION_HEIGHT

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief The type of the Array items.
 * \deprecated Use \ref VX_ARRAY_ITEMTYPE instead.
 */
#define VX_ARRAY_ATTRIBUTE_ITEMTYPE         VX_ARRAY_ITEMTYPE

/**
 * \ingroup nvx_deprecated
 * \brief The number of items in the Array.
 * \deprecated Use \ref VX_ARRAY_NUMITEMS instead.
 */
#define VX_ARRAY_ATTRIBUTE_NUMITEMS         VX_ARRAY_NUMITEMS

/**
 * \ingroup nvx_deprecated
 * \brief The maximal number of items that the Array can hold.
 * \deprecated Use \ref VX_ARRAY_CAPACITY instead.
 */
#define VX_ARRAY_ATTRIBUTE_CAPACITY         VX_ARRAY_CAPACITY

/**
 * \ingroup nvx_deprecated
 * \brief Queries an array item size.
 * \deprecated Use \ref VX_ARRAY_ITEMSIZE instead.
 */
#define VX_ARRAY_ATTRIBUTE_ITEMSIZE         VX_ARRAY_ITEMSIZE

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief The type of reference contained in the delay.
 * \deprecated Use \ref VX_DELAY_TYPE instead.
 */
#define VX_DELAY_ATTRIBUTE_TYPE             VX_DELAY_TYPE

/**
 * \ingroup nvx_deprecated
 * \brief The number of items in the delay.
 * \deprecated Use \ref VX_DELAY_SLOTS instead.
 */
#define VX_DELAY_ATTRIBUTE_SLOTS            VX_DELAY_SLOTS

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief Output values are determined by averaging the source pixels whose areas fall under the
 *        area of the destination pixel, projected onto the source image.
 * \deprecated Use \ref VX_INTERPOLATION_AREA instead.
 */
#define VX_INTERPOLATION_TYPE_AREA                  VX_INTERPOLATION_AREA

/**
 * \ingroup nvx_deprecated
 * \brief Output values are defined by bilinear interpolation between the pixels whose centers are closest
 *        to the sample position, weighted linearly by the distance of the sample from the pixel centers.
 * \deprecated Use \ref VX_INTERPOLATION_BILINEAR instead.
 */
#define VX_INTERPOLATION_TYPE_BILINEAR              VX_INTERPOLATION_BILINEAR

/**
 * \ingroup nvx_deprecated
 * \brief Output values are defined to match the source pixel whose center is nearest to the sample position.
 * \deprecated Use \ref VX_INTERPOLATION_NEAREST_NEIGHBOR instead.
 */
#define VX_INTERPOLATION_TYPE_NEAREST_NEIGHBOR      VX_INTERPOLATION_NEAREST_NEIGHBOR

//---------------------------------------------------------------------------

/*
#define VX_META_FORMAT_ATTRIBUTE_DELTA_RECTANGLE  (VX_ATTRIBUTE_BASE(VX_ID_KHRONOS, VX_TYPE_META_FORMAT) + 0x0)
*/

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief Indicates to the implementation that the user wants to disable any parallelization techniques.
 * \deprecated Not supported.
 */
#define VX_HINT_SERIALIZE (VX_ENUM_BASE(VX_ID_KHRONOS, VX_ENUM_HINT) + 0x0)

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief An enumeration of memory import types.
 * \deprecated Use \ref vx_memory_type_e instead.
 */
#define vx_import_type_e        vx_memory_type_e

/**
 * \ingroup nvx_deprecated
 * \brief The memory import enumeration.
 * \deprecated Use \ref VX_ENUM_MEMORY_TYPE instead.
 */
#define VX_ENUM_IMPORT_MEM      VX_ENUM_MEMORY_TYPE

/**
 * \ingroup nvx_deprecated
 * \brief The default memory type to import from the Host.
 * \deprecated Use \ref VX_MEMORY_TYPE_HOST instead.
 */
#define VX_IMPORT_TYPE_HOST     VX_MEMORY_TYPE_HOST

/**
 * \ingroup nvx_deprecated
 * \brief For memory allocated through OpenVX, this is the import type.
 * \deprecated Use \ref VX_MEMORY_TYPE_NONE instead.
 */
#define VX_IMPORT_TYPE_NONE     VX_MEMORY_TYPE_NONE

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief A value for comparison between Khronos defined objects and vendor structs.
 * \deprecated Use \ref VX_TYPE_KHRONOS_OBJECT_END instead.
 */
#define VX_TYPE_OBJECT_MAX      VX_TYPE_KHRONOS_OBJECT_END

/**
 * \ingroup nvx_deprecated
 * \brief A value for comparison between Khronos defined structs and user structs.
 * \deprecated Use \ref VX_TYPE_KHRONOS_STRUCT_MAX instead.
 */
#define VX_TYPE_STRUCT_MAX      VX_TYPE_KHRONOS_STRUCT_MAX

//---------------------------------------------------------------------------

/*
#define VX_KERNEL_INVALID (VX_KERNEL_BASE(VX_ID_KHRONOS, VX_LIBRARY_KHR_BASE) + 0x0)
*/

//---------------------------------------------------------------------------

/**
 * \ingroup nvx_deprecated
 * \brief The user-defined kernel node input parameter validation function.
 *
 * \deprecated Use \ref vx_kernel_validate_f and \ref vxAddUserKernel instead.
 *
 * \note This function is called once for each VX_INPUT or VX_BIDIRECTIONAL parameter index.
 *
 * \param [in] node     The handle to the node that is being validated.
 * \param [in] index    The index of the parameter being validated.
 *
 * \return An error code describing the validation status on this parameter.
 * \retval VX_ERROR_INVALID_FORMAT      The parameter format was incorrect.
 * \retval VX_ERROR_INVALID_VALUE       The value of the parameter was incorrect.
 * \retval VX_ERROR_INVALID_DIMENSION   The dimensionality of the parameter was incorrect.
 * \retval VX_ERROR_INVALID_PARAMETERS  The index was out of bounds.
 */
typedef vx_status(VX_CALLBACK *vx_kernel_input_validate_f)(vx_node node, vx_uint32 index);

/**
 * \ingroup nvx_deprecated
 * \brief The user-defined kernel node output parameter validation function.
 *
 * The function only needs to fill in the meta data structure.
 *
 * \deprecated Use \ref vx_kernel_validate_f and \ref vxAddUserKernel instead.
 *
 * \note This function is called once for each VX_OUTPUT parameter index.
 *
 * \param [in] node     The handle to the node that is being validated.
 * \param [in] index    The index of the parameter being validated.
 * \param [in] ptr      A pointer to a pre-allocated structure that the system holds.
 *                          The validation function fills in the correct type, format, and dimensionality for
 *                          the system to use either to create memory or to check against existing memory.
 *
 * \return An error code describing the validation status on this parameter.
 * \retval VX_ERROR_INVALID_PARAMETERS  The index is out of bounds.
 */
typedef vx_status(VX_CALLBACK *vx_kernel_output_validate_f)(vx_node node, vx_uint32 index, vx_meta_format meta);

//---------------------------------------------------------------------------

/*
typedef struct _vx_delta_rectangle_t {
    vx_int32 delta_start_x;
    vx_int32 delta_start_y;
    vx_int32 delta_end_x;
    vx_int32 delta_end_y;
} vx_delta_rectangle_t;
*/

//---------------------------------------------------------------------------

#ifdef __cplusplus
extern "C" {
#endif

/**
 * \ingroup nvx_deprecated
 * \brief Allows users to add custom kernels to the known kernel database in OpenVX at run-time.
 *
 * This would primarily be used by the module function \c vxPublishKernels.
 *
 * \deprecated Use \ref vxAddUserKernel instead.
 *
 * \param [in] context      The reference to the implementation context.
 * \param [in] name         The string to use to match the kernel.
 * \param [in] enumeration  The enumerated value of the kernel to be used by clients.
 * \param [in] func_ptr     The process-local function pointer to be invoked.
 * \param [in] numParams    The number of parameters for this kernel.
 * \param [in] input        The pointer to \ref vx_kernel_input_validate_f,
 *                              which validates the input parameters to this kernel.
 * \param [in] output       The pointer to \ref vx_kernel_output_validate_f,
 *                              which validates the output parameters to this kernel.
 * \param [in] init         The kernel initialization function.
 * \param [in] deinit       The kernel de-initialization function.
 *
 * \return \ref vx_kernel
 * \retval 0 Indicates that an error occurred when adding the kernel.
 * \retval * Kernel added to OpenVX.
 */
VX_API_ENTRY vx_kernel VX_API_CALL vxAddKernel(vx_context context,
                             const vx_char name[VX_MAX_KERNEL_NAME],
                             vx_enum enumeration,
                             vx_kernel_f func_ptr,
                             vx_uint32 numParams,
                             vx_kernel_input_validate_f input,
                             vx_kernel_output_validate_f output,
                             vx_kernel_initialize_f init,
                             vx_kernel_deinitialize_f deinit);

/**
 * \ingroup nvx_deprecated
 * \brief Allows the User to extract a rectangular patch (subset) of an image from a single plane.
 *
 * \deprecated Use \ref vxMapImagePatch and \ref vxUnmapImagePatch or \ref vxCopyImagePatch instead.
 *
 * \param [in] image        The reference to the image from which to extract the patch.
 * \param [in] rect         The coordinates from which to get the patch. Must be 0 <= start < end.
 * \param [in] plane_index  The plane index from which to get the data.
 * \param [in, out] addr    A pointer to a structure describing the addressing information of the
 *                              image patch to accessed.
 *      \arg Input case: ptr is a pointer to a non-NULL pointer. The addr parameter must be the
 *              address of an addressing
 *              structure that describes how the user will access the requested image data at address (*ptr).
 *      \arg Output case: ptr is a pointer to a NULL pointer. The function fills the structure pointed by
 *              addr with the addressing information that the user must consult to access the pixel data at address (*ptr).
 *      If the image being accessed was created via \ref vxCreateImageFromHandle, then the
 *          returned addressing information will be the identical to that of the addressing structure provided
 *          when \ref vxCreateImageFromHandle was called.
 * \param [in, out] ptr     A pointer to a pointer to a location to store the requested data.
 *      \arg Input case: ptr is a pointer to a non-NULL pointer to a valid pixel buffer. This buffer
 *          will be used in one of two ways, depending on the value of the usage parameter. If usage is VX_WRITE_ONLY, then the
 *          buffer must contain pixel data that the user wants to replace the image's pixel data with.
 *          Otherwise (i.e., usage is not VX_WRITE_ONLY), the image's current pixel data will be written to the
 *          memory starting at address (*ptr) as storage memory for the access request. The caller must ensure
 *          enough memory has been allocated for the requested patch with the requested addressing.
 *          If image was created via \ref vxCreateImageFromHandle, and the pixel buffer pointed to by (*ptr) overlaps
 *          the original pixel buffer provided when image was created, then the results of such a call to
 *          \ref vxAccessImagePatch are undefined.
 *      \arg Output case: ptr is a pointer to a NULL pointer. This NULL pointer will be overwritten
 *          with a pointer to the address where the requested data can be accessed. If image was created via
 *          \ref vxCreateImageFromHandle then the overwriting pointer must be within the original pixel buffer
 *          provided when image was created.
 *      \arg (*ptr) must eventually be provided as the ptr parameter of a call to \ref vxCommitImagePatch.
 * \param [in] usage        This declares the intended usage of the pointer using the \ref vx_accessor_e enumeration. For uniform images Only VX_READ_ONLY is supported.
 *
 * \note The addr and ptr parameters must both be input, or both be output, otherwise the behavior is undefined.
 *
 * \note Users must be cautious to prevent passing in \e uninitialized pointers or
 *       addresses of uninitialized pointers to this function.
 *
 * \note The user may ask for data outside the bounds of the valid region, but
 *       such data has an undefined value.
 *
 * \return A \ref vx_status_e enumeration.
 * \retval VX_ERROR_OPTIMIZED_AWAY      The reference is a virtual image and cannot be accessed or committed.
 * \retval VX_ERROR_INVALID_PARAMETERS  The \a start, \a end, \a plane_index, \a stride_x, or \a stride_y pointer is incorrect.
 * \retval VX_ERROR_INVALID_REFERENCE   The image reference is not actually an image reference.
 *
 * \pre \ref vxComputeImagePatchSize if users wish to allocate their own memory.
 * \post \ref vxCommitImagePatch with same (*ptr) value.
 */
VX_API_ENTRY vx_status VX_API_CALL vxAccessImagePatch(vx_image image,
                                    const vx_rectangle_t *rect,
                                    vx_uint32 plane_index,
                                    vx_imagepatch_addressing_t *addr,
                                    void **ptr,
                                    vx_enum usage);

/**
 * \ingroup nvx_deprecated
 * \brief This allows the User to commit a rectangular patch (subset) of an image from a single plane.
 *
 * \deprecated Use \ref vxMapImagePatch and \ref vxUnmapImagePatch or \ref vxCopyImagePatch instead.
 *
 * \param [in] image        The reference to the image from which to extract the patch.
 * \param [in] rect         The coordinates to which to set the patch. Must be 0 <= start <= end.
 *                              This may be 0 or a rectangle of zero area in order to indicate that the commit
 *                              must only decrement the reference count.
 * \param [in] plane_index  The plane index to which to set the data.
 * \param [in] addr         The addressing information for the image patch.
 * \param [in] ptr          A pointer to a pixel buffer to be committed. If the user previously provided a
 *                              pointer to this buffer to \ref vxAccessImagePatch, the buffer can be
 *                              freed or re-used after \ref vxCommitImagePatch completes. If the pointer was returned by
 *                              \ref vxAccessImagePatch, reads or writes to the location pointed by ptr after
 *                              \ref vxCommitImagePatch completes will result in undefined behavior.
 *
 * \note If the implementation gives the client a pointer from
 *       \ref vxAccessImagePatch then implementation-specific behavior may occur.
 *       If not, then a copy occurs from the users pointer to the internal data of the object.
 * \note If the rectangle intersects bounds of the current valid region, the
 *       valid region grows to the union of the two rectangles as long as they occur
 *       within the bounds of the original image dimensions.
 *
 * \return A \ref vx_status_e enumeration.
 * \retval VX_ERROR_OPTIMIZED_AWAY      The reference is a virtual image and cannot be accessed or committed.
 * \retval VX_ERROR_INVALID_PARAMETERS  The \a start, \a end, \a plane_index, \a stride_x, or \a stride_y pointer is incorrect.
 * \retval VX_ERROR_INVALID_REFERENCE   The image reference is not actually an image reference.
 */
VX_API_ENTRY vx_status VX_API_CALL vxCommitImagePatch(vx_image image,
                                    const vx_rectangle_t *rect,
                                    vx_uint32 plane_index,
                                    const vx_imagepatch_addressing_t *addr,
                                    const void *ptr);

/**
 * \ingroup nvx_deprecated
 * \brief Grants access to a sub-range of an Array. The number of elements in the sub-range is given by (end - start).
 *
 * \deprecated Use \ref vxMapArrayRange and \ref vxUnmapArrayRange or \ref vxCopyArrayRange instead.
 *
 * \param [in] arr          The reference to the Array.
 * \param [in] start        The start index.
 * \param [in] end          The end index. (end - start) elements are accessed from start.
 * \param [in, out] stride  A pointer to 'number of bytes' between the beginning of two consequent elements.
 *      \arg Input case: ptr is a pointer to a non-NULL pointer. The stride parameter must be the address
 *          of a vx_size scalar that describes how the user will access the requested array data at address
 *          (*ptr).
 *      \arg Output Case: ptr is a pointer to a NULL pointer. The function fills the vx_size scalar
 *          pointed by stride with the element stride information that the user must consult to access the
 *          array elements at address (*ptr).
 * \param [out] ptr         A pointer to a pointer to a location to store the requested data.
 *      \arg Input Case: ptr is a pointer to a non-NULL pointer to a valid buffer. This buffer will be
 *          used in one of two ways, depending on the value of the usage parameter. If usage is
 *          VX_WRITE_ONLY, then the buffer must contain element data that the user wants to replace the
 *          array's element data with. Otherwise (i.e., usage is not VX_WRITE_ONLY), the array's current
 *          element data will be written to the memory starting at address (*ptr) as storage memory for the
 *          access request. The caller must ensure enough memory has been allocated for the requested array
 *          range with the requested stride.
 *      \arg Output Case: ptr is a pointer to a NULL pointer.  This NULL pointer will be overwritten with
 *          a pointer to the address where the requested data can be accessed. (*ptr) must eventually be provided
 *          as the ptr parameter of a call to vxCommitArrayRange.
 * \param [in] usage        This declares the intended usage of the pointer using the \ref vx_accessor_e enumeration.
 *
 * \note The stride and ptr parameters must both be input, or both be output, otherwise the behavior
 *       is undefined.
 *
 * \return A \ref vx_status_e enumeration.
 * \retval VX_SUCCESS                   No errors.
 * \retval VX_ERROR_OPTIMIZED_AWAY      If the reference is a virtual array and cannot be accessed or committed.
 * \retval VX_ERROR_INVALID_REFERENCE   If the \a arr is not a \ref vx_array.
 * \retval VX_ERROR_INVALID_PARAMETERS  If any of the other parameters are incorrect.
 *
 * \post \ref vxCommitArrayRange
 */
VX_API_ENTRY vx_status VX_API_CALL vxAccessArrayRange(vx_array arr, vx_size start, vx_size end, vx_size *stride, void **ptr, vx_enum usage);

/**
 * \ingroup nvx_deprecated
 * \brief Commits data back to the Array object.
 *
 * \deprecated Use \ref vxMapArrayRange and \ref vxUnmapArrayRange or \ref vxCopyArrayRange instead.
 *
 * \details This allows a user to commit data to a sub-range of an Array. The number of elements in the sub-range is given by (end - start).
 *
 * \param [in] arr          The reference to the Array.
 * \param [in] start        The start index.
 * \param [in] end          The end index. (end - start) elements are accessed from start.
 * \param [in] ptr          The user supplied pointer.
 *
 * \return A \ref vx_status_e enumeration.
 * \retval VX_SUCCESS                   No errors.
 * \retval VX_ERROR_OPTIMIZED_AWAY      If the reference is a virtual array and cannot be accessed or committed.
 * \retval VX_ERROR_INVALID_REFERENCE   If the \a arr is not a \ref vx_array.
 * \retval VX_ERROR_INVALID_PARAMETERS  If any of the other parameters are incorrect.
 */
VX_API_ENTRY vx_status VX_API_CALL vxCommitArrayRange(vx_array arr, vx_size start, vx_size end, const void *ptr);

/**
 * \ingroup nvx_deprecated
 * \brief Grants access to a distribution object and increments the object reference count in case of success.
 *
 * \deprecated Use \ref vxMapDistribution and \ref vxUnmapDistribution or \ref vxCopyDistribution instead.
 *
 * \param [in] distribution     The reference to the distribution to access.
 * \param [in, out] ptr         The user-supplied address to a pointer, via which the requested contents
 *                                  are returned.
 *      \arg If ptr is NULL, an error occurs.
 *      \arg If ptr is not NULL and (*ptr) is NULL, (*ptr) will be set to the address of a memory area
 *          managed by the OpenVX framework containing the requested data.
 *      \arg If both ptr and (*ptr) are not NULL, requested data will be copied to (*ptr) (optionally in
 *          case of write-only access).
 * \param [in] usage            The \ref vx_accessor_e value to describe the access of the object.
 *
 * \return A \ref vx_status_e enumeration.
 *
 * \post \ref vxCommitDistribution
 */
VX_API_ENTRY vx_status VX_API_CALL vxAccessDistribution(vx_distribution distribution, void **ptr, vx_enum usage);

/**
 * \ingroup nvx_deprecated
 * \brief Commits the distribution objec> and decrements the object reference count in case of success.
 *
 * \deprecated Use \ref vxMapDistribution and \ref vxUnmapDistribution or \ref vxCopyDistribution instead.
 *
 * The memory must be a vx_uint32 array of a value at least as big as the value returned via
 * \ref VX_DISTRIBUTION_ATTRIBUTE_BINS.
 *
 * \param [in] distribution     The Distribution to modify.
 * \param [in] ptr              The pointer provided or returned by \ref vxAccessDistribution.
 *                                  The ptr cannot be NULL.
 *
 * \return A \ref vx_status_e enumeration.
 *
 * \pre \ref vxAccessDistribution.
 */
VX_API_ENTRY vx_status VX_API_CALL vxCommitDistribution(vx_distribution distribution, const void * ptr);

/**
 * \ingroup nvx_deprecated
 * \brief Grants access to a LUT table and increments the object reference count in case of success.
 *
 * \deprecated Use \ref vxMapLUT and \ref vxUnmapLUT or \ref vxCopyLUT instead.
 *
 * \details There are several variations of call methodology:
 *      \arg If \a ptr is NULL (which means the current data of the LUT is not desired),
 *          the LUT reference count is incremented.
 *      \arg If \a ptr is not NULL but (*ptr) is NULL, (*ptr) will contain the address of the LUT data when the function returns and
 *          the reference count will be incremented. Whether the (*ptr) address is mapped
 *          or allocated is undefined. (*ptr) must be returned to \ref vxCommitLUT.
 *      \arg If \a ptr is not NULL and (*ptr) is not NULL, the user is signalling the implementation to copy the LUT data into the location specified
 *          by (*ptr). Users must use \ref vxQueryLUT with \ref VX_LUT_ATTRIBUTE_SIZE to
 *          determine how much memory to allocate for the LUT data.
 *
 * In any case, \ref vxCommitLUT must be called after LUT access is complete.
 *
 * \param [in] lut      The LUT from which to get the data.
 * \param [in,out] ptr  The user-supplied address to a pointer, via which the requested contents
 *                          are returned.
 *      \arg If ptr is NULL, an error occurs.
 *      \arg If ptr is not NULL and (*ptr) is NULL, (*ptr) will be set to the address of a memory area
 *          managed by the OpenVX framework containing the requested data.
 *      \arg If both ptr and (*ptr) are not NULL, requested data will be copied to (*ptr) (optionally in
 *          case of write-only access).
 * \param [in] usage    This declares the intended usage of the pointer using the * \ref vx_accessor_e enumeration.
 *
 * \return A \ref vx_status_e enumeration.
 *
 * \post \ref vxCommitLUT
 */
VX_API_ENTRY vx_status VX_API_CALL vxAccessLUT(vx_lut lut, void **ptr, vx_enum usage);

/**
 * \ingroup nvx_deprecated
 * \brief Commits the Lookup Table and decrements the object reference count in case of success.
 *
 * \deprecated Use \ref vxMapLUT and \ref vxUnmapLUT or \ref vxCopyLUT instead.
 *
 * \details Commits the data back to the LUT object and decrements the reference count.
 * There are several variations of call methodology:
 *      \arg If a user should allocated their own memory for the LUT data copy, the user is
 *          obligated to free this memory.
 *      \arg If \a ptr is not NULL and the (*ptr) for \ref vxAccessLUT was NULL,
 *          it is undefined whether the implementation will unmap or copy and free the memory.
 *
 * \param [in] lut  The LUT to modify.
 * \param [in] ptr  The pointer provided or returned by \ref vxAccessLUT. This cannot be NULL.
 *
 * \return A \ref vx_status_e enumeration.
 *
 * \pre \ref vxAccessLUT.
 */
VX_API_ENTRY vx_status VX_API_CALL vxCommitLUT(vx_lut lut, const void *ptr);

/**
 * \ingroup nvx_deprecated
 * \brief Gets the matrix data (copy).
 *
 * \deprecated Use \ref vxCopyMatrix instead.
 *
 * \note \ref vxQueryMatrix and \ref VX_MATRIX_COLUMNS and \ref VX_MATRIX_ROWS
 *       to get the needed number of elements of the array.
 *
 * \param [in] mat      The reference to the matrix.
 * \param [out] array   The array in which to place the matrix.
 *
 * \return A \ref vx_status_e enumeration.
 */
VX_API_ENTRY vx_status VX_API_CALL vxReadMatrix(vx_matrix mat, void *array);

/**
 * \ingroup nvx_deprecated
 * \brief Sets the matrix data (copy).
 *
 * \deprecated Use \ref vxCopyMatrix instead.
 *
 * \note \ref vxQueryMatrix and \ref VX_MATRIX_COLUMNS and \ref VX_MATRIX_ROWS
 *       to get the needed number of elements of the array.
 *
 * \param [in] mat      The reference to the matrix.
 * \param [in] array    The array containing the matrix to be written.
 *
 * \return A \ref vx_status_e enumeration.
 */
VX_API_ENTRY vx_status VX_API_CALL vxWriteMatrix(vx_matrix mat, const void *array);

/**
 * \ingroup nvx_deprecated
 * \brief Gets the convolution data (copy).
 *
 * \deprecated Use \ref vxCopyConvolutionCoefficients instead.
 *
 * \note \ref vxQueryConvolution and \ref VX_CONVOLUTION_SIZE to get the
 *       needed number of bytes of the array.
 *
 * \param [in] conv     The reference to the convolution.
 * \param [out] array   The array to place the convolution.
 *
 * \return A \ref vx_status_e enumeration.
 */
VX_API_ENTRY vx_status VX_API_CALL vxReadConvolutionCoefficients(vx_convolution conv, vx_int16 *array);

/**
 * \ingroup nvx_deprecated
 * \brief Sets the convolution data (copy).
 *
 * \deprecated Use \ref vxCopyConvolutionCoefficients instead.
 *
 * \note \ref vxQueryConvolution and \ref VX_CONVOLUTION_SIZE to get the
 *       needed number of bytes of the array.
 *
 * \param [in] conv     The reference to the convolution.
 * \param [in] array    The array containing the convolution to be written.
 *
 * \return A \ref vx_status_e enumeration.
 */
VX_API_ENTRY vx_status VX_API_CALL vxWriteConvolutionCoefficients(vx_convolution conv, const vx_int16 *array);

/**
 * \ingroup nvx_deprecated
 * \brief Gets the scalar value out of a reference.
 *
 * \deprecated Use \ref vxCopyScalar instead.
 *
 * \note Use this in conjunction with Query APIs that return references which
 *       should be converted into values.
 *
 * \param [in] ref      The reference from which to get the scalar value.
 * \param [out] ptr     An appropriate typed pointer that points to a location to which to copy
 *                          the scalar value.
 *
 * \return A \ref vx_status_e enumeration.
 * \retval VX_ERROR_INVALID_REFERENCE   If the ref is not a valid reference.
 * \retval VX_ERROR_INVALID_PARAMETERS  If \a ptr is NULL.
 * \retval VX_ERROR_INVALID_TYPE        If the type does not match the type in the reference or is a bad value.
 */
VX_API_ENTRY vx_status VX_API_CALL vxReadScalarValue(vx_scalar ref, void *ptr);

/**
 * \ingroup nvx_deprecated
 * \brief Sets the scalar value in a reference.
 *
 * \deprecated Use \ref vxCopyScalar instead.
 *
 * \note Use this in conjunction with Parameter APIs that return references
 *       to parameters that need to be altered.
 *
 * \param [in] ref  The reference from which to get the scalar value.
 * \param [in] ptr  An appropriately typed pointer that points to a location to which to copy
 *                      the scalar value.
 *
 * \return A \ref vx_status_e enumeration.
 * \retval VX_ERROR_INVALID_REFERENCE   If the ref is not a valid reference.
 * \retval VX_ERROR_INVALID_PARAMETERS  If \a ptr is NULL.
 * \retval VX_ERROR_INVALID_TYPE        If the type does not match the type in the reference or is a bad value.
 */
VX_API_ENTRY vx_status VX_API_CALL vxWriteScalarValue(vx_scalar ref, const void *ptr);

#ifdef __cplusplus
}
#endif

#endif /* VX_1_0_1_NAMING_COMPATIBILITY */
