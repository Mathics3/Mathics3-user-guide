Expand
======

`WMA link <https://reference.wolfram.com/language/ref/Expand.html>`_


:code:`Expand` [:math:`expr`]
    expands out positive integer powers and products of sums in :math:`expr`, as           well as trigonometric identities.

Expand[:math:`expr`, :math:`target`]
    just expands those parts involving :math:`target`.





>>> Expand[(x + y) ^ 3]
  = x ^ 3 + 3 x ^ 2 y + 3 x y ^ 2 + y ^ 3
>>> Expand[(a + b) (a + c + d)]
  = a ^ 2 + a b + a c + a d + b c + b d
>>> Expand[(a + b) (a + c + d) (e + f) + e a a]
  = 2 a ^ 2 e + a ^ 2 f + a b e + a b f + a c e + a c f + a d e + a d f + b c e + b c f + b d e + b d f
>>> Expand[(a + b) ^ 2 * (c + d)]
  = a ^ 2 c + a ^ 2 d + 2 a b c + 2 a b d + b ^ 2 c + b ^ 2 d
>>> Expand[(x + y) ^ 2 + x y]
  = x ^ 2 + 3 x y + y ^ 2
>>> Expand[((a + b) (c + d)) ^ 2 + b (1 + a)]
  = a ^ 2 c ^ 2 + 2 a ^ 2 c d + a ^ 2 d ^ 2 + b + a b + 2 a b c ^ 2 + 4 a b c d + 2 a b d ^ 2 + b ^ 2 c ^ 2 + 2 b ^ 2 c d + b ^ 2 d ^ 2

:code:`Expand`  expands items in lists and rules:

>>> Expand[{4 (x + y), 2 (x + y) -> 4 (x + y)}]
  = {4 x + 4 y, 2 x + 2 y -> 4 x + 4 y}

:code:`Expand`  expands trigonometric identities

>>> Expand[Sin[x + y], Trig -> True]
  = Cos[x] Sin[y] + Cos[y] Sin[x]
>>> Expand[Tanh[x + y], Trig -> True]
  = Cosh[x] Sinh[y] / (Cosh[x] Cosh[y] + Sinh[x] Sinh[y]) + Cosh[y] Sinh[x] / (Cosh[x] Cosh[y] + Sinh[x] Sinh[y])

:code:`Expand`  does not change any other expression.

>>> Expand[Sin[x (1 + y)]]
  = Sin[x (1 + y)]

Using the second argument, the expression only
expands those subexpressions containing :math:`pat`:

>>> Expand[(x+a)^2+(y+a)^2+(x+y)(x+a), y]
  = a ^ 2 + 2 a y + x (a + x) + y (a + x) + y ^ 2 + (a + x) ^ 2

:code:`Expand`  also works in Galois fields

>>> Expand[(1 + a)^12, Modulus -> 3]
  = 1 + a ^ 3 + a ^ 9 + a ^ 12
>>> Expand[(1 + a)^12, Modulus -> 4]
  = 1 + 2 a ^ 2 + 3 a ^ 4 + 3 a ^ 8 + 2 a ^ 10 + a ^ 12
