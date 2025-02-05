StartOfString
=============

`WMA link <https://reference.wolfram.com/language/ref/StartOfString.html>`_


:code:`StartOfString`
    represents the start of a string.





Test whether strings start with "a":

>>> StringMatchQ[#, StartOfString ~~ "a" ~~ __] &/@ {"apple", "banana", "artichoke"}
  = {True, False, True}
>>> StringReplace["aba\nabb", StartOfString ~~ "a" -> "c"]
  = cba
    abb
