SetStreamPosition
=================

`WMA link <https://reference.wolfram.com/language/ref/SetStreamPosition.html>`_


:code:`SetStreamPosition` [:math:`stream`, :math:`n`]
    sets the current position in a stream.





>>> stream = StringToStream["Mathics is cool!"]
  = ...
>>> SetStreamPosition[stream, 8]
  = 8
>>> Read[stream, Word]
  = is
>>> SetStreamPosition[stream, Infinity]
  = 16
