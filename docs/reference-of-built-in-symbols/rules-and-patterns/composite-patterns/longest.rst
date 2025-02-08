Longest
=======

`WMA link <https://reference.wolfram.com/language/ref/Longest.html>`_


:code:`Longest` [:math:`pat`]
    is a pattern object that matches the longest sequence consistent       with the pattern :math:`pat`.





>>> StringCases["aabaaab", Longest["a" ~~ __ ~~ "b"]]
    =

:math:`\left\{\text{aabaaab}\right\}`


>>> StringCases["aabaaab", Longest[RegularExpression["a+b"]]]
    =

:math:`\left\{\text{aab},\text{aaab}\right\}`


