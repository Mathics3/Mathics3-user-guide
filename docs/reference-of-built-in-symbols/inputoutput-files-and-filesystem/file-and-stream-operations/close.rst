Close
=====

`WMA link <https://reference.wolfram.com/language/ref/Close.html>`_


:code:`Close` [:math:`obj`]
    Closes a stream or socket.
    
    :math:`obj` can be an :code:`InputStream` , or an :code:`OutputStream`  object, or a :code:`String` .       When :math:`obj` is a string file path, one of the channels associated with it is closed.





>>> Close[StringToStream["123abc"]]

    =
:math:`\text{String}`


>>> file=Close[OpenWrite[]]

    =
:math:`\text{/tmp/tmp50ig32wj}`



Closing a file doesn't delete it from the filesystem.

>>> DeleteFile[file];


>>> Clear[file]
    = `


If two streams are open with the same file, then     a :code:`Close`  by file path closes only one of the streams:

>>> stream1 = OpenRead["ExampleData/numbers.txt"]

    =
:math:`\text{InputStream}\left[\text{ExampleData/numbers.txt},15\right]`


>>> stream2 = OpenRead["ExampleData/numbers.txt"]

    =
:math:`\text{InputStream}\left[\text{ExampleData/numbers.txt},16\right]`


>>> Close["ExampleData/numbers.txt"]

    =
:math:`\text{ExampleData/numbers.txt}`



Usually, the most-recent stream is closed, while the earlier-opened     stream still persists:

>>> Read[stream1]

    =
:math:`8205.79`



However, one of the streams *is* closed:

>>> Read[stream2]

    Read::openx InputStream[ExampleData/numbers.txt, 16] is not open.

    =
:math:`\text{\$Failed}`


>>> Close["ExampleData/numbers.txt"]

    =
:math:`\text{ExampleData/numbers.txt}`


>>> Read[stream1]

    Read::openx InputStream[ExampleData/numbers.txt, 15] is not open.

    =
:math:`\text{\$Failed}`


