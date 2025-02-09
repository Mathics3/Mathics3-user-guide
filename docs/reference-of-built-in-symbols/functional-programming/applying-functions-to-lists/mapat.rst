MapAt
=====

`WMA link <https://reference.wolfram.com/language/ref/MapAt.html>`_


:code:`MapAt` [:math:`f`, :math:`expr`, :math:`n`]
    applies :math:`f` to the element at position :math:`n` in :math:`expr`. If :math:`n` is negative, the position is counted from the end.

:code:`MapAt` [f, :math:`expr`, {:math:`i`, :math:`j` ...}]
    applies :math:`f` to the part of :math:`expr` at position {:math:`i`, :math:`j`, ...}.

:code:`MapAt` [:math:`f`, :math:`pos`]
    represents an operator form of :code:`MapAt`  that can be applied to an expression.





Map function :math:`f` to the second element of an simple flat list:

>>> MapAt[f, {a, b, c}, 2]

    =
:math:`\left\{a,f\left[b\right],c\right\}`



Above, we specified a simple integer value 2. In general, the expression can be an arbitrary vector.

Using :code:`MapAt`  with :code:`Function[0]` , we can zero a value or values in a vector:

>>> MapAt[0&, {{1, 1}, {1, 1}}, {2, 1}]

    =
:math:`\left\{\left\{1,1\right\},\left\{0,1\right\}\right\}`



When the dimension of the replacement expression is less than the vector,     that element's dimension changes:

>>> MapAt[0&, {{0, 1}, {1, 0}}, 2]

    =
:math:`\left\{\left\{0,1\right\},0\right\}`



So now compare what happen when using {{2}, {1}} instead of {2, 1} above:

>>> MapAt[0&, {{0, 1}, {1, 0}}, {{2}, {1}}]

    =
:math:`\left\{0,0\right\}`



Map :math:`f` onto the last element of a list:

>>> MapAt[f, {a, b, c}, -1]

    =
:math:`\left\{a,b,f\left[c\right]\right\}`



Same as above, but use the operator form of :code:`MapAt` :

>>> MapAt[f, -1][{a, b, c}]

    =
:math:`\left\{a,b,f\left[c\right]\right\}`



Map :math:`f` onto at the second position of an association:

>>> MapAt[f, <|"a" -> 1, "b" -> 2, "c" -> 3, "d" -> 4|>, 2]

    =
:math:`\left\{\text{a}->1,\text{b}->f\left[2\right],\text{c}->3,\text{d}->4\right\}`



Same as above, but select the second-from-the-end position:

>>> MapAt[f, <|"a" -> 1, "b" -> 2, "c" -> 3, "d" -> 4|>, -2]

    =
:math:`\left\{\text{a}->1,\text{b}->2,\text{c}->f\left[3\right],\text{d}->4\right\}`


