StartOfString
=============

`WMA link <https://reference.wolfram.com/language/ref/StartOfString.html>`_


:code:`StartOfString`
    represents the start of a string.





Test whether strings start with "a":

>>> StringMatchQ[#, StartOfString ~~ "a" ~~ __] &/@ {"apple", "banana", "artichoke"}
    =

:math:`\left\{\text{True},\text{False},\text{True}\right\}`


>>> StringReplace["aba\nabb", StartOfString ~~ "a" -> "c"]
    =


.. math::
    \text{cba\newline
    abb}



