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

    =
:math:`f\left[1,2,3\right]`


>>> Plus @@ {1, 2, 3}

    =
:math:`6`



The head of :math:`expr` need not be :code:`List` :

>>> f @@ (a + b + c)

    =
:math:`f\left[a,b,c\right]`



Apply on level 1:

>>> Apply[f, {a + b, g[c, d, e * f], 3}, {1}]

    =
:math:`\left\{f\left[a,b\right],f\left[c,d,e f\right],3\right\}`



The default level is 0:

>>> Apply[f, {a, b, c}, {0}]

    =
:math:`f\left[a,b,c\right]`



Range of levels, including negative level (counting from bottom):

>>> Apply[f, {{{{{a}}}}}, {2, -3}]

    =
:math:`\left\{\left\{f\left[f\left[\left\{a\right\}\right]\right]\right\}\right\}`



Convert all operations to lists:

>>> Apply[List, a + b * c ^ e * f[g], {0, Infinity}]

    =
:math:`\left\{a,\left\{b,\left\{g\right\},\left\{c,e\right\}\right\}\right\}`


