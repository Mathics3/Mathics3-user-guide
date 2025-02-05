Level
=====

`WMA link <https://reference.wolfram.com/language/ref/Level.html>`_


:code:`Level` [:math:`expr`, :math:`levelspec`]
    gives a list of all subexpressions of :math:`expr` at the
    level(s) specified by :math:`levelspec`.





Level uses standard level specifications:


:math:`n`
    levels 1 through :math:`n`

:code:`Infinity`
    all levels from level 1

:code:`{:math:`n`}`
    level :math:`n` only

:code:`{:math:`m`, :math:`n`}`
    levels :math:`m` through :math:`n`





Level 0 corresponds to the whole expression.

A negative level :code:`-:math:`n``  consists of parts with depth :math:`n`.

Level -1 is the set of atoms in an expression:

>>> Level[a + b ^ 3 * f[2 x ^ 2], {-1}]
  = {a, b, 3, 2, x, 2}
>>> Level[{{{{a}}}}, 3]
  = {{a}, {{a}}, {{{a}}}}
>>> Level[{{{{a}}}}, -4]
  = {{{{a}}}}
>>> Level[{{{{a}}}}, -5]
  = {}
>>> Level[h0[h1[h2[h3[a]]]], {0, -1}]
  = {a, h3[a], h2[h3[a]], h1[h2[h3[a]]], h0[h1[h2[h3[a]]]]}

Use the option :code:`Heads -> True`  to include heads:

>>> Level[{{{{a}}}}, 3, Heads -> True]
  = {List, List, List, {a}, {{a}}, {{{a}}}}
>>> Level[x^2 + y^3, 3, Heads -> True]
  = {Plus, Power, x, 2, x ^ 2, Power, y, 3, y ^ 3}
>>> Level[a ^ 2 + 2 * b, {-1}, Heads -> True]
  = {Plus, Power, a, 2, Times, 2, b}
>>> Level[f[g[h]][x], {-1}, Heads -> True]
  = {f, g, h, x}
>>> Level[f[g[h]][x], {-2, -1}, Heads -> True]
  = {f, g, h, g[h], x, f[g[h]][x]}
