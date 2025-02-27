Infix
=====

`WMA link <https://reference.wolfram.com/language/ref/Infix.html>`_


:code:`Infix` [:math:`expr`, :math:`oper`, :math:`prec`, :math:`assoc`]
    displays :math:`expr` with the infix operator :math:`oper`, with precedence :math:`prec` and associativity :math:`assoc`.





:code:`Infix`  can be used with :code:`Format`  to display certain forms with
user-defined infix notation:

>>> Format[g[x_, y_]] := Infix[{x, y}, "#", 350, Left]


>>> g[a, g[b, c]]

    =
:math:`a\#\left(b\#c\right)`


>>> g[g[a, b], c]

    =
:math:`a\#b\#c`


>>> g[a + b, c]

    =
:math:`\left(a+b\right)\#c`


>>> g[a * b, c]

    =
:math:`a b\#c`


>>> g[a, b] + c

    =
:math:`c+a\#b`


>>> g[a, b] * c

    =
:math:`c \left(a\#b\right)`


>>> Infix[{a, b, c}, {"+", "-"}]

    =
:math:`a+b-c`


