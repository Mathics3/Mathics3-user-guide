ComplexExpand
=============

(`SymPy <https://docs.sympy.org/latest/modules/core.html#sympy.core.expr.Expr.expand>`_, `WMA <https://reference.wolfram.com/language/ref/ComplexExpand.html>`_)


:code:`ComplexExpand` [:math:`expr`]
    expands :math:`expr` assuming that all variables are real.

:code:`ComplexExpand` [:math:`expr`,{:math:`x_1`,:math:`x_2`, ...}]
    expands :math:`expr` assuming that variables matching any of the :math:`xi` are complex.





Note: we get equivalent, but different results from WMA:

>>> ComplexExpand[3^(I x)]

    =
:math:`3^{-\text{Im}\left[x\right]} \text{Re}\left[3^{I \text{Re}\left[x\right]}\right]+I \text{Im}\left[3^{I \text{Re}\left[x\right]}\right] 3^{-\text{Im}\left[x\right]}`



Assume that both :math:`x` and :math:`y` and are real:

>>> ComplexExpand[Sin[x + I y]]

    =
:math:`\text{Cosh}\left[y\right] \text{Sin}\left[x\right]+I \text{Cos}\left[x\right] \text{Sinh}\left[y\right]`



Take :math:`x` to be complex:

>>> ComplexExpand[Sin[x], x]

    =
:math:`\text{Cosh}\left[\text{Im}\left[x\right]\right] \text{Sin}\left[\text{Re}\left[x\right]\right]+I \text{Cos}\left[\text{Re}\left[x\right]\right] \text{Sinh}\left[\text{Im}\left[x\right]\right]`



Polynomials:

>>> ComplexExpand[Re[z^5 - 2 z^3 - z + 1], z]

    =
:math:`1+\text{Re}\left[z\right]^5-2 \text{Re}\left[z\right]^3-\text{Re}\left[z\right]-10 \text{Im}\left[z\right]^2 \text{Re}\left[z\right]^3+5 \text{Im}\left[z\right]^4 \text{Re}\left[z\right]+6 \text{Im}\left[z\right]^2 \text{Re}\left[z\right]`



Trigonometric and hyperbolic functions

>>> ComplexExpand[Cos[x + I y] + Tanh[z], {z}]

    =
:math:`\text{Cos}\left[x\right] \text{Cosh}\left[y\right]-I \text{Sin}\left[x\right] \text{Sinh}\left[y\right]+\frac{\text{Cosh}\left[\text{Re}\left[z\right]\right] \text{Sinh}\left[\text{Re}\left[z\right]\right]}{\text{Cos}\left[\text{Im}\left[z\right]\right]^2+\text{Sinh}\left[\text{Re}\left[z\right]\right]^2}+\frac{I \text{Cos}\left[\text{Im}\left[z\right]\right] \text{Sin}\left[\text{Im}\left[z\right]\right]}{\text{Cos}\left[\text{Im}\left[z\right]\right]^2+\text{Sinh}\left[\text{Re}\left[z\right]\right]^2}`



Exponential and logarithmic functions:

>>> ComplexExpand[Abs[2^z Log[2 z]], z]

    =
:math:`\text{Abs}\left[I \text{Arg}\left[\text{Re}\left[z\right]+I \text{Im}\left[z\right]\right]+\frac{\text{Log}\left[4 \text{Im}\left[z\right]^2+4 \text{Re}\left[z\right]^2\right]}{2}\right] 2^{\text{Re}\left[z\right]}`



Specify that variable :math:`z` is taken to be complex:

>>> ComplexExpand[Re[2 z^3 - z + 1], z]

    =
:math:`1-\text{Re}\left[z\right]+2 \text{Re}\left[z\right]^3-6 \text{Im}\left[z\right]^2 \text{Re}\left[z\right]`


