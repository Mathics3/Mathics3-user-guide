OpenRead
========

`WMA link <https://reference.wolfram.com/language/ref/OpenRead.html>`_


:code:`OpenRead["file"]`
    opens a file and returns an :code:`InputStream` .





>>> OpenRead["ExampleData/EinsteinSzilLetter.txt", CharacterEncoding->"UTF8"]
    =

:math:`\text{InputStream}\left[\text{ExampleData/EinsteinSzilLetter.txt},17\right]`



The stream must be closed after using it to release the resource:

>>> Close[%];


