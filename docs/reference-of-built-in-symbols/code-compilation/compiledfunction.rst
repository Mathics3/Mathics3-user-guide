CompiledFunction
================

`WMA link <https://reference.wolfram.com/language/ref/CompiledFunction.html>`_


:code:`CompiledFunction` [:math:`args`...]
    represents compiled code for evaluating a compiled function.





>>> sqr = Compile[{x}, x x]

>>> Head[sqr]

    =
:math:`\text{CompiledFunction}`


>>> sqr[2]

    =
:math:`4.`


