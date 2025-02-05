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
  = {a, f[b], c}

Above, we specified a simple integer value 2. In general, the expression can be an arbitrary vector.

Using :code:`MapAt`  with :code:`Function[0]` , we can zero a value or values in a vector:

>>> MapAt[0&, {{1, 1}, {1, 1}}, {2, 1}]
  = {{1, 1}, {0, 1}}

When the dimension of the replacement expression is less than the vector,     that element's dimension changes:

>>> MapAt[0&, {{0, 1}, {1, 0}}, 2]
  = {{0, 1}, 0}

So now compare what happen when using {{2}, {1}} instead of {2, 1} above:

>>> MapAt[0&, {{0, 1}, {1, 0}}, {{2}, {1}}]
  = {0, 0}

Map :math:`f` onto the last element of a list:

>>> MapAt[f, {a, b, c}, -1]
  = {a, b, f[c]}

Same as above, but use the operator form of :code:`MapAt` :

>>> MapAt[f, -1][{a, b, c}]
  = {a, b, f[c]}

Map :math:`f` onto at the second position of an association:

>>> MapAt[f, <|"a" -> 1, "b" -> 2, "c" -> 3, "d" -> 4|>, 2]
  = {a -> 1, b -> f[2], c -> 3, d -> 4}

Same as above, but select the second-from-the-end position:

>>> MapAt[f, <|"a" -> 1, "b" -> 2, "c" -> 3, "d" -> 4|>, -2]
  = {a -> 1, b -> 2, c -> f[3], d -> 4}
