RepeatedNull
============

`WMA link <https://reference.wolfram.com/language/ref/RepeatedNull.html>`_


:code:`RepeatedNull` [:math:`pat`]
    matches zero or more occurrences of :math:`pat`.





>>> a___Integer...//FullForm
  = RepeatedNull[Pattern[a, BlankNullSequence[Integer]]]
>>> f[x] /. f[x, 0...] -> t
  = t
