RandomPrime
===========

`Prime numbers <https://reference.wolfram.com/language/ref/RandomPrime.html>`_


:code:`RandomPrime` [{:math:`i_{min}`, :math:`i_{max}`}]
    gives a random prime between :math:`i_{min}` and :math:`i_{max}`.

:code:`RandomPrime` [:math:`i_{max}`]
    gives a random prime between 2 and :math:`i_{max}`.

:code:`RandomPrime` [:math:`range`, :math:`n`]
    gives a list of :math:`n` random primes in :math:`range`.





>>> RandomPrime[{14, 17}]
  = 17
>>> RandomPrime[{14, 16}, 1]
  = RandomPrime[{14, 16}, 1]
>>> RandomPrime[{8,12}, 3]
  = {11, 11, 11}
>>> RandomPrime[{10,30}, {2,5}]
  = ...
