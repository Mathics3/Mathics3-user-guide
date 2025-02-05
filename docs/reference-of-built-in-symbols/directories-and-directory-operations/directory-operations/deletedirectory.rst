DeleteDirectory
===============

`WMA link <https://reference.wolfram.com/language/ref/DeleteDirectory.html>`_


:code:`DeleteDirectory` [":math:`dir`"]
    deletes a directory called :math:`dir`.





>>> dir = CreateDirectory[]
  = ...
>>> DeleteDirectory[dir]

>>> DirectoryQ[dir]
  = False
>>> Quiet[DeleteDirectory[dir]]
  = $Failed
