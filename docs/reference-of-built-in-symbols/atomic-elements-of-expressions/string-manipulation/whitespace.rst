Whitespace
==========

`WMA link <https://reference.wolfram.com/language/ref/Whitespace.html>`_

:code:`Whitespace`
    represents a sequence of whitespace characters.





>>> StringMatchQ["\r \n", Whitespace]

    =
:math:`\text{True}`


>>> StringSplit["a  \n b \r\n c d", Whitespace]

    =
:math:`\left\{\text{a},\text{b},\text{c},\text{d}\right\}`


>>> StringReplace[" this has leading and trailing whitespace \n ", (StartOfString ~~ Whitespace) | (Whitespace ~~ EndOfString) -> ""] <> " removed" // FullForm

    =
:math:`\text{\`{}\`{}this has leading and trailing whitespace removed''}`


