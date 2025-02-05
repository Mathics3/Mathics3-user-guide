StreamPosition
==============

`WMA link <https://reference.wolfram.com/language/ref/StreamPosition.html>`_


:code:`StreamPosition` [:math:`stream`]
    returns the current position in a stream as an integer.





>>> stream = StringToStream["Mathics is cool!"]
  = ...
>>> Read[stream, Word]
  = Mathics
>>> StreamPosition[stream]
  = 7
