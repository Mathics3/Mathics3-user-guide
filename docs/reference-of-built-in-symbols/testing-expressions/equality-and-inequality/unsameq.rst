UnsameQ
=======

`WMA link <https://reference.wolfram.com/language/ref/UnsameQ.html>`_


:code:`UnsameQ` [:math:`x`, :math:`y`]
    same as

:code:`:math:`x` =!= :math:`y``
    returns :code:`True`  if :math:`x` and :math:`y` are not structurally identical.
    Commutative properties apply, so if :math:`x` =!= :math:`y`, then :math:`y` =!= :math:`x`.





>>> a =!= a

    =
:math:`\text{False}`


>>> 1 =!= 1.

    =
:math:`\text{True}`



UnsameQ accepts any number of arguments and returns True if all expressions
are structurally distinct:

>>> 1 =!= 2 =!= 3 =!= 4

    =
:math:`\text{True}`



UnsameQ returns False if any expression is identical to another:

>>> 1 =!= 2 =!= 1 =!= 4

    =
:math:`\text{False}`



UnsameQ[] and UnsameQ[expr] return True:

>>> UnsameQ[]

    =
:math:`\text{True}`


>>> UnsameQ[expr]

    =
:math:`\text{True}`


