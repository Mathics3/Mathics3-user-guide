Blank
=====

`WMA link <https://reference.wolfram.com/language/ref/Blank.html>`_


:code:`Blank[]`
    same as

:code:`_`
    represents any single expression in a pattern.

:code:`Blank` [:math:`h`]
    same as

:code:`_:math:`h``
    represents any expression with head :math:`h`.





>>> MatchQ[a + b, _]

    =
:math:`\text{True}`



Patterns of the form :code:`_` :math:`h` can be used to test the types of     objects:

>>> MatchQ[42, _Integer]

    =
:math:`\text{True}`


>>> MatchQ[1.0, _Integer]

    =
:math:`\text{False}`


>>> {42, 1.0, x} /. {_Integer -> "integer", _Real -> "real"} // InputForm

    =
:math:`\left\{\text{\`{}\`{}integer''}, \text{\`{}\`{}real''}, x\right\}`



:code:`Blank`  only matches a single expression:

>>> MatchQ[f[1, 2], f[_]]

    =
:math:`\text{False}`


