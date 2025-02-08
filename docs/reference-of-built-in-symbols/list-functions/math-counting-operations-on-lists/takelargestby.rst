TakeLargestBy
=============

`WMA link <https://reference.wolfram.com/language/ref/TakeLargestBy.html>`_


:code:`TakeLargestBy` [:math:`list`, :math:`f`, :math:`n`]
    returns the a sorted list of the :math:`n` largest items in :math:`list`
    using :math:`f` to retrieve the items' keys to compare them.





For details on how to use the ExcludedForms option, see TakeLargest[].

>>> TakeLargestBy[{{1, -1}, {10, 100}, {23, 7, 8}, {5, 1}}, Total, 2]
    =

:math:`\left\{\left\{10,100\right\},\left\{23,7,8\right\}\right\}`


>>> TakeLargestBy[{"abc", "ab", "x"}, StringLength, 1]
    =

:math:`\left\{\text{abc}\right\}`


