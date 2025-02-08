FileNameDrop
============

`WMA link <https://reference.wolfram.com/language/ref/FileNameDrop.html>`_


:code:`FileNameDrop` [":math:`path`", :math:`n`]
    drops the first :math:`n` path elements in the file name :math:`path`.

:code:`FileNameDrop` [":math:`path`", -:math:`n`]
    drops the last :math:`n` path elements in the file name :math:`path`.

:code:`FileNameDrop` [":math:`path`", {:math:`m`, :math:`n`}]
    drops elements :math:`m` through :math:`n` path elements in the file name :math:`path`.

:code:`FileNameDrop` [":math:`path`"]
    drops the last path elements in the file name :math:`path`.





>>> path = FileNameJoin[{"a","b","c"}]
    =

:math:`\text{a/b/c}`


>>> FileNameDrop[path, -1]
    =

:math:`\text{a/b}`



A shorthand for the above:

>>> FileNameDrop[path]
    =

:math:`\text{a/b}`


