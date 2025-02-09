Subfactorial
============

`Derangement <https://en.wikipedia.org/wiki/Derangement>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/combinatorial.html#sympy.functions.combinatorial.factorials.subfactorial>`_, `WMA <https://reference.wolfram.com/language/ref/Subfactorial.html>`_)


:code:`Subfactorial` [:math:`n`]
    computes the subfactorial of :math:`n`.





Here are the first few derangements:

>>> Subfactorial[{0, 1, 2, 3}]

    =
:math:`\left\{1,0,1,2\right\}`



We can handle :code:`MachineReal`  numbers:

>>> Subfactorial[6.0]

    =
:math:`265`



Here is how the exponential, :code:`Factorial` , and :code:`Subfactoral`  grow in comparison:

>>> LogPlot[{10^x, Factorial[x], Subfactorial[x]}, {x, 0, 25}, PlotPoints->26]

    =
.. image:: tmphczy7f8u.png
    :align: center



