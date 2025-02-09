WriteString
===========

`WMA link <https://reference.wolfram.com/language/ref/WriteString.html>`_


:code:`WriteString` [:math:`stream`, :math:`str_1`, :math:`str_2`, ... ]
    writes the strings to the output stream.





>>> stream = OpenWrite[];


>>> WriteString[stream, "This is a test 1"]


>>> WriteString[stream, "This is also a test 2"]


>>> pathname = Close[stream];


>>> FilePrint[%]

    This is a test 1This is also a test 2


>>> DeleteFile[pathname];


>>> stream = OpenWrite[];


>>> WriteString[stream, "This is a test 1", "This is also a test 2"]


>>> pathname = Close[stream]

    =
:math:`\text{/tmp/tmpmf1eh56m}`


>>> FilePrint[%]

    This is a test 1This is also a test 2


>>> DeleteFile[pathname];



If stream is the string "stdout" or "stderr", writes to the system standard output/ standard error channel:

>>> WriteString["stdout", "Hola"]


