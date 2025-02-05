DeleteFile
==========

`WMA link <https://reference.wolfram.com/language/ref/DeleteFile.html>`_


:code:`Delete` [":math:`file`"]
    deletes :math:`file`.

:code:`Delete` [{":math:`file_1`", ":math:`file_2`", ...}]
    deletes a list of files.





>>> CopyFile["ExampleData/sunflowers.jpg", "MathicsSunflowers.jpg"];

>>> DeleteFile["MathicsSunflowers.jpg"]

>>> CopyFile["ExampleData/sunflowers.jpg", "MathicsSunflowers1.jpg"];

>>> CopyFile["ExampleData/sunflowers.jpg", "MathicsSunflowers2.jpg"];

>>> DeleteFile[{"MathicsSunflowers1.jpg", "MathicsSunflowers2.jpg"}]

