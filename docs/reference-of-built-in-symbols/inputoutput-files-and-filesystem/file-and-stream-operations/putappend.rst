PutAppend
=========

`WMA link <https://reference.wolfram.com/language/ref/PutAppend.html>`_


:code:`:math:`expr` >>> :math:`filename``
    append :math:`expr` to a file.

:code:`PutAppend` [:math:`expr_1`, :math:`expr_2`, ..., ":math:`filename`"]
    write a sequence of expressions to a file.





>>> Put[50!, "factorials"]

>>> FilePrint["factorials"]

>>> PutAppend[10!, 20!, 30!, "factorials"]

>>> FilePrint["factorials"]

>>> 60! >>> "factorials"

>>> FilePrint["factorials"]

>>> "string" >>> factorials

>>> FilePrint["factorials"]

>>> DeleteFile["factorials"];

