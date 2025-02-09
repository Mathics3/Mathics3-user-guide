Permutations
============

`WMA link <https://reference.wolfram.com/language/ref/Permutations.html>`_


:code:`Permutations` [:math:`list`]
    gives all possible orderings of the items in :math:`list`.

:code:`Permutations` [:math:`list`, :math:`n`]
    gives permutations up to length :math:`n`.

:code:`Permutations` [:math:`list`, {:math:`n`}]
    gives permutations of length :math:`n`.





>>> Permutations[{y, 1, x}]

    =
:math:`\left\{\left\{y,1,x\right\},\left\{y,x,1\right\},\left\{1,y,x\right\},\left\{1,x,y\right\},\left\{x,y,1\right\},\left\{x,1,y\right\}\right\}`



Elements are differentiated by their position in :math:`list`, not their value.

>>> Permutations[{a, b, b}]

    =
:math:`\left\{\left\{a,b,b\right\},\left\{a,b,b\right\},\left\{b,a,b\right\},\left\{b,b,a\right\},\left\{b,a,b\right\},\left\{b,b,a\right\}\right\}`


>>> Permutations[{1, 2, 3}, 2]

    =
:math:`\left\{\left\{\right\},\left\{1\right\},\left\{2\right\},\left\{3\right\},\left\{1,2\right\},\left\{1,3\right\},\left\{2,1\right\},\left\{2,3\right\},\left\{3,1\right\},\left\{3,2\right\}\right\}`


>>> Permutations[{1, 2, 3}, {2}]

    =
:math:`\left\{\left\{1,2\right\},\left\{1,3\right\},\left\{2,1\right\},\left\{2,3\right\},\left\{3,1\right\},\left\{3,2\right\}\right\}`


