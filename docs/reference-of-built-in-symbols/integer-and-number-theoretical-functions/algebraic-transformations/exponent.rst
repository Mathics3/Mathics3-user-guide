Exponent
========

`WMA link <https://reference.wolfram.com/language/ref/Exponent.html>`_


:code:`Exponent[expr, form]`
    returns the maximum power with which :math:`form` appears in the expanded           form of :math:`expr`.

:code:`Exponent[expr, form, h]`
    applies :math:`h` to the set of exponents with which :math:`form` appears in :math:`expr`.





>>> Exponent[5 x^2 - 3 x + 7, x]
  = 2
>>> Exponent[(x^3 + 1)^2 + 1, x]
  = 6
>>> Exponent[x^(n + 1) + Sqrt[x] + 1, x]
  = Max[1 / 2, 1 + n]
>>> Exponent[x / y, y]
  = -1
>>> Exponent[(x^2 + 1)^3 - 1, x, Min]
  = 2
>>> Exponent[0, x]
  = -Infinity
>>> Exponent[1, x]
  = 0
