StreamPosition
==============

`WMA link <https://reference.wolfram.com/language/ref/StreamPosition.html>`_


:code:`StreamPosition` [:math:`stream`]
    returns the current position in a stream as an integer.





>>> stream = StringToStream["Mathics is cool!"]
    =

:math:`\text{InputStream}\left[\text{String},36\right]`


>>> Read[stream, Word]
    =

:math:`\text{Mathics}`


>>> StreamPosition[stream]
    =

:math:`7`


