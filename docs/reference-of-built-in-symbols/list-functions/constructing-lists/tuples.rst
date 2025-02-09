Tuples
======

`WMA link <https://reference.wolfram.com/language/ref/Tuples.html>`_


:code:`Tuples` [:math:`list`, :math:`n`]
    returns a list of all :math:`n`-tuples of elements in :math:`list`.

:code:`Tuples` [{:math:`list_1`, :math:`list_2`, ...}]
    returns a list of tuples with elements from the given lists.





>>> Tuples[{a, b, c}, 2]

    =
:math:`\left\{\left\{a,a\right\},\left\{a,b\right\},\left\{a,c\right\},\left\{b,a\right\},\left\{b,b\right\},\left\{b,c\right\},\left\{c,a\right\},\left\{c,b\right\},\left\{c,c\right\}\right\}`


>>> Tuples[{}, 2]

    =
:math:`\left\{\right\}`


>>> Tuples[{a, b, c}, 0]

    =
:math:`\left\{\left\{\right\}\right\}`


>>> Tuples[{{a, b}, {1, 2, 3}}]

    =
:math:`\left\{\left\{a,1\right\},\left\{a,2\right\},\left\{a,3\right\},\left\{b,1\right\},\left\{b,2\right\},\left\{b,3\right\}\right\}`



The head of :math:`list` need not be :code:`List` :

>>> Tuples[f[a, b, c], 2]

    =
:math:`\left\{f\left[a,a\right],f\left[a,b\right],f\left[a,c\right],f\left[b,a\right],f\left[b,b\right],f\left[b,c\right],f\left[c,a\right],f\left[c,b\right],f\left[c,c\right]\right\}`



However, when specifying multiple expressions, :code:`List`  is always used:

>>> Tuples[{f[a, b], g[c, d]}]

    =
:math:`\left\{\left\{a,c\right\},\left\{a,d\right\},\left\{b,c\right\},\left\{b,d\right\}\right\}`


