ImportString
============

`WMA link <https://reference.wolfram.com/language/ref/ImportString.html>`_


:code:`ImportString` [":math:`data`", ":math:`format`"]
    imports data in the specified format from a string.

:code:`ImportString` [":math:`file`", :math:`elements`]
    imports the specified elements from a string.

:code:`ImportString` [":math:`data`"]
    attempts to determine the format of the string from its content.





>>> str = "Hello!\n    This is a testing text\n";


>>> ImportString[str, "Elements"]

    =
:math:`\left\{\text{Data},\text{Lines},\text{Plaintext},\text{String},\text{Words}\right\}`


>>> ImportString[str, "Lines"]

    =
:math:`\left\{\text{Hello!},\text{    This is a testing text}\right\}`


