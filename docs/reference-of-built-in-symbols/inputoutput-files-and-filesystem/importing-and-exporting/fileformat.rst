FileFormat
==========

`WMA link <https://reference.wolfram.com/language/ref/FileFormat.html>`_


:code:`FileFormat` [":math:`name`"]
    attempts to determine what format :code:`Import`  should use to import specified file.





>>> FileFormat["ExampleData/sunflowers.jpg"]
  = JPEG
>>> FileFormat["ExampleData/EinsteinSzilLetter.txt"]
  = Text
>>> FileFormat["ExampleData/hedy.tif"]
  = TIFF
