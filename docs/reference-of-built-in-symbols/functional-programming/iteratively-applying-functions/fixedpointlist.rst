FixedPointList
==============

`WMA link <https://reference.wolfram.com/language/ref/FixedPointList.html>`_


:code:`FixedPointList` [:math:`f`, :math:`expr`]
    starting with :math:`expr`, iteratively applies :math:`f` until the result no longer changes,           and returns a list of all intermediate results.

:code:`FixedPointList` [:math:`f`, :math:`expr`, :math:`n`]
    performs at most :math:`n` iterations.





>>> FixedPointList[Cos, 1.0, 4]
    =

:math:`\left\{1.,0.540302,0.857553,0.65429,0.79348\right\}`



Observe the convergence of Newton's method for approximating square roots:

>>> newton[n_] := FixedPointList[.5(# + n/#) &, 1.];


>>> newton[9]
    =

:math:`\left\{1.,5.,3.4,3.02353,3.00009,3.,3.,3.\right\}`



Compute the `Hailstone Number <https://mathworld.wolfram.com/HailstoneNumber.html>`_: for 14:

>>> collatz[1] := 1;


>>> collatz[x_ ? EvenQ] := x / 2;


>>> collatz[x_] := 3 x + 1;


>>> list = FixedPointList[collatz, 14]
    =

:math:`\left\{14,7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1,1\right\}`



Plot this:

>>> ListLinePlot[list]
    =

.. image:: tmp_bw7ni5x.png
    :align: center



