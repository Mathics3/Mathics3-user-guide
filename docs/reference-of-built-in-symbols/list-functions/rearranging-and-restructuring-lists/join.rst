Join
====

`WMA link <https://reference.wolfram.com/language/ref/Join.html>`_


:code:`Join` [:math:`l_1`, :math:`l_2`]
    concatenates the lists :math:`l_1` and :math:`l_2`.





:code:`Join`  concatenates lists:

>>> Join[{a, b}, {c, d, e}]
    =

:math:`\left\{a,b,c,d,e\right\}`


>>> Join[{{a, b}, {c, d}}, {{1, 2}, {3, 4}}]
    =

:math:`\left\{\left\{a,b\right\},\left\{c,d\right\},\left\{1,2\right\},\left\{3,4\right\}\right\}`



The concatenated expressions may have any head:

>>> Join[a + b, c + d, e + f]
    =

:math:`a+b+c+d+e+f`



However, it must be the same for all expressions:

>>> Join[a + b, c * d]

    Join::heads Heads Plus and Times are expected to be the same.
    =

:math:`\text{Join}\left[a+b,c d\right]`


