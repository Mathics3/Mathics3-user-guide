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
  = {Data, Lines, Plaintext, String, Words}
>>> ImportString[str, "Lines"]
  = ...
