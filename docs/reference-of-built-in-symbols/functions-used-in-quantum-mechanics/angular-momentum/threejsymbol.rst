ThreeJSymbol
============

`3-j symbol <https://en.wikipedia.org/wiki/3-j_symbol>`_ (`SymPy <https://docs.sympy.org/latest/modules/physics/wigner.html#sympy.physics.wigner.wigner_3j>`_, `WMA <https://reference.wolfram.com/language/ref/ThreeJSymbol.html>`_)


:code:`ThreeJSymbol` [{:math:`j_1`, :math:`m_1`}, {:math:`j_2`, :math:`m_2`}, {:math:`j_3`, :math:`m_3`}]
    returns the values of the Wigner 3-:math:`j` symbol.





Compare with SymPy examples:

>>> ThreeJSymbol[{2, 0}, {6, 0}, {4, 0}]
    =

:math:`\frac{\sqrt{715}}{143}`



:code:`ThreeJSymbol`  is symmetric under permutations:

>>> % == ThreeJSymbol[{2, 0}, {4, 0}, {6, 0}] == ThreeJSymbol[{4, 0}, {2, 0}, {6, 0}]
    =

:math:`\text{True}`


>>> ThreeJSymbol[{2, 0}, {6, 0}, {4, 1}]
    =

:math:`0`



Compare with WMA examples:

>>> ThreeJSymbol[{6, 0}, {4, 0}, {2, 0}] == Sqrt[5 / 143]
    =

:math:`\text{True}`


>>> ThreeJSymbol[{2, 1}, {2, 2}, {4, -3}] == -(1 / (3 Sqrt[2]))
    =

:math:`\text{True}`


>>> ThreeJSymbol[{1/2, -1/2}, {1/2, -1/2}, {1, 1}]
    =

:math:`-\frac{\sqrt{3}}{3}`



Result 0 returned for unphysical cases:

>>> ThreeJSymbol[{1, 2}, {3, 4}, {5, 12}]
    =

:math:`0`



Arguments must be integer or half integer values:

>>> ThreeJSymbol[{2.1, 6}, {4, 0}, {0, 0}]

    ThreeJSymbol::3jsymbol_value ThreeJSymbol values {2.1, 6}, {4, 0}, {0, 0} must be integer or half integer
    =

:math:`\text{ThreeJSymbol}\left[\left\{2.1,6\right\},\left\{4,0\right\},\left\{0,0\right\}\right]`


