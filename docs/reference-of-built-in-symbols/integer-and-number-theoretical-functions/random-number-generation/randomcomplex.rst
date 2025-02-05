RandomComplex
=============

`WMA link <https://reference.wolfram.com/language/ref/RandomComplex.html>`_


:code:`RandomComplex` [{:math:`z_{min}`, :math:`z_{max}`}]
    yields a pseudorandom complex number in the rectangle with complex corners           :math:`z_{min}` and :math:`z_{max}`.

:code:`RandomComplex` [:math:`z_{max}`]
    yields a pseudorandom complex number in the rectangle with corners at the           origin and at :math:`z_{max}`.

:code:`RandomComplex[]`
    yields a pseudorandom complex number with real and imaginary parts from 0           to 1.

:code:`RandomComplex` [:math:`range`, :math:`n`]
    gives a list of :math:`n` pseudorandom complex numbers.

:code:`RandomComplex` [:math:`range`, {:math:`n_1`, :math:`n_2`, ...}]
    gives a nested list of pseudorandom complex numbers.





>>> RandomComplex[]
  = ...
>>> RandomComplex[{1+I, 5+5I}]
  = ...
>>> RandomComplex[1+I, 5]
  = {..., ..., ..., ..., ...}
>>> RandomComplex[{1+I, 2+2I}, {2, 2}]
  = {{..., ...}, {..., ...}}
