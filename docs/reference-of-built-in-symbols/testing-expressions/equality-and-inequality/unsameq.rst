UnsameQ
=======

`WMA link <https://reference.wolfram.com/language/ref/UnsameQ.html>`_


:code:`UnsameQ` [:math:`x`, :math:`y`]
    same as

:code:`:math:`x` =!= :math:`y``
    returns :code:`True`  if :math:`x` and :math:`y` are not structurally identical.
    Commutative properties apply, so if :math:`x` =!= :math:`y`, then :math:`y` =!= :math:`x`.





>>> a =!= a
  = False
>>> 1 =!= 1.
  = True

UnsameQ accepts any number of arguments and returns True if all expressions
are structurally distinct:

>>> 1 =!= 2 =!= 3 =!= 4
  = True

UnsameQ returns False if any expression is identical to another:

>>> 1 =!= 2 =!= 1 =!= 4
  = False

UnsameQ[] and UnsameQ[expr] return True:

>>> UnsameQ[]
  = True
>>> UnsameQ[expr]
  = True
