Increment
=========

`WMA link <https://reference.wolfram.com/language/ref/Increment.html>`_


:code:`Increment` [:math:`x`]
    same as

:math:`x`:code:`++`
    increments :math:`x` by 1, returning the original value of :math:`x`.





>>> a = 1; a++
  = 1
>>> a
  = 2

Increment a numeric value:

>>> a = 1.5; a++
  = 1.5
>>> a
  = 2.5

Increment a symbolic value:

>>> y = 2 x; y++; y
  = 1 + 2 x

Increment all values in a list:

>>> x = {1, 3, 5}
  = {1, 3, 5}

x++; x
= {2, 4, 6}

Grouping of :code:`Increment` , :code:`PreIncrement`  and :code:`Plus` :

>>> ++++a+++++2//Hold//FullForm
  = Hold[Plus[PreIncrement[PreIncrement[Increment[Increment[a]]]], 2]]

Compare with `PreIncrement </doc/reference-of-built-in-symbols/assignments/in-place-binary-assignment-operator/preincrement>`_ which returns the value before update.

>>> Clear[a, x, y]

