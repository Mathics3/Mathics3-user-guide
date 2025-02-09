Projection
==========

`WMA link <https://reference.wolfram.com/language/ref/Projection.html>`_


:code:`Projection` [:math:`u`, :math:`v`]
    gives the projection of the vector :math:`u` onto :math:`v`





For vectors :math:`u` and :math:`v`, the projection is taken to be ( :math:`v` . :math:`u` / :math:`v` . :math:`v` ) :math:`v`

For complex vectors :math:`u` and :math:`v`, the projection is taken to be ( :math:`v`* . :math:`u` / :math:`v`* . :math:`v` ) :math:`v` where :math:`v`* is :code:`Conjugate[v]` .

Projection of two three-dimensional Integer vectors:

>>> Projection[{5, 6, 7}, {1, 0, 0}]

    =
:math:`\left\{5,0,0\right\}`



Projection of two two-dimensional Integer vectors:

>>> Projection[{2, 3}, {1, 2}]

    =
:math:`\left\{\frac{8}{5},\frac{16}{5}\right\}`



Projection of a machine-precision vector onto another:

>>> Projection[{1.3, 2.1, 3.1}, {-0.3, 4.2, 5.3}]

    =
:math:`\left\{-0.162767,2.27874,2.87556\right\}`



Projection of two complex vectors:

>>> Projection[{3 + I, 2, 2 - I}, {2, 4, 5 I}]

    =
:math:`\left\{\frac{2}{5}-\frac{16 I}{45},\frac{4}{5}-\frac{32 I}{45},\frac{8}{9}+I\right\}`



Project a symbol vector onto a numeric vector:

>>> Projection[{a, b, c}, {1, 1, 1}]

    =
:math:`\left\{\frac{a+b+c}{3},\frac{a+b+c}{3},\frac{a+b+c}{3}\right\}`



The projection of vector :math:`u` onto vector :math:`v` is in the direction of :math:`v`:

>>> {u, v} = RandomReal[1, {2, 6}];


>>> Abs[VectorAngle[Projection[u, v], v]] < 0. + 10^-7

    =
:math:`\text{True}`


