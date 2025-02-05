DigitCharacter
==============

`WMA link <https://reference.wolfram.com/language/ref/DigitCharacter.html>`_


:code:`DigitCharacter`
    represents the digits 0-9.





>>> StringMatchQ["1", DigitCharacter]
  = True
>>> StringMatchQ["a", DigitCharacter]
  = False
>>> StringMatchQ["12", DigitCharacter]
  = False
>>> StringMatchQ["123245", DigitCharacter..]
  = True
