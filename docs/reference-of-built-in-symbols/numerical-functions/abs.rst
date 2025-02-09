Abs
===

`Absolute value <https://en.wikipedia.org/wiki/Absolute_value>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/elementary.html#sympy.functions.elementary.complexes.Abs>`_, `WMA <https://reference.wolfram.com/language/ref/Abs>`_)


:code:`Abs` [:math:`x`]
    returns the absolute value of :math:`x`.





>>> Abs[-3]

    =
:math:`3`


>>> Plot[Abs[x], {x, -4, 4}]

    =
.. image:: tmpsg20dc13.png
    :align: center




:code:`Abs`  returns the magnitude of complex numbers:

>>> Abs[3 + I]

    =
:math:`\sqrt{10}`


>>> Abs[3.0 + I]

    =
:math:`3.16228`



All of the below evaluate to Infinity:

>>> Abs[Infinity] == Abs[I Infinity] == Abs[ComplexInfinity]

    =
:math:`\text{True}`


