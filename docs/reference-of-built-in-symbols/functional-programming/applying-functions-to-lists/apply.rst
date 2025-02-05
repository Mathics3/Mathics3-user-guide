Apply
=====

`WMA link <https://reference.wolfram.com/language/ref/Apply.html>`_



:code:`Apply` [:math:`f`, :math:`expr`]
    same as

:code:`:math:`f` @@ :math:`expr``
    replaces the head of :math:`expr` with :math:`f`.

:code:`Apply` [:math:`f`, :math:`expr`, :math:`levelspec`]
    applies :math:`f` on the parts specified by :math:`levelspec`.





>>> f @@ {1, 2, 3}
  = f[1, 2, 3]
>>> Plus @@ {1, 2, 3}
  = 6

The head of :math:`expr` need not be :code:`List` :

>>> f @@ (a + b + c)
  = f[a, b, c]

Apply on level 1:

>>> Apply[f, {a + b, g[c, d, e * f], 3}, {1}]
  = {f[a, b], f[c, d, e f], 3}

The default level is 0:

>>> Apply[f, {a, b, c}, {0}]
  = f[a, b, c]

Range of levels, including negative level (counting from bottom):

>>> Apply[f, {{{{{a}}}}}, {2, -3}]
  = {{f[f[{a}]]}}

Convert all operations to lists:

>>> Apply[List, a + b * c ^ e * f[g], {0, Infinity}]
  = {a, {b, {g}, {c, e}}}
