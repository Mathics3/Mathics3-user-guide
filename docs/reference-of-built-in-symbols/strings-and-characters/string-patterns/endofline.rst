EndOfLine
=========

`WMA link <https://reference.wolfram.com/language/ref/EndOfLine.html>`_


:code:`EndOfLine`
    represents the end of a line in a string.





>>> StringReplace["aba\nbba\na\nab", "a" ~~ EndOfLine -> "c"]
  = abc
    bbc
    c
    ab
>>> StringSplit["abc\ndef\nhij", EndOfLine]
  = {abc,
    def,
    hij}
