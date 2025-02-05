Format
======

`WMA link <https://reference.wolfram.com/language/ref/Format.html>`_


:code:`Format` [:math:`expr`]
    holds values specifying how :math:`expr` should be printed.





Assign values to :code:`Format`  to control how particular expressions
should be formatted when printed to the user.

>>> Format[f[x___]] := Infix[{x}, "~"]

>>> f[1, 2, 3]
  = 1 ~ 2 ~ 3
>>> f[1]
  = 1

Raw objects cannot be formatted:

>>> Format[3] = "three";


Format types must be symbols:

>>> Format[r, a + b] = "r";


Formats must be attached to the head of an expression:

>>> f /: Format[g[f]] = "my f";

