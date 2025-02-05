WhitespaceCharacter
===================

`WMA link <https://reference.wolfram.com/language/ref/WhitespaceCharacter.html>`_


:code:`WhitespaceCharacter`
    represents a single whitespace character.





>>> StringMatchQ["\n", WhitespaceCharacter]
  = True
>>> StringSplit["a\nb\r\nc\rd", WhitespaceCharacter]
  = {a, b, , c, d}

For sequences of whitespace characters use :code:`Whitespace` :

>>> StringMatchQ[" \n", WhitespaceCharacter]
  = False
>>> StringMatchQ[" \n", Whitespace]
  = True
