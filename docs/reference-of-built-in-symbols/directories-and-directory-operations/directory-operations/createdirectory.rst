CreateDirectory
===============

`WMA link <https://reference.wolfram.com/language/ref/CreateDirectory.html>`_


:code:`CreateDirectory` [":math:`dir`"]
    creates a directory called :math:`dir`.

:code:`CreateDirectory[]`
    creates a temporary directory.





>>> dir = CreateDirectory[]

    =
:math:`\text{/tmp/mf\_d9ug41}`


>>> DirectoryQ[dir]
    = True`

>>> DeleteDirectory[dir]
    = `

