Max
===

`WMA link <https://reference.wolfram.com/language/ref/Max.html>`_


:code:`Max` [:math:`e_1`, :math:`e_2`, ..., :math:`e_i`]
    returns the expression with the greatest value among the :math:`e_i`.





Maximum of a series of values:

>>> Max[4, -8, 1]
    =

:math:`4`


>>> Max[E - Pi, Pi, E + Pi, 2 E]
    =

:math:`E+ \pi`



:code:`Max`  flattens lists in its arguments:

>>> Max[{1,2},3,{-3,3.5,-Infinity},{{1/2}}]
    =

:math:`3.5`



:code:`Max`  with symbolic arguments remains in symbolic form:

>>> Max[x, y]
    =

:math:`\text{Max}\left[x,y\right]`


>>> Max[5, x, -3, y, 40]
    =

:math:`\text{Max}\left[40,x,y\right]`



With no arguments, :code:`Max`  gives :code:`-Infinity` :

>>> Max[]
    =

:math:`-\infty`



:code:`Max`  does not compare strings or symbols:

>>> Max[-1.37, 2, "a", b]
    =

:math:`\text{Max}\left[2,\text{a},b\right]`


