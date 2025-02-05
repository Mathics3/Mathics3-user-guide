Inner
=====

`WMA link <https://reference.wolfram.com/language/ref/Inner.html>`_


:code:`Inner` [:math:`f`, :math:`x`, :math:`y`, :math:`g`]
    computes a generalised inner product of :math:`x` and :math:`y`, using
    a multiplication function :math:`f` and an addition function :math:`g`.





>>> Inner[f, {a, b}, {x, y}, g]
  = g[f[a, x], f[b, y]]

:code:`Inner`  can be used to compute a dot product:

>>> Inner[Times, {a, b}, {c, d}, Plus] == {a, b} . {c, d}
  = True

The inner product of two boolean matrices:

>>> Inner[And, {{False, False}, {False, True}}, {{True, False}, {True, True}}, Or]
  = {{False, False}, {True, True}}

Inner works with tensors of any depth:

>>> Inner[f, {{{a, b}}, {{c, d}}}, {{1}, {2}}, g]
  = {{{g[f[a, 1], f[b, 2]]}}, {{g[f[c, 1], f[d, 2]]}}}
