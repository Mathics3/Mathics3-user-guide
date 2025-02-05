DivisorSigma
============

`Divisor function <https://en.wikipedia.org/wiki/Divisor_function>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/combinatorial.html#sympy.functions.combinatorial.numbers.divisor_sigma>`_, `WMA <https://reference.wolfram.com/language/ref/DivisorSigma.html>`_)


:code:`DivisorSigma` [:math:`k`, :math:`n`]
    returns :math:`\sigma_k(n)`





For reference, let us first get the integer divisors of 20:

>>> Divisors[20]
  = {1, 2, 4, 5, 10, 20}

The DivisorSigma function counts this sum:

>>> DivisorSigma[1, 20]
  = 42

This is the same thing as:

>>> DivisorSum[20, # &]
  = 42

To get a sum of the second power of the factors of 20:

>>> DivisorSigma[2, 20]
  = 546

Doing this with :code:`DivisorSum`  instead:

>>> DivisorSum[20, #^2 &]
  = 546

See also `:code:`DivisorSum`  </doc/reference-of-built-in-symbols/integer-and-number-theoretical-functions/number-theoretic-functions/divisorsum/>`_ and `Divisors </doc/reference-of-built-in-symbols/integer-and-number-theoretical-functions/number-theoretic-functions/divisors/>`_.