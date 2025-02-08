FileNameJoin
============

`WMA link <https://reference.wolfram.com/language/ref/FileNameJoin.html>`_


:code:`FileNameJoin` [{":math:`dir_1`", ":math:`dir_2`", ...}]
    joins the :math:`dir_i` together into one path.

:code:`FileNameJoin[..., OperatingSystem->"os"]`
    yields a file name in the format for the specified operating system.           Possible choices are "Windows", "MacOSX", and "Unix".





>>> FileNameJoin[{"dir1", "dir2", "dir3"}]
    =

:math:`\text{dir1/dir2/dir3}`


>>> FileNameJoin[{"dir1", "dir2", "dir3"}, OperatingSystem -> "Unix"]
    =

:math:`\text{dir1/dir2/dir3}`


>>> FileNameJoin[{"dir1", "dir2", "dir3"}, OperatingSystem -> "Windows"]
    =

:math:`\text{dir1$\backslash$dir2$\backslash$dir3}`


