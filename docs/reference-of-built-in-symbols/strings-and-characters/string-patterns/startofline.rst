StartOfLine
===========

`WMA link <https://reference.wolfram.com/language/ref/StartOfLine.html>`_


:code:`StartOfLine`
    represents the start of a line in a string.





>>> StringReplace["aba\nbba\na\nab", StartOfLine ~~ "a" -> "c"]
    =


.. math::
    \text{cba\newline
    bba\newline
    c\newline
    cb}



>>> StringSplit["abc\ndef\nhij", StartOfLine]
    =


.. math::
    \left\{\text{abc\newline
    },\text{def\newline
    },\text{hij}\right\}



