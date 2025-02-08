EndOfLine
=========

`WMA link <https://reference.wolfram.com/language/ref/EndOfLine.html>`_


:code:`EndOfLine`
    represents the end of a line in a string.





>>> StringReplace["aba\nbba\na\nab", "a" ~~ EndOfLine -> "c"]
    =


.. math::
    \text{abc\newline
    bbc\newline
    c\newline
    ab}



>>> StringSplit["abc\ndef\nhij", EndOfLine]
    =


.. math::
    \left\{\text{abc},\text{\newline
    def},\text{\newline
    hij}\right\}



