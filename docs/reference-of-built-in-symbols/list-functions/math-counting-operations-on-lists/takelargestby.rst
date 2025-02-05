TakeLargestBy
=============

`WMA link <https://reference.wolfram.com/language/ref/TakeLargestBy.html>`_


:code:`TakeLargestBy` [:math:`list`, :math:`f`, :math:`n`]
    returns the a sorted list of the :math:`n` largest items in :math:`list`
    using :math:`f` to retrieve the items' keys to compare them.





For details on how to use the ExcludedForms option, see TakeLargest[].

>>> TakeLargestBy[{{1, -1}, {10, 100}, {23, 7, 8}, {5, 1}}, Total, 2]
  = {{10, 100}, {23, 7, 8}}
>>> TakeLargestBy[{"abc", "ab", "x"}, StringLength, 1]
  = {abc}
