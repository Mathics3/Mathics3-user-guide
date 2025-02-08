Total
=====

`WMA link <https://reference.wolfram.com/language/ref/Total.html>`_


:code:`Total` [:math:`list`]
    adds all values in :math:`list`.

:code:`Total` [:math:`list`, :math:`n`]
    adds all values up to level :math:`n`.

:code:`Total` [:math:`list`, {:math:`n`}]
    totals only the values at level {:math:`n`}.

:code:`Total` [:math:`list`, {:math:`n_1`, :math:`n_2`}]
    totals at levels {:math:`n_1`, :math:`n_2`}.





>>> Total[{1, 2, 3}]
    =

:math:`6`


>>> Total[{{1, 2, 3}, {4, 5, 6}, {7, 8 ,9}}]
    =

:math:`\left\{12,15,18\right\}`



Total over rows and columns

>>> Total[{{1, 2, 3}, {4, 5, 6}, {7, 8 ,9}}, 2]
    =

:math:`45`



Total over rows instead of columns

>>> Total[{{1, 2, 3}, {4, 5, 6}, {7, 8 ,9}}, {2}]
    =

:math:`\left\{6,15,24\right\}`


