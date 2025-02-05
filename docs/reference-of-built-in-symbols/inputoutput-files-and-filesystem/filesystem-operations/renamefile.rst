RenameFile
==========

`WMA link <https://reference.wolfram.com/language/ref/RenameFile.html>`_


:code:`RenameFile` [":math:`file_1`", ":math:`file_2`"]
    renames :math:`file_1` to :math:`file_2`.





>>> CopyFile["ExampleData/sunflowers.jpg", "MathicsSunflowers.jpg"]
  = MathicsSunflowers.jpg
>>> RenameFile["MathicsSunflowers.jpg", "MathicsSunnyFlowers.jpg"]
  = MathicsSunnyFlowers.jpg
>>> DeleteFile["MathicsSunnyFlowers.jpg"]

