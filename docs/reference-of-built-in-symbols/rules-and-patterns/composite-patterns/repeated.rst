Repeated
========

`WMA link <https://reference.wolfram.com/language/ref/Repeated.html>`_


:code:`Repeated` [:math:`pat`]
    matches one or more occurrences of :math:`pat`.





>>> a_Integer.. // FullForm

    =
:math:`\text{Repeated}\left[\text{Pattern}\left[a, \text{Blank}\left[\text{Integer}\right]\right]\right]`


>>> 0..1//FullForm

    =
:math:`\text{Repeated}\left[0\right]`


>>> {{}, {a}, {a, b}, {a, a, a}, {a, a, a, a}} /. {Repeated[x : a | b, 3]} -> x

    =
:math:`\left\{\left\{\right\},a,\left\{a,b\right\},a,\left\{a,a,a,a\right\}\right\}`


>>> f[x, 0, 0, 0] /. f[x, s:0..] -> s

    =
:math:`\text{Sequence}\left[0,0,0\right]`


