LetterCharacter
===============

`WMA link <https://reference.wolfram.com/language/ref/LetterCharacter.html>`_


:code:`LetterCharacter`
    represents letters.





>>> StringMatchQ[#, LetterCharacter] & /@ {"a", "1", "A", " ", "."}
  = {True, False, True, False, False}

LetterCharacter also matches unicode characters.

>>> StringMatchQ["\[Lambda]", LetterCharacter]
  = True
