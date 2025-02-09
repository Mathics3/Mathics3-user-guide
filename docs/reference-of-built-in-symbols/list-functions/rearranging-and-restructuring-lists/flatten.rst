Flatten
=======

`WMA link <https://reference.wolfram.com/language/ref/Flatten.html>`_


:code:`Flatten` [:math:`expr`]
    flattens out nested lists in :math:`expr`.

:code:`Flatten` [:math:`expr`, :math:`n`]
    stops flattening at level :math:`n`.

:code:`Flatten` [:math:`expr`, :math:`n`, :math:`h`]
    flattens expressions with head :math:`h` instead of :code:`List` .





>>> Flatten[{{a, b}, {c, {d}, e}, {f, {g, h}}}]

    =
:math:`\left\{a,b,c,d,e,f,g,h\right\}`


>>> Flatten[{{a, b}, {c, {e}, e}, {f, {g, h}}}, 1]

    =
:math:`\left\{a,b,c,\left\{e\right\},e,f,\left\{g,h\right\}\right\}`


>>> Flatten[f[a, f[b, f[c, d]], e], Infinity, f]

    =
:math:`f\left[a,b,c,d,e\right]`


>>> Flatten[{{a, b}, {c, d}}, {{2}, {1}}]

    =
:math:`\left\{\left\{a,c\right\},\left\{b,d\right\}\right\}`


>>> Flatten[{{a, b}, {c, d}}, {{1, 2}}]

    =
:math:`\left\{a,b,c,d\right\}`



Flatten also works in irregularly shaped arrays

>>> Flatten[{{1, 2, 3}, {4}, {6, 7}, {8, 9, 10}}, {{2}, {1}}]

    =
:math:`\left\{\left\{1,4,6,8\right\},\left\{2,7,9\right\},\left\{3,10\right\}\right\}`


