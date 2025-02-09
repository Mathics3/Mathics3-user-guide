Listable
========

`WMA link <https://reference.wolfram.com/language/ref/Listable.html>`_


:code:`Listable`
    is an attribute specifying that a function should be         automatically applied to each element of a list.





>>> SetAttributes[f, Listable]


>>> f[{1, 2, 3}, {4, 5, 6}]

    =
:math:`\left\{f\left[1,4\right],f\left[2,5\right],f\left[3,6\right]\right\}`


>>> f[{1, 2, 3}, 4]

    =
:math:`\left\{f\left[1,4\right],f\left[2,4\right],f\left[3,4\right]\right\}`


>>> {{1, 2}, {3, 4}} + {5, 6}

    =
:math:`\left\{\left\{6,7\right\},\left\{9,10\right\}\right\}`


