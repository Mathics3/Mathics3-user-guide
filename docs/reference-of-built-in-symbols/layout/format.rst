Format
======

`WMA link <https://reference.wolfram.com/language/ref/Format.html>`_


:code:`Format` [:math:`expr`]
    holds values specifying how :math:`expr` should be printed.





Assign values to :code:`Format`  to control how particular expressions
should be formatted when printed to the user.

>>> Format[f[x___]] := Infix[{x}, "~"]


>>> f[1, 2, 3]

    =
:math:`1\sim{}2\sim{}3`


>>> f[1]

    =
:math:`1`



Raw objects cannot be formatted:

>>> Format[3] = "three";

    Set::setraw Cannot assign to raw object 3.



Format types must be symbols:

>>> Format[r, a + b] = "r";

    Format::fttp Format type a + b is not a symbol.



Formats must be attached to the head of an expression:

>>> f /: Format[g[f]] = "my f";

    TagSet::tagnfd Tag f not found or too deep for an assigned rule.


