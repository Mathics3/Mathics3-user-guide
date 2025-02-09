EndOfString
===========

`WMA link <https://reference.wolfram.com/language/ref/EndOfString.html>`_


:code:`EndOfString`
    represents the end of a string.





Test whether strings end with "e":

>>> StringMatchQ[#, __ ~~ "e" ~~ EndOfString] &/@ {"apple", "banana", "artichoke"}

    =
:math:`\left\{\text{True},\text{False},\text{True}\right\}`


>>> StringReplace["aab\nabb", "b" ~~ EndOfString -> "c"]

    =

.. math::
    \text{aab\newline
    abc}



