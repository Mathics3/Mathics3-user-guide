BernsteinBasis
==============

`Bernstein polynomial basis <https://en.wikipedia.org/wiki/Bernstein_polynomial>`_ (`SciPy <https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.BPoly.html>`_ :WMA:

A Bernstein is a polynomial that is a linear combination of Bernstein basis polynomials.
With the advent of computer graphics, Bernstein polynomials, restricted to the interval [0, 1], became important in the form of Bézier curves.
:code:`BernsteinBasis[d,n,x]`  equals :code:`Binomial[d, n] x^n (1-x)^(d-n)`  in the interval [0, 1] and zero elsewhere.


:code:`BernsteinBasis` [:math:`d`,:math:`n`,:math:`x`]
    returns the :math:`n`th Bernstein basis of degree :math:`d` at :math:`x`.





>>> BernsteinBasis[4, 3, 0.5]
  = 0.25
