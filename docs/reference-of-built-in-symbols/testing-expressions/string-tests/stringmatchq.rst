StringMatchQ
============

`WMA link <https://reference.wolfram.com/language/ref/StringMatchQ.html>`_


:code:`StringMatchQ` ["string", :math:`pattern`]
    checks  is "string" matches :math:`pattern`





>>> StringMatchQ["abc", "abc"]
  = True
>>> StringMatchQ["abc", "abd"]
  = False
>>> StringMatchQ["15a94xcZ6", (DigitCharacter | LetterCharacter)..]
  = True

Use StringMatchQ as an operator

>>> StringMatchQ[LetterCharacter]["a"]
  = True
