LetterNumber
============

`WMA link <https://reference.wolfram.com/language/ref/LetterNumber.html>`_

:code:`LetterNumber` [:math:`c`]
    returns the position of the character :math:`c` in the English alphabet.

:code:`LetterNumber["string"]`
    returns a list of the positions of characters in string.

:code:`LetterNumber` ["string", :math:`alpha`]
    returns a list of the positions of characters in string, regarding the alphabet :math:`alpha`.





>>> LetterNumber["b"]

    =
:math:`2`



LetterNumber also works with uppercase characters

>>> LetterNumber["B"]

    =
:math:`2`


>>> LetterNumber["ss2!"]

    =
:math:`\left\{19,19,0,0\right\}`



Get positions of each of the letters in a string:

>>> LetterNumber[Characters["Peccary"]]

    =
:math:`\left\{16,5,3,3,1,18,25\right\}`


>>> LetterNumber[{"P", "Pe", "P1", "eck"}]

    =
:math:`\left\{16,\left\{16,5\right\},\left\{16,0\right\},\left\{5,3,11\right\}\right\}`


>>> LetterNumber["\[Beta]", "Greek"]

    =
:math:`2`


