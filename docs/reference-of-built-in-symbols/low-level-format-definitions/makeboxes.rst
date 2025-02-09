MakeBoxes
=========

`WMA link <https://reference.wolfram.com/language/ref/MakeBoxes.html>`_


:code:`MakeBoxes` [:math:`expr`]
    is a low-level formatting primitive that converts :math:`expr`
    to box form, without evaluating it.

:code:`\( ... \)`
    directly inputs box objects.





String representation of boxes

>>> \(x \^ 2\)

    =
:math:`\text{SuperscriptBox}\left[\text{x},\text{2}\right]`


>>> \(x \_ 2\)

    =
:math:`\text{SubscriptBox}\left[\text{x},\text{2}\right]`


>>> \( a \+ b \% c\)

    =
:math:`\text{UnderoverscriptBox}\left[\text{a},\text{b},\text{c}\right]`


>>> \( a \& b \% c\)

    =
:math:`\text{UnderoverscriptBox}\left[\text{a},\text{c},\text{b}\right]`


>>> \( \@ 5 \)
    = SqrtBox[5]`

>>> \(x \& y \)

    =
:math:`\text{OverscriptBox}\left[\text{x},\text{y}\right]`


>>> \(x \+ y \)

    =
:math:`\text{UnderscriptBox}\left[\text{x},\text{y}\right]`


>>> \( x \^ 2 \_ 4 \)
    = SuperscriptBox[x, SubscriptBox[2, 4]]`

>>> (a + b)[x]
    = (a + b)[x]`

>>> (a b)[x]
    = (a b)[x]`

>>> (a <> b)[x]
    = (a <> b)[x]`

