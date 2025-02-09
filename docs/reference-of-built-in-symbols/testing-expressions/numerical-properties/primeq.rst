PrimeQ
======

`WMA link <https://reference.wolfram.com/language/ref/PrimeQ.html>`_


:code:`PrimeQ` [:math:`n`]
    returns :code:`True`  if :math:`n` is a prime number.





For very large numbers, :code:`PrimeQ`  uses probabilistic prime testing, so it might be wrong sometimes
(a number might be composite even though :code:`PrimeQ`  says it is prime).
The algorithm might be changed in the future.

>>> PrimeQ[2]

    =
:math:`\text{True}`


>>> PrimeQ[-3]

    =
:math:`\text{True}`


>>> PrimeQ[137]

    =
:math:`\text{True}`


>>> PrimeQ[2 ^ 127 - 1]

    =
:math:`\text{True}`



All prime numbers between 1 and 100:

>>> Select[Range[100], PrimeQ]

    =
:math:`\left\{2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97\right\}`



:code:`PrimeQ`  has attribute :code:`Listable` :

>>> PrimeQ[Range[20]]

    =
:math:`\left\{\text{False},\text{True},\text{True},\text{False},\text{True},\text{False},\text{True},\text{False},\text{False},\text{False},\text{True},\text{False},\text{True},\text{False},\text{False},\text{False},\text{True},\text{False},\text{True},\text{False}\right\}`


