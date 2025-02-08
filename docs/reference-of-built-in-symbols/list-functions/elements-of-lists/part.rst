Part
====

`WMA link <https://reference.wolfram.com/language/ref/Part.html>`_


:code:`Part` [:math:`expr`, :math:`i`]
    returns part :math:`i` of :math:`expr`.





Extract an element from a list:

>>> A = {a, b, c, d};


>>> A[[3]]
    =

:math:`c`



Negative indices count from the end:

>>> {a, b, c}[[-2]]
    =

:math:`b`



:code:`Part`  can be applied on any expression, not necessarily lists.

>>> (a + b + c)[[2]]
    =

:math:`b`



:code:`:math:`expr`[[0]]`  gives the head of :math:`expr`:

>>> (a + b + c)[[0]]
    =

:math:`\text{Plus}`



Parts of nested lists:

>>> M = {{a, b}, {c, d}};


>>> M[[1, 2]]
    =

:math:`b`



You can use :code:`Span`  to specify a range of parts:

>>> {1, 2, 3, 4}[[2;;4]]
    =

:math:`\left\{2,3,4\right\}`


>>> {1, 2, 3, 4}[[2;;-1]]
    =

:math:`\left\{2,3,4\right\}`



A list of parts extracts elements at certain indices:

>>> {a, b, c, d}[[{1, 3, 3}]]
    =

:math:`\left\{a,c,c\right\}`



Get a certain column of a matrix:

>>> B = {{a, b, c}, {d, e, f}, {g, h, i}};


>>> B[[;;, 2]]
    =

:math:`\left\{b,e,h\right\}`



Extract a submatrix of 1st and 3rd row and the two last columns:

>>> B = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};


>>> B[[{1, 3}, -2;;-1]]
    =

:math:`\left\{\left\{2,3\right\},\left\{8,9\right\}\right\}`



The 3d column of a matrix:

>>> {{a, b, c}, {d, e, f}, {g, h, i}}[[All, 3]]
    =

:math:`\left\{c,f,i\right\}`



Further examples:

>>> (a+b+c+d)[[-1;;-2]]
    =

:math:`0`


>>> x[[2]]

    Part::partd Part specification is longer than depth of object.
    =

:math:`x\left[\left[2\right]\right]`



Assignments to parts are possible:

>>> B[[;;, 2]] = {10, 11, 12}
    =

:math:`\left\{10,11,12\right\}`


>>> B
    =

:math:`\left\{\left\{1,10,3\right\},\left\{4,11,6\right\},\left\{7,12,9\right\}\right\}`


>>> B[[;;, 3]] = 13
    =

:math:`13`


>>> B
    =

:math:`\left\{\left\{1,10,13\right\},\left\{4,11,13\right\},\left\{7,12,13\right\}\right\}`


>>> B[[1;;-2]] = t;


>>> B
    =

:math:`\left\{t,t,\left\{7,12,13\right\}\right\}`


>>> F = Table[i*j*k, {i, 1, 3}, {j, 1, 3}, {k, 1, 3}];


>>> F[[;; All, 2 ;; 3, 2]] = t;


>>> F
    =

:math:`\left\{\left\{\left\{1,2,3\right\},\left\{2,t,6\right\},\left\{3,t,9\right\}\right\},\left\{\left\{2,4,6\right\},\left\{4,t,12\right\},\left\{6,t,18\right\}\right\},\left\{\left\{3,6,9\right\},\left\{6,t,18\right\},\left\{9,t,27\right\}\right\}\right\}`


>>> F[[;; All, 1 ;; 2, 3 ;; 3]] = k;


>>> F
    =

:math:`\left\{\left\{\left\{1,2,k\right\},\left\{2,t,k\right\},\left\{3,t,9\right\}\right\},\left\{\left\{2,4,k\right\},\left\{4,t,k\right\},\left\{6,t,18\right\}\right\},\left\{\left\{3,6,k\right\},\left\{6,t,k\right\},\left\{9,t,27\right\}\right\}\right\}`



Of course, part specifications have precedence over most arithmetic operations:

>>> A[[1]] + B[[2]] + C[[3]] // Hold // FullForm
    =

:math:`\text{Hold}\left[\text{Plus}\left[\text{Part}\left[A, 1\right], \text{Part}\left[B, 2\right], \text{Part}\left[C, 3\right]\right]\right]`


