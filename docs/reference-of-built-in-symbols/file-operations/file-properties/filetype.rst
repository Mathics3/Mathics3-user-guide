FileType
========

`WMA link <https://reference.wolfram.com/language/ref/FileType.html>`_


:code:`FileType` [":math:`file`"]
    gives the type of a file, a string. This is typically :code:`File` , :code:`Directory`            or :code:`None` .





>>> FileType["ExampleData/sunflowers.jpg"]
  = File
>>> FileType["ExampleData"]
  = Directory
>>> FileType["ExampleData/nonexistent"]
  = None
