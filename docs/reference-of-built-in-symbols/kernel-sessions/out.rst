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
    =

:math:`42`


>>> %
    =

:math:`42`


>>> 43;


>>> %
    =

:math:`43`


>>> 44
    =

:math:`44`


>>> %1
    =

:math:`42`


>>> %%
    =

:math:`44`


>>> Hold[Out[-1]]
    =

:math:`\text{Hold}\left[\%\right]`


>>> Hold[%4]
    =

:math:`\text{Hold}\left[\text{\%4}\right]`


>>> Out[0]
    =

:math:`\text{Out}\left[0\right]`


>>> 10
    = 10`

>>> Out[-1] + 1
    = 11`

>>> Out[] + 1
    = 12`

