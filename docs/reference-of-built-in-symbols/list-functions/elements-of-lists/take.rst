Take
====

`WMA link <https://reference.wolfram.com/language/ref/Take.html>`_


:code:`Take` [:math:`expr`, :math:`n`]
    returns :math:`expr` with all but the first :math:`n` elements removed.

:code:`Take` [:math:`list`, -:math:`n`]
    returns last :math:`n` elements of :math:`list`.

:code:`Take` [:math:`list`, {:math:`m`, :math:`n`}]
    returns elements :math:`m` through :math:`n` of :math:`list`.





Get the first three elements:

>>> Take[{a, b, c, d}, 3]
    =

:math:`\left\{a,b,c\right\}`



Get the last two elements:

>>> Take[{a, b, c, d}, -2]
    =

:math:`\left\{c,d\right\}`



Get the elements from the second element through the next to last element:

>>> Take[{a, b, c, d, e}, {2, -2}]
    =

:math:`\left\{b,c,d\right\}`



Take a submatrix:

>>> A = {{a, b, c}, {d, e, f}};


>>> Take[A, 2, 2]
    =

:math:`\left\{\left\{a,b\right\},\left\{d,e\right\}\right\}`



Take a single column:

>>> Take[A, All, {2}]
    =

:math:`\left\{\left\{b\right\},\left\{e\right\}\right\}`



Taking the 0th element does nothing, and returns an empty list:

>>> Take[{a, b, c, d}, 0]
    =

:math:`\left\{\right\}`



See also `:code:`Drop`  </doc/reference-of-built-in-symbols/list-functions/elements-of-lists/drop/>`_.