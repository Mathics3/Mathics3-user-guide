Curve Sketching
===============

Let's sketch the function

>>> f[x_] := 4 x / (x ^ 2 + 3 x + 5)



The derivatives are:

>>> {f'[x], f''[x], f'''[x]} // Together

    =
:math:`\left\{\frac{-4 \left(-5+x^2\right)}{{\left(5+3 x+x^2\right)}^2},\frac{8 \left(-15-15 x+x^3\right)}{{\left(5+3 x+x^2\right)}^3},\frac{-24 \left(-20-60 x-30 x^2+x^4\right)}{{\left(5+3 x+x^2\right)}^4}\right\}`



To get the extreme values of :code:`f` , compute the zeroes of the first derivatives:

>>> extremes = Solve[f'[x] == 0, x]

    =
:math:`\left\{\left\{x->-\sqrt{5}\right\},\left\{x->\sqrt{5}\right\}\right\}`



And test the second derivative:

>>> f''[x] /. extremes // N

    =
:math:`\left\{1.65086,-0.064079\right\}`



Thus, there is a local maximum at :code:`x = Sqrt[5]`  and a local minimum at :code:`x = -Sqrt[5]` .
Compute the inflection points numerically, chopping imaginary parts close to 0:

>>> inflections = Solve[f''[x] == 0, x] // N // Chop

    =
:math:`\left\{\left\{x->-1.0852\right\},\left\{x->-3.21463\right\},\left\{x->4.29983\right\}\right\}`



Insert into the third derivative:

>>> f'''[x] /. inflections

    =
:math:`\left\{-3.67683,0.694905,0.00671894\right\}`



Being different from 0, all three points are actual inflection points.
:code:`f`  is not defined where its denominator is 0:

>>> Solve[Denominator[f[x]] == 0, x]

    =
:math:`\left\{\left\{x->-\frac{3}{2}-\frac{I}{2} \sqrt{11}\right\},\left\{x->-\frac{3}{2}+\frac{I}{2} \sqrt{11}\right\}\right\}`



These are non-real numbers, consequently :code:`f`  is defined on all real numbers.
The behaviour of :code:`f`  at the boundaries of its definition:

>>> Limit[f[x], x -> Infinity]

    =
:math:`0`


>>> Limit[f[x], x -> -Infinity]

    =
:math:`0`



Finally, let's plot :code:`f` :

>>> Plot[f[x], {x, -8, 6}]

    =
.. image:: tmp1h__d952.png
    :align: center



