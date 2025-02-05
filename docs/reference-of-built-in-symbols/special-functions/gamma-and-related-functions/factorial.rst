Factorial
=========

`Factorial <https://en.wikipedia.org/wiki/Factorial>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/combinatorial.html#factorial>`_, `mpmath <https://mpmath.org/doc/current/functions/gamma.html#mpmath.factorial>`_, `WMA <https://reference.wolfram.com/language/ref/Factorial.html>`_)


:code:`Factorial` [:math:`n`]
    same as

:code:`:math:`n`!`
    computes the factorial of :math:`n`.





>>> 20!
  = 2432902008176640000

:code:`Factorial`  handles numeric (real and complex) values using the gamma function:

>>> 10.5!
  = 1.18994×10^7
>>> (-3.0+1.5*I)!
  = 0.0427943 - 0.00461565 I

However, the value at poles is :code:`ComplexInfinity` :

>>> (-1.)!
  = ComplexInfinity

:code:`Factorial`  has the same operator (:code:`!` ) as :code:`Not` , but with higher precedence:

>>> !a! //FullForm
  = Not[Factorial[a]]
