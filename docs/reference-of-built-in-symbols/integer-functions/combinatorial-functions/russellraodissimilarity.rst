RussellRaoDissimilarity
=======================

`Russel-Rao coefficient <https://en.wikipedia.org/wiki/Qualitative_variation#Russel%E2%80%93Rao_coefficient>`_ (`WMA <https://reference.wolfram.com/language/ref/RusselRaoDissimilarity.html>`_)


:code:`RussellRaoDissimilarity` [:math:`u`, :math:`v`]
    returns the Russell-Rao dissimilarity between the two Boolean       1-D lists :math:`u` and :math:`v`, which is defined as :math:`(n - c_{tt}) / c_{tt}`       where :math:`n` is :math:`len(u)`, :math:`c_{ij}` is       the number of occurrences of :math:`u[k]=i` and :math:`v[k]=j` for :math:`k < n`.





>>> RussellRaoDissimilarity[{1, 0, 1, 1, 0, 1, 1}, {0, 1, 1, 0, 0, 0, 1}]
  = 5 / 7
