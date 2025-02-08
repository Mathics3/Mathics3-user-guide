Get
===

`WMA link <https://reference.wolfram.com/language/ref/Get.html>`_


:code:`<<:math:`name``
    reads a file and evaluates each expression, returning only the last one.

:code:`Get` [:math:`name`, Trace->True]
    Runs Get tracing each line before it is evaluated.
    
    :code:`Settings`$TraceGet`  can be also used to trace lines on all :code:`Get[]`  calls.





>>> filename = $TemporaryDirectory <> "/example_file";


>>> Put[x + y, filename]


>>> Get[filename]
    =

:math:`x+y`


>>> filename = $TemporaryDirectory <> "/example_file";


>>> Put[x + y, 2x^2 + 4z!, Cos[x] + I Sin[x], filename]


>>> Get[filename]
    =

:math:`\text{Cos}\left[x\right]+I \text{Sin}\left[x\right]`


>>> DeleteFile[filename]


