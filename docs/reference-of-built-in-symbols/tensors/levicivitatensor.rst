LeviCivitaTensor
================

`Levi-Civita tensor <https://en.wikipedia.org/wiki/Levi-Civita_symbol>`_     (`WMA link <https://reference.wolfram.com/language/ref/LeviCivitaTensor.html>`_)


:code:`LeviCivitaTensor` [:math:`d`]
    gives the :math:`d`-dimensional Levi-Civita totally antisymmetric tensor.





>>> LeviCivitaTensor[3]
  = SparseArray[Automatic, {3, 3, 3}, 0, {{1, 2, 3} -> 1, {1, 3, 2} -> -1, {2, 1, 3} -> -1, {2, 3, 1} -> 1, {3, 1, 2} -> 1, {3, 2, 1} -> -1}]
>>> LeviCivitaTensor[3, List]
  = {{{0, 0, 0}, {0, 0, 1}, {0, -1, 0}}, {{0, 0, -1}, {0, 0, 0}, {1, 0, 0}}, {{0, 1, 0}, {-1, 0, 0}, {0, 0, 0}}}
