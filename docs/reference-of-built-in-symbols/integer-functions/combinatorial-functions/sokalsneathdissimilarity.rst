SokalSneathDissimilarity
========================

`Snokal-Sneath coefficient <https://en.wikipedia.org/wiki/Qualitative_variation#Sokal%E2%80%93Sneath_coefficient>`_ (`WMA <https://reference.wolfram.com/language/ref/SokalSneathDissimilarity.html>`_)


:code:`SokalSneathDissimilarity` [:math:`u`, :math:`v`]
    returns the Sokal-Sneath dissimilarity between the two Boolean       1-D lists :math:`u` and :math:`v`, which is defined as :math:`R / (c_{tt} + R)` where       :math:`n` is :math:`len(u)`, :math:`c_{ij}` is the number of occurrences of       :math:`u[k]=i`, :math:`v[k]=j` for :math:`k < n`,       and :math:`R = 2 (c_{tf} + c_{ft})`.





>>> SokalSneathDissimilarity[{1, 0, 1, 1, 0, 1, 1}, {0, 1, 1, 0, 0, 0, 1}]
    =

:math:`\frac{4}{5}`


