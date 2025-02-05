Orderless
=========

`WMA link <https://reference.wolfram.com/language/ref/Orderless.html>`_


:code:`Orderless`
    is an attribute that can be assigned to a symbol :math:`f` to         indicate that the elements :math:`ei` in expressions of the form         :math:`f`[:math:`e_1`, :math:`e_2`, ...] should automatically be sorted into         canonical order. This property is accounted for in pattern         matching.





The elements of an :code:`Orderless`  function are automatically sorted:

>>> SetAttributes[f, Orderless]

>>> f[c, a, b, a + b, 3, 1.0]
  = f[1., 3, a, b, c, a + b]

A symbol with the :code:`Orderless`  attribute represents a commutative     mathematical operation.

>>> f[a, b] == f[b, a]
  = True

:code:`Orderless`  affects pattern matching:

>>> SetAttributes[f, Flat]

>>> f[a, b, c] /. f[a, c] -> d
  = f[b, d]
