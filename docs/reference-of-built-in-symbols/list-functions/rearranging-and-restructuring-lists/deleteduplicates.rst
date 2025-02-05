DeleteDuplicates
================

`WMA link <https://reference.wolfram.com/language/ref/DeleteDuplicates.html>`_


:code:`DeleteDuplicates` [:math:`list`]
    deletes duplicates from :math:`list`.

:code:`DeleteDuplicates` [:math:`list`, :math:`test`]
    deletes elements from :math:`list` based on whether the function :math:`test` yields           :code:`True`  on pairs of elements.
    
    :code:`DeleteDuplicates`  does not change the order of the remaining elements.





>>> DeleteDuplicates[{1, 7, 8, 4, 3, 4, 1, 9, 9, 2, 1}]
  = {1, 7, 8, 4, 3, 9, 2}
>>> DeleteDuplicates[{3,2,1,2,3,4}, Less]
  = {3, 2, 1}
