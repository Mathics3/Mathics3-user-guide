Pochhammer
==========

`Rising factorial <https://en.wikipedia.org/wiki/Falling_and_rising_factorials>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/combinatorial.html#risingfactorial>`_, `WMA <https://reference.wolfram.com/language/ref/Pochhammer.html>`_)

The Pochhammer symbol or rising factorial often appears in series     expansions for hypergeometric functions.

The Pochammer symbol has a definite value even when the gamma     functions which appear in its definition are infinite.

:code:`Pochhammer` [:math:`a`, :math:`n`]
    is the Pochhammer symbol :math:`a_n`.





Product of the first 3 numbers:

>>> Pochhammer[1, 3]
    =

:math:`6`



:code:`Pochhammer[1, :math:`n`]`  is     the same as Pochhammer[2, :math:`n`-1] since 1 is a multiplicative identity.

>>> Pochhammer[1, 3] == Pochhammer[2, 2]
    =

:math:`\text{True}`



Although sometimes :code:`Pochhammer[0, :math:`n`]`  is taken to be 1, in Mathics it is 0:

>>> Pochhammer[0, n]
    =

:math:`0`



Pochhammer uses Gamma for non-Integer values of :math:`n`:

>>> Pochhammer[1, 3.001]
    =

:math:`6.00754`


>>> Pochhammer[1, 3.001] == Pochhammer[2, 2.001]
    =

:math:`\text{True}`


>>> Pochhammer[1.001, 3] == 1.001 2.001 3.001
    =

:math:`\text{True}`


