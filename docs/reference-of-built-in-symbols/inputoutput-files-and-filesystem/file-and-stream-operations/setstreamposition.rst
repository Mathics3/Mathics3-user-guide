SetStreamPosition
=================

`WMA link <https://reference.wolfram.com/language/ref/SetStreamPosition.html>`_


:code:`SetStreamPosition` [:math:`stream`, :math:`n`]
    sets the current position in a stream.





>>> stream = StringToStream["Mathics is cool!"]

    =
:math:`\text{InputStream}\left[\text{String},33\right]`


>>> SetStreamPosition[stream, 8]

    =
:math:`8`


>>> Read[stream, Word]

    =
:math:`\text{is}`


>>> SetStreamPosition[stream, Infinity]

    =
:math:`16`


