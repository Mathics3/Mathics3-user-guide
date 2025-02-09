LetterCharacter
===============

`WMA link <https://reference.wolfram.com/language/ref/LetterCharacter.html>`_


:code:`LetterCharacter`
    represents letters.





>>> StringMatchQ[#, LetterCharacter] & /@ {"a", "1", "A", " ", "."}

    =
:math:`\left\{\text{True},\text{False},\text{True},\text{False},\text{False}\right\}`



LetterCharacter also matches unicode characters.

>>> StringMatchQ["\[Lambda]", LetterCharacter]

    =
:math:`\text{True}`


