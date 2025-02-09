RogersTanimotoDissimilarity
===========================

`Rogers Tanimoto coefficient <https://en.wikipedia.org/wiki/Qualitative_variation#Rogers%E2%80%93Tanimoto_coefficient>`_ (`WMA <https://reference.wolfram.com/language/ref/RogersTanimotoDissimilarity.html>`_)


:code:`RogersTanimotoDissimilarity` [:math:`u`, :math:`v`]
    returns the Rogers-Tanimoto dissimilarity between the two Boolean       1-D lists :math:`u` and :math:`v`, which is defined as       :math:`R / (c_{tt} + c_{ff} + R)` where :math:`n` is :math:`len(u)`, :math:`c_{ij}` is       the number of occurrences of :math:`u[k]=i`, :math:`v[k]=j` for :math:`k<n`,       and :math:`R = 2 (c_{tf} + c_{ft})`.





>>> RogersTanimotoDissimilarity[{1, 0, 1, 1, 0, 1, 1}, {0, 1, 1, 0, 0, 0, 1}]

    =
:math:`\frac{8}{11}`


