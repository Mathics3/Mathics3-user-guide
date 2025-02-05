PolyGamma
=========

`Polygamma function <https://en.wikipedia.org/wiki/Polygamma_function>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.gamma_functions.polygamma>`_, `WMA <https://reference.wolfram.com/language/ref/PolyGamma.html>`_)

PolyGamma is a meromorphic function on the complex numbers and is defined as a derivative of the logarithm of the gamma function.

PolyGamma[z]
    returns the digamma function.

PolyGamma[n,z]
    gives the n^(th) derivative of the digamma function.





>>> PolyGamma[5]
  = 25 / 12 - EulerGamma
>>> PolyGamma[3, 5]
  = -22369 / 3456 + Pi ^ 4 / 15
