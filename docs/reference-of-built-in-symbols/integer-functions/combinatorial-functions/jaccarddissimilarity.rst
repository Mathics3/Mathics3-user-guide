JaccardDissimilarity
====================

`Jaccard index <https://en.wikipedia.org/wiki/Jaccard_index>`_ (`SciPy <https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.jaccard.html>`_, `WMA <https://reference.wolfram.com/language/ref/JaccardDissimilarity.html>`_)

:code:`JaccardDissimilarity` [:math:`u`, :math:`v`]
    returns the Jaccard-Needham dissimilarity between the two Boolean           1-D lists :math:`u` and :math:`v`, which is defined as           :math:`(c_{tf} + c_{ft}) / (c_{tt} + c_{ft} + c_{tf})`, where :math:`n` is           len(:math:`u`) and :math:`c_{ij}` is the number of occurrences of           :math:`u[k]=i` and :math:`v[k]=j` for :math:`k < n`.





>>> JaccardDissimilarity[{1, 0, 1, 1, 0, 1, 1}, {0, 1, 1, 0, 0, 0, 1}]
    =

:math:`\frac{2}{3}`


