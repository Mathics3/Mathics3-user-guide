Unevaluated
===========

`WMA link <https://reference.wolfram.com/language/ref/Unevaluated.html>`_


:code:`Unevaluated` [:math:`expr`]
    temporarily leaves :math:`expr` in an unevaluated form when it
    appears as a function argument.





:code:`Unevaluated`  is automatically removed when function arguments are
evaluated:

>>> Sqrt[Unevaluated[x]]

    =
:math:`\sqrt{x}`


>>> Length[Unevaluated[1+2+3+4]]

    =
:math:`4`



:code:`Unevaluated`  has attribute :code:`HoldAllComplete` :

>>> Attributes[Unevaluated]

    =
:math:`\left\{\text{HoldAllComplete},\text{Protected}\right\}`



:code:`Unevaluated`  is maintained for arguments to non-executed functions:

>>> f[Unevaluated[x]]

    =
:math:`f\left[\text{Unevaluated}\left[x\right]\right]`



Likewise, its kept in flattened arguments and sequences:

>>> Attributes[f] = {Flat};


>>> f[a, Unevaluated[f[b, c]]]

    =
:math:`f\left[a,\text{Unevaluated}\left[b\right],\text{Unevaluated}\left[c\right]\right]`


>>> g[a, Sequence[Unevaluated[b], Unevaluated[c]]]

    =
:math:`g\left[a,\text{Unevaluated}\left[b\right],\text{Unevaluated}\left[c\right]\right]`



However, unevaluated sequences are kept:

>>> g[Unevaluated[Sequence[a, b, c]]]

    =
:math:`g\left[\text{Unevaluated}\left[\text{Sequence}\left[a,b,c\right]\right]\right]`


