Repeated
========

`WMA link <https://reference.wolfram.com/language/ref/Repeated.html>`_


:code:`Repeated` [:math:`pat`]
    matches one or more occurrences of :math:`pat`.





>>> a_Integer.. // FullForm
  = Repeated[Pattern[a, Blank[Integer]]]
>>> 0..1//FullForm
  = Repeated[0]
>>> {{}, {a}, {a, b}, {a, a, a}, {a, a, a, a}} /. {Repeated[x : a | b, 3]} -> x
  = {{}, a, {a, b}, a, {a, a, a, a}}
>>> f[x, 0, 0, 0] /. f[x, s:0..] -> s
  = Sequence[0, 0, 0]
