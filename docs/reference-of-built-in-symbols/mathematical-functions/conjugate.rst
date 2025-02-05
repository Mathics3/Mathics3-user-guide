Conjugate
=========

`Complex Conjugate <https://en.wikipedia.org/wiki/Complex_conjugate>`_     `WMA link <https://reference.wolfram.com/language/ref/Conjugate.html>`_


:code:`Conjugate` [:math:`z`]
    returns the complex conjugate of the complex number :math:`z`.





>>> Conjugate[3 + 4 I]
  = 3 - 4 I
>>> Conjugate[3]
  = 3
>>> Conjugate[a + b * I]
  = Conjugate[a] - I Conjugate[b]
>>> Conjugate[{{1, 2 + I 4, a + I b}, {I}}]
  = {{1, 2 - 4 I, Conjugate[a] - I Conjugate[b]}, {-I}}
>>> Conjugate[1.5 + 2.5 I]
  = 1.5 - 2.5 I
