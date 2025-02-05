TakeSmallestBy
==============

`WMA link <https://reference.wolfram.com/language/ref/TakeSmallestBy.html>`_


:code:`TakeSmallestBy` [:math:`list`, :math:`f`, :math:`n`]
    returns the a sorted list of the :math:`n` smallest items in :math:`list`
    using :math:`f` to retrieve the items' keys to compare them.





For details on how to use the ExcludedForms option, see TakeLargest[].

>>> TakeSmallestBy[{{1, -1}, {10, 100}, {23, 7, 8}, {5, 1}}, Total, 2]
  = {{1, -1}, {5, 1}}
>>> TakeSmallestBy[{"abc", "ab", "x"}, StringLength, 1]
  = {x}
