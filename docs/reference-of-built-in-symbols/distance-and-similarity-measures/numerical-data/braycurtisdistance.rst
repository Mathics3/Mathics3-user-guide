BrayCurtisDistance
==================

`Bray-Curtis Dissimilarity <https://en.wikipedia.org/wiki/Bray%E2%80%93Curtis_dissimilarity>`_     (`WMA <https://reference.wolfram.com/language/ref/BrayCurtisDistance.html>`_)


:code:`BrayCurtisDistance` [:math:`u`, :math:`v`]
    returns the Bray-Curtis distance between :math:`u` and :math:`v`.





The Bray-Curtis distance is equivalent to :code:`Total[Abs[u-v]]/Total[Abs[u+v]]` .

>>> BrayCurtisDistance[-7, 5]

    =
:math:`6`


>>> BrayCurtisDistance[{-1, -1}, {10, 10}]

    =
:math:`\frac{11}{9}`


