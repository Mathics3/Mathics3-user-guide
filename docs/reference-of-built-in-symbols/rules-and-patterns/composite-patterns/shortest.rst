Shortest
========

`WMA link <https://reference.wolfram.com/language/ref/Shortest.html>`_


:code:`Shortest` [:math:`pat`]
    is a pattern object that matches the shortest sequence consistent with the pattern :math:`pat`.





>>> StringCases["aabaaab", Shortest["a" ~~ __ ~~ "b"]]
    =

:math:`\left\{\text{aab},\text{aaab}\right\}`


>>> StringCases["aabaaab", Shortest[RegularExpression["a+b"]]]
    =

:math:`\left\{\text{aab},\text{aaab}\right\}`


