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
  = 3
>>> a
  = 3

An assignment like this creates an ownvalue:

>>> OwnValues[a]
  = {HoldPattern[a] :> 3}

You can set multiple values at once using lists:

>>> {a, b, c} = {10, 2, 3}
  = {10, 2, 3}
>>> {a, b, {c, {d}}} = {1, 2, {{c1, c2}, {a}}}
  = {1, 2, {{c1, c2}, {10}}}
>>> d
  = 10

:code:`Set`  evaluates its right-hand side immediately and assigns it to
the left-hand side:

>>> a
  = 1
>>> x = a
  = 1
>>> a = 2
  = 2
>>> x
  = 1

:code:`Set`  always returns the right-hand side, which you can again use
in an assignment:

>>> a = b = c = 2;

>>> a == b == c == 2
  = True

:code:`Set`  supports assignments to parts:

>>> A = {{1, 2}, {3, 4}};

>>> A[[1, 2]] = 5
  = 5
>>> A
  = {{1, 5}, {3, 4}}
>>> A[[;;, 2]] = {6, 7}
  = {6, 7}
>>> A
  = {{1, 6}, {3, 7}}

Set a submatrix:

>>> B = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

>>> B[[1;;2, 2;;-1]] = {{t, u}, {y, z}};

>>> B
  = {{1, t, u}, {4, y, z}, {7, 8, 9}}
