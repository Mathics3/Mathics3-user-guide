Prefix
======

`WMA link <https://reference.wolfram.com/language/ref/Prefix.html>`_


:code:`:math:`f` @ :math:`x``
    is equivalent to :code:`:math:`f`[:math:`x`]` .





>>> a @ b

    =
:math:`a\left[b\right]`


>>> a @ b @ c

    =
:math:`a\left[b\left[c\right]\right]`


>>> Format[p[x_]] := Prefix[{x}, "*"]


>>> p[3]

    =
:math:`*3`


>>> Format[q[x_]] := Prefix[{x}, "~", 350]


>>> q[a+b]

    =
:math:`\sim{}\left(a+b\right)`


>>> q[a*b]

    =
:math:`\sim{}a b`


>>> q[a]+b

    =
:math:`b+\sim{}a`



The prefix operator :code:`@`  is parsed to an expression before evaluation:

>>> Hold[a @ b @ c @ d @ e @ f @ x]

    =
:math:`\text{Hold}\left[a\left[b\left[c\left[d\left[e\left[f\left[x\right]\right]\right]\right]\right]\right]\right]`


