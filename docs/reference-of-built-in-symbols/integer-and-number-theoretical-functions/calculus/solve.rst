Solve
=====

`Equation solving <https://en.wikipedia.org/wiki/Equation_solving>`_ (`SymPy <https://docs.sympy.org/latest/modules/solvers/solvers.html#module-sympy.solvers>`_,     `WMA <https://reference.wolfram.com/language/ref/Solve.html>`_)


:code:`Solve` [:math:`equation`, :math:`vars`]
    attempts to solve :math:`equation` for the variables :math:`vars`.

:code:`Solve` [:math:`equation`, :math:`vars`, :math:`domain`]
    restricts variables to :math:`domain`, which can be :code:`Complexes`           or :code:`Reals`  or :code:`Integers` .





>>> Solve[x ^ 2 - 3 x == 4, x]
  = {{x -> -1}, {x -> 4}}
>>> Solve[4 y - 8 == 0, y]
  = {{y -> 2}}

Apply the solution:

>>> sol = Solve[2 x^2 - 10 x - 12 == 0, x]
  = {{x -> -1}, {x -> 6}}
>>> x /. sol
  = {-1, 6}

Contradiction:

>>> Solve[x + 1 == x, x]
  = {}

Tautology:

>>> Solve[x ^ 2 == x ^ 2, x]
  = {{}}

Rational equations:

>>> Solve[x / (x ^ 2 + 1) == 1, x]
  = {{x -> 1 / 2 - I / 2 Sqrt[3]}, {x -> 1 / 2 + I / 2 Sqrt[3]}}
>>> Solve[(x^2 + 3 x + 2)/(4 x - 2) == 0, x]
  = {{x -> -2}, {x -> -1}}

Transcendental equations:

>>> Solve[Cos[x] == 0, x]
  = {{x -> Pi / 2}, {x -> 3 Pi / 2}}

Solve can only solve equations with respect to symbols or functions:

>>> Solve[f[x + y] == 3, f[x + y]]
  = {{f[x + y] -> 3}}
>>> Solve[a + b == 2, a + b]
  = Solve[a + b == 2, a + b]

This happens when solving with respect to an assigned symbol:

>>> x = 3;

>>> Solve[x == 2, x]
  = Solve[False, 3]
>>> Clear[x]

>>> Solve[a < b, a]
  = Solve[a < b, a]

Solve a system of equations:

>>> eqs = {3 x ^ 2 - 3 y == 0, 3 y ^ 2 - 3 x == 0};

>>> sol = Solve[eqs, {x, y}] // Simplify
  = {{x -> 0, y -> 0}, {x -> 1, y -> 1}, {x -> -1 / 2 + I / 2 Sqrt[3], y -> -1 / 2 - I / 2 Sqrt[3]}, {x -> -1 / 2 - I / 2 Sqrt[3], y -> -1 / 2 + I / 2 Sqrt[3]}}
>>> eqs /. sol // Simplify
  = {{True, True}, {True, True}, {True, True}, {True, True}}

Solve when given an underdetermined system:

>>> Solve[x^2 == 1 && z^2 == -1, {x, y, z}]
  = {{x -> -1, z -> -I}, {x -> -1, z -> I}, {x -> 1, z -> -I}, {x -> 1, z -> I}}

Examples using specifying the Domain in solutions:

>>> Solve[x^2 == -1, x, Reals]
  = {}
>>> Solve[x^2 == 1, x, Reals]
  = {{x -> -1}, {x -> 1}}
>>> Solve[x^2 == -1, x, Complexes]
  = {{x -> -I}, {x -> I}}
>>> Solve[4 - 4 * x^2 - x^4 + x^6 == 0, x, Integers]
  = {{x -> -1}, {x -> 1}}
