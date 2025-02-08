Split
=====

`WMA link <https://reference.wolfram.com/language/ref/Split.html>`_


:code:`Split` [:math:`list`]
    splits :math:`list` into collections of consecutive identical elements.

:code:`Split` [:math:`list`, :math:`test`]
    splits :math:`list` based on whether the function :math:`test` yields
    :code:`True`  on consecutive elements.





>>> Split[{x, x, x, y, x, y, y, z}]
    =

:math:`\left\{\left\{x,x,x\right\},\left\{y\right\},\left\{x\right\},\left\{y,y\right\},\left\{z\right\}\right\}`



Split into increasing or decreasing runs of elements

>>> Split[{1, 5, 6, 3, 6, 1, 6, 3, 4, 5, 4}, Less]
    =

:math:`\left\{\left\{1,5,6\right\},\left\{3,6\right\},\left\{1,6\right\},\left\{3,4,5\right\},\left\{4\right\}\right\}`


>>> Split[{1, 5, 6, 3, 6, 1, 6, 3, 4, 5, 4}, Greater]
    =

:math:`\left\{\left\{1\right\},\left\{5\right\},\left\{6,3\right\},\left\{6,1\right\},\left\{6,3\right\},\left\{4\right\},\left\{5,4\right\}\right\}`



Split based on first element

>>> Split[{x -> a, x -> y, 2 -> a, z -> c, z -> a}, First[#1] === First[#2] &]
    =

:math:`\left\{\left\{x->a,x->y\right\},\left\{2->a\right\},\left\{z->c,z->a\right\}\right\}`


