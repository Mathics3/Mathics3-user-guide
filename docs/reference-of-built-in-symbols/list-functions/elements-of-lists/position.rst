Position
========

`WMA link <https://reference.wolfram.com/language/ref/Position.html>`_


:code:`Position` [:math:`expr`, :math:`patt`]
    returns the list of positions for which :math:`expr` matches :math:`patt`.

:code:`Position` [:math:`expr`, :math:`patt`, :math:`ls`]
    returns the positions on levels specified by levelspec :math:`ls`.





>>> Position[{1, 2, 2, 1, 2, 3, 2}, 2]
    =

:math:`\left\{\left\{2\right\},\left\{3\right\},\left\{5\right\},\left\{7\right\}\right\}`



Find positions upto 3 levels deep:

>>> Position[{1 + Sin[x], x, (Tan[x] - y)^2}, x, 3]
    =

:math:`\left\{\left\{1,2,1\right\},\left\{2\right\}\right\}`



Find all powers of x:

>>> Position[{1 + x^2, x y ^ 2,  4 y,  x ^ z}, x^_]
    =

:math:`\left\{\left\{1,2\right\},\left\{4\right\}\right\}`



Use Position as an operator:

>>> Position[_Integer][{1.5, 2, 2.5}]
    =

:math:`\left\{\left\{2\right\}\right\}`


