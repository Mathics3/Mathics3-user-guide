Out
===

`WMA <https://reference.wolfram.com/language/ref/$Out>`_

:code:`%:math:`k``  or :code:`Out` [:math:`k`]
    gives the result of the :math:`k`-th input line.

:code:`%`
    gives the last result.

:code:`` %%'
    gives the result before the previous input line.





>>> 42
  = 42
>>> %
  = 42
>>> 43;

>>> %
  = 43
>>> 44
  = 44
>>> %1
  = 42
>>> %%
  = 44
>>> Hold[Out[-1]]
  = Hold[%]
>>> Hold[%4]
  = Hold[%4]
>>> Out[0]
  = Out[0]
>>> 10
  = 10
>>> Out[-1] + 1
  = 11
>>> Out[] + 1
  = 12
