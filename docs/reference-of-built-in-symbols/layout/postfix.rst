Postfix
=======

`WMA link <https://reference.wolfram.com/language/ref/Postfix.html>`_


:code:`:math:`x` // :math:`f``
    is equivalent to :code:`:math:`f`[:math:`x`]` .





>>> b // a
    =

:math:`a\left[b\right]`


>>> c // b // a
    =

:math:`a\left[b\left[c\right]\right]`



The postfix operator :code:`//`  is parsed to an expression before evaluation:

>>> Hold[x // a // b // c // d // e // f]
    =

:math:`\text{Hold}\left[f\left[e\left[d\left[c\left[b\left[a\left[x\right]\right]\right]\right]\right]\right]\right]`


