SixJSymbol
==========

`6-j symbol <https://en.wikipedia.org/wiki/6-j_symbol>`_ (`SymPy <https://docs.sympy.org/latest/modules/physics/wigner.html#sympy.physics.wigner.wigner_6j>`_, `WMA <https://reference.wolfram.com/language/ref/SixJSymbol.html>`_)


:code:`SixJSymbol` [{:math:`j_1`, :math:`j_2`, :math:`j_3`}, {:math:`j_4`, :math:`j_5`, :math:`j_6`}]
    returns the values of the Wigner 6-:math:`j` symbol.





>>> SixJSymbol[{1, 2, 3}, {1, 2, 3}]
  = 1 / 105

:code:`SixJSymbol`  is symmetric under permutations:

>>> % == SixJSymbol[{3, 2, 1}, {3, 2, 1}]
  = True
>>> SixJSymbol[{1, 2, 3}, {1, 2, 3}] == SixJSymbol[{2, 1, 3}, {2, 1, 3}]
  = True

:code:`SixJSymbol`  works with integer and half-integer arguments:

>>> SixJSymbol[{1/2, 1/2, 1}, {5/2, 7/2, 3}]
  = -Sqrt[21] / 21

Compare with WMA example:

>>> SixJSymbol[{1, 2, 3}, {2, 1, 2}] == 1 / (5 Sqrt[21])
  = True

Result 0 returned for unphysical cases:

>>> SixJSymbol[{1, 2, 3}, {4, 5, 12}]
  = 0

Arguments must be integer or half integer values:

>>> SixJSymbol[{0.5, 0.5, 1.1},{0.5, 0.5, 1.1}]
  = SixJSymbol[{0.5, 0.5, 1.1}, {0.5, 0.5, 1.1}]
