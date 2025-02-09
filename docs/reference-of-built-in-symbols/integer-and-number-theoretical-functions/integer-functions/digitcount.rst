DigitCount
==========

`WMA link <https://reference.wolfram.com/language/ref/DigitCount.html>`_


:code:`DigitCount` [:math:`n`, :math:`b`, :math:`d`]
    returns the number of times digit :math:`d` occurs in the base :math:`b` representation of :math:`n`.

:code:`DigitCount` [:math:`n`, :math:`b`]
    returns a list indicating the number of times each digit occurs in the base :math:`b` representation of :math:`n`.

:code:`DigitCount` [:math:`n`, :math:`b`]
    returns a list indicating the number of times each digit occurs in the decimal representation of :math:`n`.





>>> DigitCount[1022]

    =
:math:`\left\{1,2,0,0,0,0,0,0,0,1\right\}`


>>> DigitCount[Floor[Pi * 10^100]]

    =
:math:`\left\{8,12,12,10,8,9,8,12,14,8\right\}`


>>> DigitCount[1022, 2]

    =
:math:`\left\{9,1\right\}`


>>> DigitCount[1022, 2, 1]

    =
:math:`9`


