DateDifference
==============

`WMA link <https://reference.wolfram.com/language/ref/DateDifference.html>`_


:code:`DateDifference` [:math:`date_1`, :math:`date_2`]
    returns the difference between :math:`date_1` and :math:`date_2` in days.

:code:`DateDifference` [:math:`date_1`, :math:`date_2`, :math:`unit`]
    returns the difference in the specified :math:`unit`.

:code:`DateDifference` [:math:`date_1`, :math:`date_2`, {:math:`unit_1`, :math:`unit_2`, ...}]
    represents the difference as a list of integer multiples of each :math:`unit`, with any remainder expressed in the smallest unit.





>>> DateDifference[{2042, 1, 4}, {2057, 1, 1}]

    =
:math:`5476`


>>> DateDifference[{1936, 8, 14}, {2000, 12, 1}, "Year"]

    =
:math:`\left\{64.3425,\text{Year}\right\}`


>>> DateDifference[{2010, 6, 1}, {2015, 1, 1}, "Hour"]

    =
:math:`\left\{40200,\text{Hour}\right\}`


>>> DateDifference[{2003, 8, 11}, {2003, 10, 19}, {"Week", "Day"}]

    =
:math:`\left\{\left\{9,\text{Week}\right\},\left\{6,\text{Day}\right\}\right\}`


