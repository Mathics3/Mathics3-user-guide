StringMatchQ
============

`WMA link <https://reference.wolfram.com/language/ref/StringMatchQ.html>`_


:code:`StringMatchQ` ["string", :math:`pattern`]
    checks  is "string" matches :math:`pattern`





>>> StringMatchQ["abc", "abc"]

    =
:math:`\text{True}`


>>> StringMatchQ["abc", "abd"]

    =
:math:`\text{False}`


>>> StringMatchQ["15a94xcZ6", (DigitCharacter | LetterCharacter)..]

    =
:math:`\text{True}`



Use StringMatchQ as an operator

>>> StringMatchQ[LetterCharacter]["a"]

    =
:math:`\text{True}`


