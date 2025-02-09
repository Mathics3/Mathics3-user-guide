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

    =
:math:`17`


>>> RandomPrime[{14, 16}, 1]

    RandomPrime::noprime There are no primes in the specified interval.

    =
:math:`\text{RandomPrime}\left[\left\{14,16\right\},1\right]`


>>> RandomPrime[{8,12}, 3]

    =
:math:`\left\{11,11,11\right\}`


>>> RandomPrime[{10,30}, {2,5}]

    =
:math:`\left\{\left\{23,23,23,23,23\right\},\left\{23,23,23,23,23\right\}\right\}`


