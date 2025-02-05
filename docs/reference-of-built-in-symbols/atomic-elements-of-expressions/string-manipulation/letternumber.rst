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
  = 2

LetterNumber also works with uppercase characters

>>> LetterNumber["B"]
  = 2
>>> LetterNumber["ss2!"]
  = {19, 19, 0, 0}

Get positions of each of the letters in a string:

>>> LetterNumber[Characters["Peccary"]]
  = {16, 5, 3, 3, 1, 18, 25}
>>> LetterNumber[{"P", "Pe", "P1", "eck"}]
  = {16, {16, 5}, {16, 0}, {5, 3, 11}}
>>> LetterNumber["\[Beta]", "Greek"]
  = 2
