OpenRead
========

`WMA link <https://reference.wolfram.com/language/ref/OpenRead.html>`_


:code:`OpenRead["file"]`
    opens a file and returns an :code:`InputStream` .





>>> OpenRead["ExampleData/EinsteinSzilLetter.txt", CharacterEncoding->"UTF8"]
  = InputStream[...]

The stream must be closed after using it to release the resource:

>>> Close[%];

