WhitespaceCharacter
===================

`WMA link <https://reference.wolfram.com/language/ref/WhitespaceCharacter.html>`_


:code:`WhitespaceCharacter`
    represents a single whitespace character.





>>> StringMatchQ["\n", WhitespaceCharacter]
    =

:math:`\text{True}`


>>> StringSplit["a\nb\r\nc\rd", WhitespaceCharacter]
    =

:math:`\left\{\text{a},\text{b},\text{},\text{c},\text{d}\right\}`



For sequences of whitespace characters use :code:`Whitespace` :

>>> StringMatchQ[" \n", WhitespaceCharacter]
    =

:math:`\text{False}`


>>> StringMatchQ[" \n", Whitespace]
    =

:math:`\text{True}`


