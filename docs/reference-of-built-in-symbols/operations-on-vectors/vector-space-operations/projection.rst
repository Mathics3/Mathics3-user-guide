Projection
==========

`WMA link <https://reference.wolfram.com/language/ref/Projection.html>`_


:code:`Projection` [:math:`u`, :math:`v`]
    gives the projection of the vector :math:`u` onto :math:`v`





For vectors :math:`u` and :math:`v`, the projection is taken to be ( :math:`v` . :math:`u` / :math:`v` . :math:`v` ) :math:`v`

For complex vectors :math:`u` and :math:`v`, the projection is taken to be ( :math:`v`* . :math:`u` / :math:`v`* . :math:`v` ) :math:`v` where :math:`v`* is :code:`Conjugate[v]` .

Projection of two three-dimensional Integer vectors:

>>> Projection[{5, 6, 7}, {1, 0, 0}]
  = {5, 0, 0}

Projection of two two-dimensional Integer vectors:

>>> Projection[{2, 3}, {1, 2}]
  = {8 / 5, 16 / 5}

Projection of a machine-precision vector onto another:

>>> Projection[{1.3, 2.1, 3.1}, {-0.3, 4.2, 5.3}]
  = {-0.162767, 2.27874, 2.87556}

Projection of two complex vectors:

>>> Projection[{3 + I, 2, 2 - I}, {2, 4, 5 I}]
  = {2 / 5 - 16 I / 45, 4 / 5 - 32 I / 45, 8 / 9 + I}

Project a symbol vector onto a numeric vector:

>>> Projection[{a, b, c}, {1, 1, 1}]
  = {(a + b + c) / 3, (a + b + c) / 3, (a + b + c) / 3}

The projection of vector :math:`u` onto vector :math:`v` is in the direction of :math:`v`:

>>> {u, v} = RandomReal[1, {2, 6}];

>>> Abs[VectorAngle[Projection[u, v], v]] < 0. + 10^-7
  = True
