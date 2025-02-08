SixJSymbol
==========

`6-j symbol <https://en.wikipedia.org/wiki/6-j_symbol>`_ (`SymPy <https://docs.sympy.org/latest/modules/physics/wigner.html#sympy.physics.wigner.wigner_6j>`_, `WMA <https://reference.wolfram.com/language/ref/SixJSymbol.html>`_)


:code:`SixJSymbol` [{:math:`j_1`, :math:`j_2`, :math:`j_3`}, {:math:`j_4`, :math:`j_5`, :math:`j_6`}]
    returns the values of the Wigner 6-:math:`j` symbol.





>>> SixJSymbol[{1, 2, 3}, {1, 2, 3}]
    =

:math:`\frac{1}{105}`



:code:`SixJSymbol`  is symmetric under permutations:

>>> % == SixJSymbol[{3, 2, 1}, {3, 2, 1}]
    =

:math:`\text{True}`


>>> SixJSymbol[{1, 2, 3}, {1, 2, 3}] == SixJSymbol[{2, 1, 3}, {2, 1, 3}]
    =

:math:`\text{True}`



:code:`SixJSymbol`  works with integer and half-integer arguments:

>>> SixJSymbol[{1/2, 1/2, 1}, {5/2, 7/2, 3}]
    =

:math:`-\frac{\sqrt{21}}{21}`



Compare with WMA example:

>>> SixJSymbol[{1, 2, 3}, {2, 1, 2}] == 1 / (5 Sqrt[21])
    =

:math:`\text{True}`



Result 0 returned for unphysical cases:

>>> SixJSymbol[{1, 2, 3}, {4, 5, 12}]
    =

:math:`0`



Arguments must be integer or half integer values:

>>> SixJSymbol[{0.5, 0.5, 1.1},{0.5, 0.5, 1.1}]

    SixJSymbol::6jsymbol_value SixJSymbol values {0.5, 0.5, 1.1} {0.5, 0.5, 1.1} must be integer or half integer and fulfill the triangle relation
    =

:math:`\text{SixJSymbol}\left[\left\{0.5,0.5,1.1\right\},\left\{0.5,0.5,1.1\right\}\right]`


