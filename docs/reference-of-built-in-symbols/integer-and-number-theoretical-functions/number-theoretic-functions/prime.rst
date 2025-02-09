Prime
=====

`WMA link <https://reference.wolfram.com/language/ref/Prime.html>`_


:code:`Prime` [:math:`n`]
    same as

:code:`Prime` [{:math:`n_0`, :math:`n_1`, ...}]
    returns the :math:`n`th prime number where :math:`n` is an positive Integer.
    If given a list of integers, the return value is a list with :code:`Prime`  applied to each.





Note that the first prime is 2, not 1:

>>> Prime[1]

    =
:math:`2`


>>> Prime[167]

    =
:math:`991`



When given a list of integers, a list is returned:

>>> Prime[{5, 10, 15}]

    =
:math:`\left\{11,29,47\right\}`



1.2 isn't an integer

>>> Prime[1.2]

    =
:math:`\text{Prime}\left[1.2\right]`



Since 0 is less than 1, like 1.2 it is invalid.

>>> Prime[{0, 1, 1.2, 3}]

    =
:math:`\left\{\text{Prime}\left[0\right],2,\text{Prime}\left[1.2\right],5\right\}`


