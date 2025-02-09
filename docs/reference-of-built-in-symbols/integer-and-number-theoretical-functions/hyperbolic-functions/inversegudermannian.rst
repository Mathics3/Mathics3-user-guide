InverseGudermannian
===================

`Inverse Gudermannian function <https://en.wikipedia.org/wiki/Gudermannian_function>`_ (`WMA <https://reference.wolfram.com/language/ref/InverseGudermannian.html>`_, `MathWorld <https://mathworld.wolfram.com/InverseGudermannian.html>`_)

:code:`InverseGudermannian` [:math:`z`]
    returns the inverse Gudermannian function :math:`gd`^-1(:math:`z`).





>>> InverseGudermannian[.5]

    =
:math:`0.522238`



:code:`InverseGudermannian[-:math:`z`]`  == -:code:`InversGudermannian[:math:`z`]` :

>>> InverseGudermannian[-.5] ==  -InverseGudermannian[.5]

    =
:math:`\text{True}`



InverseGudermannian is 0 at multiples of 8 Pi:
= 0

>>> Plot[InverseGudermannian[x], {x, -2 Pi, 2 Pi}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Integer_and_Number-Theoretical_Functions_InverseGudermannian_v616qlnx.png
    :align: center



