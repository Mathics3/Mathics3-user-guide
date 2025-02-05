Curve Sketching
===============

Let's sketch the function

>>> f[x_] := 4 x / (x ^ 2 + 3 x + 5)


The derivatives are:

>>> {f'[x], f''[x], f'''[x]} // Together
  = {-4 (-5 + x ^ 2) / (5 + 3 x + x ^ 2) ^ 2, 8 (-15 - 15 x + x ^ 3) / (5 + 3 x + x ^ 2) ^ 3, -24 (-20 - 60 x - 30 x ^ 2 + x ^ 4) / (5 + 3 x + x ^ 2) ^ 4}

To get the extreme values of :code:`f` , compute the zeroes of the first derivatives:

>>> extremes = Solve[f'[x] == 0, x]
  = {{x -> -Sqrt[5]}, {x -> Sqrt[5]}}

And test the second derivative:

>>> f''[x] /. extremes // N
  = {1.65086, -0.064079}

Thus, there is a local maximum at :code:`x = Sqrt[5]`  and a local minimum at :code:`x = -Sqrt[5]` .
Compute the inflection points numerically, chopping imaginary parts close to 0:

>>> inflections = Solve[f''[x] == 0, x] // N // Chop
  = {{x -> -1.0852}, {x -> -3.21463}, {x -> 4.29983}}

Insert into the third derivative:

>>> f'''[x] /. inflections
  = {-3.67683, 0.694905, 0.00671894}

Being different from 0, all three points are actual inflection points.
:code:`f`  is not defined where its denominator is 0:

>>> Solve[Denominator[f[x]] == 0, x]
  = {{x -> -3 / 2 - I / 2 Sqrt[11]}, {x -> -3 / 2 + I / 2 Sqrt[11]}}

These are non-real numbers, consequently :code:`f`  is defined on all real numbers.
The behaviour of :code:`f`  at the boundaries of its definition:

>>> Limit[f[x], x -> Infinity]
  = 0
>>> Limit[f[x], x -> -Infinity]
  = 0

Finally, let's plot :code:`f` :

>>> Plot[f[x], {x, -8, 6}]
  = -Graphics-
