BlankSequence
=============

`WMA link <https://reference.wolfram.com/language/ref/BlankSequence.html>`_


:code:`BlankSequence[]`
    same as

:code:`__`
    represents any non-empty sequence of expression elements in         a pattern.

:code:`BlankSequence` [:math:`h`]
    same as

:code:`__:math:`h``
    represents any sequence of elements, all of which have head :math:`h`.





Use a :code:`BlankSequence`  pattern to stand for a non-empty sequence of     arguments:

>>> MatchQ[f[1, 2, 3], f[__]]
    =

:math:`\text{True}`


>>> MatchQ[f[], f[__]]
    =

:math:`\text{False}`



:code:`__` :math:`h` will match only if all elements have head :math:`h`:

>>> MatchQ[f[1, 2, 3], f[__Integer]]
    =

:math:`\text{True}`


>>> MatchQ[f[1, 2.0, 3], f[__Integer]]
    =

:math:`\text{False}`



The value captured by a named :code:`BlankSequence`  pattern is a     :code:`Sequence`  object:

>>> f[1, 2, 3] /. f[x__] -> x
    =

:math:`\text{Sequence}\left[1,2,3\right]`


