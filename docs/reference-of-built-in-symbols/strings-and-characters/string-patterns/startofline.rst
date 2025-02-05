StartOfLine
===========

`WMA link <https://reference.wolfram.com/language/ref/StartOfLine.html>`_


:code:`StartOfLine`
    represents the start of a line in a string.





>>> StringReplace["aba\nbba\na\nab", StartOfLine ~~ "a" -> "c"]
  = cba
    bba
    c
    cb
>>> StringSplit["abc\ndef\nhij", StartOfLine]
  = {abc
    , def
    , hij}
