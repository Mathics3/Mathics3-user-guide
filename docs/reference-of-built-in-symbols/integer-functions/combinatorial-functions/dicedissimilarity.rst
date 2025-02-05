DiceDissimilarity
=================

`Sørensen–Dice coefficient <https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient>`_ (`Sympy <https://docs.scipy.org/doc/scipy/search.html>`_, `DiceDissimilarity <https://reference.wolfram.com/language/ref/DiceDissimilarity.html>`_)

:code:`DiceDissimilarity` [:math:`u`, :math:`v`]
    returns the Dice dissimilarity between the two Boolean 1-D lists :math:`u` and :math:`v`.
    This is defined as (:math:`c_{tf}` + :math:`c_{ft}`) / (2 * :math:`c_{tt}` + :math:`c_{ft}` + :math:`c_{tf}`).
    :math:`n` is len(:math:`u`) and :math:`c_{ij}` is the number of occurrences of :math:`u[k]=i` and :math:`v[k]=j` for :math:`k < n`.





>>> DiceDissimilarity[{1, 0, 1, 1, 0, 1, 1}, {0, 1, 1, 0, 0, 0, 1}]
  = 1 / 2
