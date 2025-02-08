Delete
======

`WMA link <https://reference.wolfram.com/language/ref/Delete.html>`_


:code:`Delete` [:math:`expr`, :math:`i`]
    deletes the element at position :math:`i` in :math:`expr`. The position is counted from the end if :math:`i` is negative.

:code:`Delete` [:math:`expr`, {:math:`m`, :math:`n`, ...}]
    deletes the element at position {:math:`m`, :math:`n`, ...}.

:code:`Delete` [:math:`expr`, {{:math:`m_1`, :math:`n_1`, ...}, {:math:`m_2`, :math:`n_2`, ...}, ...}]
    deletes the elements at several positions.





Delete the element at position 3:

>>> Delete[{a, b, c, d}, 3]
    =

:math:`\left\{a,b,d\right\}`



Delete at position 2 from the end:

>>> Delete[{a, b, c, d}, -2]
    =

:math:`\left\{a,b,d\right\}`



Delete at positions 1 and 3:

>>> Delete[{a, b, c, d}, {{1}, {3}}]
    =

:math:`\left\{b,d\right\}`



Delete in a 2D array:

>>> Delete[{{a, b}, {c, d}}, {2, 1}]
    =

:math:`\left\{\left\{a,b\right\},\left\{d\right\}\right\}`



Deleting the head of a whole expression gives a Sequence object:

>>> Delete[{a, b, c}, 0]
    =

:math:`\text{Sequence}\left[a,b,c\right]`



Delete in an expression with any head:

>>> Delete[f[a, b, c, d], 3]
    =

:math:`f\left[a,b,d\right]`



Delete a head to splice in its arguments:

>>> Delete[f[a, b, u + v, c], {3, 0}]
    =

:math:`f\left[a,b,u,v,c\right]`


>>> Delete[{a, b, c}, 0]
    =

:math:`\text{Sequence}\left[a,b,c\right]`



Delete without the position:

>>> Delete[{a, b, c, d}]

    Delete::argr Delete called with 1 argument; 2 arguments are expected.
    =

:math:`\text{Delete}\left[\left\{a,b,c,d\right\}\right]`



Delete with many arguments:

>>> Delete[{a, b, c, d}, 1, 2]

    Delete::argt Delete called with 3 arguments; 2 arguments are expected.
    =

:math:`\text{Delete}\left[\left\{a,b,c,d\right\},1,2\right]`



Delete the element out of range:

>>> Delete[{a, b, c, d}, 5]

    Part::partw Part {5} of {a, b, c, d} does not exist.
    =

:math:`\text{Delete}\left[\left\{a,b,c,d\right\},5\right]`


>>> Delete[{a, b, c, d}, {1, 2}]
    = Delete[{a, b, c, d}, {1, 2}]`


Delete the position not integer:

>>> Delete[{a, b, c, d}, {1, n}]

    Delete::psl Position specification n in {a, b, c, d} is not a machine-sized integer or a list of machine-sized integers.
    =

:math:`\text{Delete}\left[\left\{a,b,c,d\right\},\left\{1,n\right\}\right]`


