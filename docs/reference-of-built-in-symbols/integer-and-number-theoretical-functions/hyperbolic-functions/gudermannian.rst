Gudermannian
============

`Gudermannian function <https://en.wikipedia.org/wiki/Gudermannian_function>`_ (`WMA <https://reference.wolfram.com/language/ref/Gudermannian.html>`_, `MathWorld <https://mathworld.wolfram.com/Gudermannian.html>`_)

:code:`Gudermannian` [:math:`z`]
    returns the Gudermannian function :math:`gd`(:math:`z`).





>>> Gudermannian[4.2]

    =
:math:`1.54081`



:code:`Gudermannian[-:math:`z`]`  == - :code:`Gudermannian[:math:`z`]` :

>>> Gudermannian[-4.2] ==  -Gudermannian[4.2]

    =
:math:`\text{True}`


>>> Plot[Gudermannian[x], {x, -10, 10}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Integer_and_Number-Theoretical_Functions_Gudermannian_0epvr2c8.png
    :align: center



