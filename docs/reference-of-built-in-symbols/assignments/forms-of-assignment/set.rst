Set
===

`WMA link <https://reference.wolfram.com/language/ref/Set.html>`_


:code:`Set` [:math:`expr`, :math:`value`]
    same as

:math:`expr` = :math:`value`
    evaluates :math:`value` and assigns it to :math:`expr`.

{:math:`s_1`, :math:`s_2`, :math:`s_3`} = {:math:`v_1`, :math:`v_2`, :math:`v_3`}
    sets multiple symbols (:math:`s_1`, :math:`s_2`, ...) to the corresponding           values (:math:`v_1`, :math:`v_2`, ...).





:code:`Set`  can be used to give a symbol a value:

>>> a = 3

    =
:math:`3`


>>> a

    =
:math:`3`



An assignment like this creates an ownvalue:

>>> OwnValues[a]

    =
:math:`\left\{\text{HoldPattern}\left[a\right]\text{:>}3\right\}`



You can set multiple values at once using lists:

>>> {a, b, c} = {10, 2, 3}

    =
:math:`\left\{10,2,3\right\}`


>>> {a, b, {c, {d}}} = {1, 2, {{c1, c2}, {a}}}

    =
:math:`\left\{1,2,\left\{\left\{\text{c1},\text{c2}\right\},\left\{10\right\}\right\}\right\}`


>>> d

    =
:math:`10`



:code:`Set`  evaluates its right-hand side immediately and assigns it to
the left-hand side:

>>> a

    =
:math:`1`


>>> x = a

    =
:math:`1`


>>> a = 2

    =
:math:`2`


>>> x

    =
:math:`1`



:code:`Set`  always returns the right-hand side, which you can again use
in an assignment:

>>> a = b = c = 2;


>>> a == b == c == 2

    =
:math:`\text{True}`



:code:`Set`  supports assignments to parts:

>>> A = {{1, 2}, {3, 4}};


>>> A[[1, 2]] = 5

    =
:math:`5`


>>> A

    =
:math:`\left\{\left\{1,5\right\},\left\{3,4\right\}\right\}`


>>> A[[;;, 2]] = {6, 7}

    =
:math:`\left\{6,7\right\}`


>>> A

    =
:math:`\left\{\left\{1,6\right\},\left\{3,7\right\}\right\}`



Set a submatrix:

>>> B = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};


>>> B[[1;;2, 2;;-1]] = {{t, u}, {y, z}};


>>> B

    =
:math:`\left\{\left\{1,t,u\right\},\left\{4,y,z\right\},\left\{7,8,9\right\}\right\}`


