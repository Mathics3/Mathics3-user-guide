MatchingDissimilarity
=====================

`WMA link <https://reference.wolfram.com/language/ref/MatchingDissimilarity.html>`_


:code:`MatchingDissimilarity` [:math:`u`, :math:`v`]
    returns the Matching dissimilarity between the two Boolean       1-D lists :math:`u` and :math:`v`, which is defined as :math:`(c_{tf} + c_{ft}) / n`,       where :math:`n` is len(:math:`u`) and :math:`c_{ij}` is the number of occurrences of       :math:`u[k]=i` and :math:`v[k]=j` for :math:`k < n`.





>>> MatchingDissimilarity[{1, 0, 1, 1, 0, 1, 1}, {0, 1, 1, 0, 0, 0, 1}]

    =
:math:`\frac{4}{7}`


