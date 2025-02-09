SeedRandom
==========

`WMA link <https://reference.wolfram.com/language/ref/SeedRandom.html>`_

:code:`SeedRandom` [:math:`n`]
    resets the pseudorandom generator with seed :math:`n`.

:code:`SeedRandom[]`
    uses the current date and time as the seed.





:code:`SeedRandom`  can be used to get reproducible random numbers:

>>> SeedRandom[42]


>>> RandomInteger[100]

    =
:math:`51`


>>> RandomInteger[100]

    =
:math:`92`


>>> SeedRandom[42]


>>> RandomInteger[100]

    =
:math:`51`


>>> RandomInteger[100]

    =
:math:`92`



String seeds are supported as well:

>>> SeedRandom["Mathics"]


>>> RandomInteger[100]

    =
:math:`27`



Calling :code:`SeedRandom`  without arguments will seed the random
number generator to a random state:

>>> SeedRandom[]


>>> RandomInteger[100]

    =
:math:`95`


