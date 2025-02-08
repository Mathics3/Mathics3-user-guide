Increment
=========

`WMA link <https://reference.wolfram.com/language/ref/Increment.html>`_


:code:`Increment` [:math:`x`]
    same as

:math:`x`:code:`++`
    increments :math:`x` by 1, returning the original value of :math:`x`.





>>> a = 1; a++
    =

:math:`1`


>>> a
    =

:math:`2`



Increment a numeric value:

>>> a = 1.5; a++
    =

:math:`1.5`


>>> a
    =

:math:`2.5`



Increment a symbolic value:

>>> y = 2 x; y++; y
    =

:math:`1+2 x`



Increment all values in a list:

>>> x = {1, 3, 5}
    =

:math:`\left\{1,3,5\right\}`



x++; x
= {2, 4, 6}

Grouping of :code:`Increment` , :code:`PreIncrement`  and :code:`Plus` :

>>> ++++a+++++2//Hold//FullForm
    =

:math:`\text{Hold}\left[\text{Plus}\left[\text{PreIncrement}\left[\text{PreIncrement}\left[\text{Increment}\left[\text{Increment}\left[a\right]\right]\right]\right], 2\right]\right]`



Compare with `PreIncrement </doc/reference-of-built-in-symbols/assignments/in-place-binary-assignment-operator/preincrement>`_ which returns the value before update.

>>> Clear[a, x, y]
    = `

