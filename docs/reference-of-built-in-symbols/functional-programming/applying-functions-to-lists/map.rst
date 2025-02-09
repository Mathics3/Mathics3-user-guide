Map
===

`WMA link <https://reference.wolfram.com/language/ref/Map.html>`_


:code:`Map` [:math:`f`, :math:`expr`] or :code:`:math:`f` /@ :math:`expr``
    applies :math:`f` to each part on the first level of :math:`expr`.

:code:`Map` [:math:`f`, :math:`expr`, :math:`levelspec`]
    applies :math:`f` to each level specified by :math:`levelspec` of :math:`expr`.





>>> f /@ {1, 2, 3}

    =
:math:`\left\{f\left[1\right],f\left[2\right],f\left[3\right]\right\}`


>>> #^2& /@ {1, 2, 3, 4}

    =
:math:`\left\{1,4,9,16\right\}`



Map :math:`f` on the second level:

>>> Map[f, {{a, b}, {c, d, e}}, {2}]

    =
:math:`\left\{\left\{f\left[a\right],f\left[b\right]\right\},\left\{f\left[c\right],f\left[d\right],f\left[e\right]\right\}\right\}`



Include heads:

>>> Map[f, a + b + c, Heads->True]

    =
:math:`f\left[\text{Plus}\right]\left[f\left[a\right],f\left[b\right],f\left[c\right]\right]`


