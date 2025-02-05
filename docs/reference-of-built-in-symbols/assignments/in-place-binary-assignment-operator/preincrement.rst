PreIncrement
============

`WMA link <https://reference.wolfram.com/language/ref/PreIncrement.html>`_


:code:`PreIncrement` [:math:`x`]
    same as

:code:`++` :math:`x`
    increments :math:`x` by 1, returning the new value of :math:`x`.





:code:`++` :math:`a` is equivalent to :math:`a` :code:`=`  :math:`a` :code:`+ 1` :

>>> a = 2
  = 2
>>> ++a
  = 3
>>> a
  = 3

PreIncrement a numeric value:

>>> a + 1.6
  = 4.6

PreIncrement a symbolic value:

>>> Clear[x, y]

>>> y = x; ++y
  = 1 + x
>>> y
  = 1 + x

Compare with `Increment </doc/reference-of-built-in-symbols/assignments/in-place-binary-assignment-operator/increment>`_ which returns the updated value, and `PreDecrement </doc/reference-of-built-in-symbols/assignments/in-place-binary-assignment-operator/predecrement>`_ which goes the other way.

>>> Clear[a, x, y]

