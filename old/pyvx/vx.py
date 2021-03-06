""" 
:mod:`pyvx.vx` --- C-like Python API
==========================================

This module provides the functions specified by the `OpenVX`_ standard.
Please refer to the `OpenVX speficication`_ for a description of the API. The
module name vx is used instead of a vx prefix on all symbols. The initial
example on page 12 of the specification would in python look like this:

.. code-block:: python 

    from pyvx import vx

    context = vx.CreateContext()
    images = [
        vx.CreateImage(context, 640, 480, vx.DF_IMAGE_UYVY),
        vx.CreateImage(context, 640, 480, vx.DF_IMAGE_U8),
        vx.CreateImage(context, 640, 480, vx.DF_IMAGE_U8),
    ]
    graph = vx.CreateGraph(context)
    virts = [
        vx.CreateVirtualImage(graph, 0, 0, vx.DF_IMAGE_VIRT),
        vx.CreateVirtualImage(graph, 0, 0, vx.DF_IMAGE_VIRT),
        vx.CreateVirtualImage(graph, 0, 0, vx.DF_IMAGE_VIRT),
        vx.CreateVirtualImage(graph, 0, 0, vx.DF_IMAGE_VIRT),
    ]
    vx.ChannelExtractNode(graph, images[0], vx.CHANNEL_Y, virts[0])
    vx.Gaussian3x3Node(graph, virts[0], virts[1])
    vx.Sobel3x3Node(graph, virts[1], virts[2], virts[3])
    vx.MagnitudeNode(graph, virts[2], virts[3], images[1])
    vx.PhaseNode(graph, virts[2], virts[3], images[2])
    status = vx.VerifyGraph(graph)
    if status == vx.SUCCESS:
        status = vx.ProcessGraph(graph)
    else:
        print("Verification failed.")
    vx.ReleaseContext(context)


.. _`OpenVX`: https://www.khronos.org/openvx
.. _`OpenVX speficication`: https://www.khronos.org/registry/vx/specs/OpenVX_1.0_Provisional_Specifications.zip

In some cases, the C-API uses pointers to pass data in and out
of functions. As there are no similar concept in python, direct values 
and multiple return values are used instead. The python signature are:

.. code-block:: python 

"""

from pyvx.inc.vx import *
from pyvx import model
from pyvx.nodes import *
from functools import wraps

def _make_api_function(api, func):
    @wraps(func)
    def f(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return api.on_exception.hanlde(e)
    f.__name__ = api.name
    return f

for n in sorted(dir(model)):
    func = getattr(model, n)
    if hasattr(func, 'apis'):
        for api in func.apis:
            locals()[api.name] = _make_api_function(api, func)
            args = func.func_code.co_varnames[:func.func_code.co_argcount]
            args = ', '.join(str(a) for a in args)
            r = api.returns
            if r:
                r += ' = '
            __doc__ += '    %s%s(%s)\n' % (r, api.name, args)
