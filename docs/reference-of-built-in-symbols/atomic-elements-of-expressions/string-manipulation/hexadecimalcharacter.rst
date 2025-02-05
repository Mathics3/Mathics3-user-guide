HexadecimalCharacter
====================

`WMA link <https://reference.wolfram.com/language/ref/HexadecimalCharacter.html>`_


:code:`HexadecimalCharacter`
    represents the characters 0-9, a-f and A-F.





>>> StringMatchQ[#, HexadecimalCharacter] & /@ {"a", "1", "A", "x", "H", " ", "."}
  = {True, True, True, False, False, False, False}
