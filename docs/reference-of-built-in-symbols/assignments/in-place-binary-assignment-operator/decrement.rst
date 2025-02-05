Decrement
=========

`WMA link
 <https://reference.wolfram.com/language/ref/Decrement.html>`_


:code:`Decrement` [:math:`x`]
    same as

:math:`x`:code:`--`
    decrements :math:`x` by 1, returning the original value of :math:`x`.





>>> a = 5; a--
  = 5
>>> a
  = 4

Decrement a numerical value:

>>> a = 1.6; a--; a
  = 0.6

Decrement all values in a list:

>>> a = {1, 3, 5}
  = {1, 3, 5}
>>> a--; a
  = {0, 2, 4}

Compare with `PreDecrement </doc/reference-of-built-in-symbols/assignments/in-place-binary-assignment-operator/predecrement>`_ which returns the value before updating, and `Increment </doc/reference-of-built-in-symbols/assignments/in-place-binary-assignment-operator/increment>`_ which goes the other way.