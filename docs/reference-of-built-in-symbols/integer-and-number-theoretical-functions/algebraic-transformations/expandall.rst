ExpandAll
=========

`WMA link <https://reference.wolfram.com/language/ref/ExpandAll.html>`_


:code:`ExpandAll` [:math:`expr`]
    expands out negative integer powers and products of sums in :math:`expr`.

:code:`ExpandAll` [:math:`expr`, :math:`target`]
    just expands those parts involving :math:`target`.





>>> ExpandAll[(a + b) ^ 2 / (c + d)^2]
  = a ^ 2 / (c ^ 2 + 2 c d + d ^ 2) + 2 a b / (c ^ 2 + 2 c d + d ^ 2) + b ^ 2 / (c ^ 2 + 2 c d + d ^ 2)

:code:`ExpandAll`  descends into sub expressions

>>> ExpandAll[(a + Sin[x (1 + y)])^2]
  = 2 a Sin[x + x y] + a ^ 2 + Sin[x + x y] ^ 2
>>> ExpandAll[Sin[(x+y)^2]]
  = Sin[x ^ 2 + 2 x y + y ^ 2]
>>> ExpandAll[Sin[(x+y)^2], Trig->True]
  = Cos[x ^ 2] Cos[2 x y] Sin[y ^ 2] + Cos[x ^ 2] Cos[y ^ 2] Sin[2 x y] + Cos[2 x y] Cos[y ^ 2] Sin[x ^ 2] - Sin[x ^ 2] Sin[2 x y] Sin[y ^ 2]

:code:`ExpandAll`  also expands heads

>>> ExpandAll[((1 + x)(1 + y))[x]]
  = (1 + x + y + x y)[x]

:code:`ExpandAll`  can also work in finite fields

>>> ExpandAll[(1 + a) ^ 6 / (x + y)^3, Modulus -> 3]
  = (1 + 2 a ^ 3 + a ^ 6) / (x ^ 3 + y ^ 3)
