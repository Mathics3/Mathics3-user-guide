ReplaceList
===========

`WMA link <https://reference.wolfram.com/language/ref/ReplaceList.html>`_


:code:`ReplaceList` [:math:`expr`, :math:`rules`]
    returns a list of all possible results when applying :math:`rules`         to :math:`expr`.

:code:`ReplaceList` [:math:`expr`, :math:`rules`, :math:`n`]
    returns a list of at most :math:`n` results when applying :math:`rules`         to :math:`expr`.





Get all subsequences of a list:

>>> ReplaceList[{a, b, c}, {___, x__, ___} -> {x}]
    =

:math:`\left\{\left\{a\right\},\left\{a,b\right\},\left\{a,b,c\right\},\left\{b\right\},\left\{b,c\right\},\left\{c\right\}\right\}`



You can specify the maximum number of items:

>>> ReplaceList[{a, b, c}, {___, x__, ___} -> {x}, 3]
    =

:math:`\left\{\left\{a\right\},\left\{a,b\right\},\left\{a,b,c\right\}\right\}`


>>> ReplaceList[{a, b, c}, {___, x__, ___} -> {x}, 0]
    =

:math:`\left\{\right\}`



If no rule matches, an empty list is returned:

>>> ReplaceList[a, b->x]
    =

:math:`\left\{\right\}`



Like in :code:`ReplaceAll` , :math:`rules` can be a nested list:

>>> ReplaceList[{a, b, c}, {{{___, x__, ___} -> {x}}, {{a, b, c} -> t}}, 2]
    =

:math:`\left\{\left\{\left\{a\right\},\left\{a,b\right\}\right\},\left\{t\right\}\right\}`



Possible matches for a sum:

>>> ReplaceList[a + b + c, x_ + y_ -> {x, y}]
    =

:math:`\left\{\left\{a,b+c\right\},\left\{b,a+c\right\},\left\{c,a+b\right\},\left\{a+b,c\right\},\left\{a+c,b\right\},\left\{b+c,a\right\}\right\}`


