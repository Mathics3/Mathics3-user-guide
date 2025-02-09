YuleDissimilarity
=================

`WMA link <https://reference.wolfram.com/language/ref/YuleDissimilarity.html>`_


:code:`YuleDissimilarity` [:math:`u`, :math:`v`]
    returns the Yule dissimilarity between the two Boolean 1-D lists :math:`u`           and :math:`v`, which is defined as :math:`R / (c_{tt} c_{ff} + R / 2)`           where :math:`n` is :math:`len(u)`, :math:`c_{ij}` is the number of occurrences of           :math:`u[k]=i`, :math:`v[k]=j` for :math:`k<n`,           and :math:`R = 2 c_{tf} c_{ft}`.





>>> YuleDissimilarity[{1, 0, 1, 1, 0, 1, 1}, {0, 1, 1, 0, 0, 0, 1}]

    =
:math:`\frac{6}{5}`


