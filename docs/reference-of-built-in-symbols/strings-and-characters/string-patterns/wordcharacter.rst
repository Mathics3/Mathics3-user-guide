WordCharacter
=============

`WMA link <https://reference.wolfram.com/language/ref/WordCharacter.html>`_


:code:`WordCharacter`
    represents a single letter or digit character.





>>> StringMatchQ[#, WordCharacter] &/@ {"1", "a", "A", ",", " "}
  = {True, True, True, False, False}

Test whether a string is alphanumeric:

>>> StringMatchQ["abc123DEF", WordCharacter..]
  = True
>>> StringMatchQ["$b;123", WordCharacter..]
  = False
