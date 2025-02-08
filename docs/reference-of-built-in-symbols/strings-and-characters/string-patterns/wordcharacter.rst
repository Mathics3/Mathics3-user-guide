WordCharacter
=============

`WMA link <https://reference.wolfram.com/language/ref/WordCharacter.html>`_


:code:`WordCharacter`
    represents a single letter or digit character.





>>> StringMatchQ[#, WordCharacter] &/@ {"1", "a", "A", ",", " "}
    =

:math:`\left\{\text{True},\text{True},\text{True},\text{False},\text{False}\right\}`



Test whether a string is alphanumeric:

>>> StringMatchQ["abc123DEF", WordCharacter..]
    =

:math:`\text{True}`


>>> StringMatchQ["$b;123", WordCharacter..]
    =

:math:`\text{False}`


