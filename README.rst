About this fork
---------------

I've created this fork because the original PyVX bindings did not support the OpenVX implementation I wanted to use (NVidia VisionWorks). After fixing that fairly simple problem, I noticed that the bindings were using hand-edited versions of the OpenVX header files, which happened to be out of date (they were taken from the 1.0 release, while VisionWorks at the time of writing ships with 1.1, which is also the latest version published by Khronos).

Though hand-edited header files are more or less recommended by the authors of the binding library CFFI used by PyVX, I was unsatisfied with this approach, and found an alternative in the form of libclang, which is the C interface around the awesome CLang C/C++ parsing library. Since libclang comes complete with Python bindings, I decided to give this a try.

[TODO: update this section when done]

That "try" turned out to take a couple of days of experimentation (mainly due to my still being new to Python), but I succeeded yesterday in extracting from the header files declarations that were accepted by both CFFI and the Visual C++ compiler (I'm using 2015 Community Edition).

I haven't cleanup up my code yet (almost exclusively in pyvx/build_cbackend.py and pyvx/api_filter.py), and probably won't do so until I've confirmed that my OpenVX bindings are actually working.

Next step: testing, fixing, cleaning up.


Original PyVX README
--------------------

PyVX is a set of python bindings for `OpenVX`_. `OpenVX`_ is a standard for
expressing computer vision processing algorithms as a graph of function nodes.
This graph is verified once and can then be processed (executed) multiple
times. PyVX allows these graphs to be constructed and interacted with from
python. It also supports the use of multiple `OpenVX`_ backends, both C and
python backends. It also used to contain a code generating `OpenVX`_ backend
written it python, but it will be moved to a package of it's own (curently
it lives on the try1 branch of pyvx).

Further details are provided in the `Documentation`_

.. _`OpenVX`: https://www.khronos.org/openvx
.. _`Documentation`: https://pyvx.readthedocs.org
