NextPrime
=========

`WMA link <https://reference.wolfram.com/language/ref/NextPrime.html>`_


:code:`NextPrime` [:math:`n`]
    gives the next prime after :math:`n`.

:code:`NextPrime` [:math:`n`,:math:`k`]
    gives the :math:`k`th  prime after :math:`n`.





>>> NextPrime[100]

    =
:math:`101`



The the first number does not have to be an integer:

>>> NextPrime[100.5, 2]

    =
:math:`103`



However, when the second value, the step value is not an integer is given, we do nothing:

>>> NextPrime[100, 2.5]

    =
:math:`\text{NextPrime}\left[100,2.5\right]`



With a negative number, we find a prime number *before* the given number:

>>> NextPrime[100, -1]

    =
:math:`97`



And with negative counts, it is possible to get *negative* prime numbers:

>>> NextPrime[2, -1]

    =
:math:`-2`


