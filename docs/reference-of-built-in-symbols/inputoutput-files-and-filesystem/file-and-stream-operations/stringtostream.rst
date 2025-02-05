StringToStream
==============

`WMA link <https://reference.wolfram.com/language/ref/StringToStream.html>`_


:code:`StringToStream` [:math:`string`]
    converts a :math:`string` to an open input stream.





>>> strm = StringToStream["abc 123"]
  = InputStream[String, ...]

The stream must be closed after using it, to release the resource:

>>> Close[strm];

