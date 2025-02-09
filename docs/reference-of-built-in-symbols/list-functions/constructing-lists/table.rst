Table
=====

`WMA link <https://reference.wolfram.com/language/ref/Table.html>`_


:code:`Table` [:math:`expr`, :math:`n`]
    generates a list of :math:`n` copies of :math:`expr`.

:code:`Table` [:math:`expr`, {:math:`i`, :math:`n`}]
    generates a list of the values of expr when :math:`i` runs from 1 to :math:`n`.

:code:`Table` [:math:`expr`, {:math:`i`, :math:`start`, :math:`stop`, :math:`step`}]
    evaluates :math:`expr` with :math:`i` ranging from :math:`start` to :math:`stop`, incrementing by :math:`step`.

:code:`Table` [:math:`expr`, {:math:`i`, {:math:`e_1`, :math:`e_2`, ..., :math:`ei`}}]
    evaluates :math:`expr` with :math:`i` taking on the values :math:`e_1`, :math:`e_2`, ..., :math:`ei`.





>>> Table[x, 3]

    =
:math:`\left\{x,x,x\right\}`


>>> n = 0; Table[n = n + 1, {5}]

    =
:math:`\left\{1,2,3,4,5\right\}`


>>> Clear[n]
    = `

>>> Table[i, {i, 4}]

    =
:math:`\left\{1,2,3,4\right\}`


>>> Table[i, {i, 2, 5}]

    =
:math:`\left\{2,3,4,5\right\}`


>>> Table[i, {i, 2, 6, 2}]

    =
:math:`\left\{2,4,6\right\}`


>>> Table[i, {i, Pi, 2 Pi, Pi / 2}]

    =
:math:`\left\{ \pi ,\frac{3  \pi }{2},2  \pi \right\}`


>>> Table[x^2, {x, {a, b, c}}]

    =
:math:`\left\{a^2,b^2,c^2\right\}`



:code:`Table`  supports multi-dimensional tables:

>>> Table[{i, j}, {i, {a, b}}, {j, 1, 2}]

    =
:math:`\left\{\left\{\left\{a,1\right\},\left\{a,2\right\}\right\},\left\{\left\{b,1\right\},\left\{b,2\right\}\right\}\right\}`



Symbolic bounds:

>>> Table[x, {x, a, a + 5 n, n}]

    =
:math:`\left\{a,5+a,10+a,15+a,20+a,25+a\right\}`



The lower bound is always included even for large step sizes:

>>> Table[i, {i, 1, 9, Infinity}]

    =
:math:`\left\{1\right\}`


