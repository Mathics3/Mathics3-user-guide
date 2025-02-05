LogGamma
========

`log-gamma function <https://en.wikipedia.org/wiki/Gamma_function#The_log-gamma_function>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.gamma_functions.loggamma>`_, `WMA <https://reference.wolfram.com/language/ref/LogGamma.html>`_)

:code:`LogGamma` [:math:`z`]
    is the logarithm of the gamma function on the complex number :math:`z`.





>>> LogGamma[3]
  = Log[2]

LogGamma[z] has different analytical structure than Log[Gamma[z]]

>>> LogGamma[-2.+3 I]
  = -6.77652 - 4.56879 I
>>> Log[Gamma[-2.+3 I]]
  = -6.77652 + 1.71439 I

LogGamma also can be evaluated for large arguments, for which Gamma produces Overflow:

>>> LogGamma[1.*^20]
  = 4.50517×10^21
>>> Log[Gamma[1.*^20]]
  = Overflow[]
