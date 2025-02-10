DeleteDirectory
===============

`WMA link <https://reference.wolfram.com/language/ref/DeleteDirectory.html>`_


:code:`DeleteDirectory` [":math:`dir`"]
    deletes a directory called :math:`dir`.





>>> dir = CreateDirectory[]

    =
:math:`\text{/tmp/mx1gez4ae}`


>>> DeleteDirectory[dir]


>>> DirectoryQ[dir]

    =
:math:`\text{False}`


>>> Quiet[DeleteDirectory[dir]]
    = $Failed`

