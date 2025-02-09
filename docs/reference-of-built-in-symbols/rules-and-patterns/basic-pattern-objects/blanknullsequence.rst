BlankNullSequence
=================

`WMA link <https://reference.wolfram.com/language/ref/BlankNullSequence.html>`_


:code:`BlankNullSequence[]`
    same as

:code:`___`
    represents any sequence of expression elements in a pattern,         including an empty sequence.





:code:`BlankNullSequence`  is like :code:`BlankSequence` , except it can match an     empty sequence:

>>> MatchQ[f[], f[___]]

    =
:math:`\text{True}`


