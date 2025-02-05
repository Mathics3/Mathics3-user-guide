Whitespace
==========

`WMA link <https://reference.wolfram.com/language/ref/Whitespace.html>`_

:code:`Whitespace`
    represents a sequence of whitespace characters.





>>> StringMatchQ["\r \n", Whitespace]
  = True
>>> StringSplit["a  \n b \r\n c d", Whitespace]
  = {a, b, c, d}
>>> StringReplace[" this has leading and trailing whitespace \n ", (StartOfString ~~ Whitespace) | (Whitespace ~~ EndOfString) -> ""] <> " removed" // FullForm
  = "this has leading and trailing whitespace removed"
