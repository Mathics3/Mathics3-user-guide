Solve
=====

`Equation solving <https://en.wikipedia.org/wiki/Equation_solving>`_ (`SymPy <https://docs.sympy.org/latest/modules/solvers/solvers.html#module-sympy.solvers>`_,     `WMA <https://reference.wolfram.com/language/ref/Solve.html>`_)


:code:`Solve` [:math:`equation`, :math:`vars`]
    attempts to solve :math:`equation` for the variables :math:`vars`.

:code:`Solve` [:math:`equation`, :math:`vars`, :math:`domain`]
    restricts variables to :math:`domain`, which can be :code:`Complexes`           or :code:`Reals`  or :code:`Integers` .





>>> Solve[x ^ 2 - 3 x == 4, x]

    =
:math:`\left\{\left\{x->-1\right\},\left\{x->4\right\}\right\}`


>>> Solve[4 y - 8 == 0, y]

    =
:math:`\left\{\left\{y->2\right\}\right\}`



Apply the solution:

>>> sol = Solve[2 x^2 - 10 x - 12 == 0, x]

    =
:math:`\left\{\left\{x->-1\right\},\left\{x->6\right\}\right\}`


>>> x /. sol

    =
:math:`\left\{-1,6\right\}`



Contradiction:

>>> Solve[x + 1 == x, x]

    =
:math:`\left\{\right\}`



Tautology:

>>> Solve[x ^ 2 == x ^ 2, x]

    =
:math:`\left\{\left\{\right\}\right\}`



Rational equations:

>>> Solve[x / (x ^ 2 + 1) == 1, x]

    =
:math:`\left\{\left\{x->\frac{1}{2}-\frac{I}{2} \sqrt{3}\right\},\left\{x->\frac{1}{2}+\frac{I}{2} \sqrt{3}\right\}\right\}`


>>> Solve[(x^2 + 3 x + 2)/(4 x - 2) == 0, x]

    =
:math:`\left\{\left\{x->-2\right\},\left\{x->-1\right\}\right\}`



Transcendental equations:

>>> Solve[Cos[x] == 0, x]

    =
:math:`\left\{\left\{x->\frac{ \pi }{2}\right\},\left\{x->\frac{3  \pi }{2}\right\}\right\}`



Solve can only solve equations with respect to symbols or functions:

>>> Solve[f[x + y] == 3, f[x + y]]

    =
:math:`\left\{\left\{f\left[x+y\right]->3\right\}\right\}`


>>> Solve[a + b == 2, a + b]

    Solve::ivar a + b is not a valid variable.

    =
:math:`\text{Solve}\left[a+b\text{==}2,a+b\right]`



This happens when solving with respect to an assigned symbol:

>>> x = 3;


>>> Solve[x == 2, x]

    Solve::ivar 3 is not a valid variable.

    =
:math:`\text{Solve}\left[\text{False},3\right]`


>>> Clear[x]


>>> Solve[a < b, a]

    Solve::eqf a < b is not a well-formed equation.

    =
:math:`\text{Solve}\left[a<b,a\right]`



Solve a system of equations:

>>> eqs = {3 x ^ 2 - 3 y == 0, 3 y ^ 2 - 3 x == 0};


>>> sol = Solve[eqs, {x, y}] // Simplify

    =
:math:`\left\{\left\{x->0,y->0\right\},\left\{x->1,y->1\right\},\left\{x->-\frac{1}{2}+\frac{I}{2} \sqrt{3},y->-\frac{1}{2}-\frac{I}{2} \sqrt{3}\right\},\left\{x->-\frac{1}{2}-\frac{I}{2} \sqrt{3},y->-\frac{1}{2}+\frac{I}{2} \sqrt{3}\right\}\right\}`


>>> eqs /. sol // Simplify

    =
:math:`\left\{\left\{\text{True},\text{True}\right\},\left\{\text{True},\text{True}\right\},\left\{\text{True},\text{True}\right\},\left\{\text{True},\text{True}\right\}\right\}`



Solve when given an underdetermined system:

>>> Solve[x^2 == 1 && z^2 == -1, {x, y, z}]

    Solve::svars Equations may not give solutions for all "solve" variables.

    =
:math:`\left\{\left\{x->-1,z->-I\right\},\left\{x->-1,z->I\right\},\left\{x->1,z->-I\right\},\left\{x->1,z->I\right\}\right\}`



Examples using specifying the Domain in solutions:

>>> Solve[x^2 == -1, x, Reals]

    =
:math:`\left\{\right\}`


>>> Solve[x^2 == 1, x, Reals]

    =
:math:`\left\{\left\{x->-1\right\},\left\{x->1\right\}\right\}`


>>> Solve[x^2 == -1, x, Complexes]

    =
:math:`\left\{\left\{x->-I\right\},\left\{x->I\right\}\right\}`


>>> Solve[4 - 4 * x^2 - x^4 + x^6 == 0, x, Integers]

    =
:math:`\left\{\left\{x->-1\right\},\left\{x->1\right\}\right\}`


