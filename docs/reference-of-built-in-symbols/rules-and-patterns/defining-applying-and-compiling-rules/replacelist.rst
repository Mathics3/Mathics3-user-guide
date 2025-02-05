ReplaceList
===========

`WMA link <https://reference.wolfram.com/language/ref/ReplaceList.html>`_


:code:`ReplaceList` [:math:`expr`, :math:`rules`]
    returns a list of all possible results when applying :math:`rules`         to :math:`expr`.

:code:`ReplaceList` [:math:`expr`, :math:`rules`, :math:`n`]
    returns a list of at most :math:`n` results when applying :math:`rules`         to :math:`expr`.





Get all subsequences of a list:

>>> ReplaceList[{a, b, c}, {___, x__, ___} -> {x}]
  = {{a}, {a, b}, {a, b, c}, {b}, {b, c}, {c}}

You can specify the maximum number of items:

>>> ReplaceList[{a, b, c}, {___, x__, ___} -> {x}, 3]
  = {{a}, {a, b}, {a, b, c}}
>>> ReplaceList[{a, b, c}, {___, x__, ___} -> {x}, 0]
  = {}

If no rule matches, an empty list is returned:

>>> ReplaceList[a, b->x]
  = {}

Like in :code:`ReplaceAll` , :math:`rules` can be a nested list:

>>> ReplaceList[{a, b, c}, {{{___, x__, ___} -> {x}}, {{a, b, c} -> t}}, 2]
  = {{{a}, {a, b}}, {t}}

Possible matches for a sum:

>>> ReplaceList[a + b + c, x_ + y_ -> {x, y}]
  = {{a, b + c}, {b, a + c}, {c, a + b}, {a + b, c}, {a + c, b}, {b + c, a}}
