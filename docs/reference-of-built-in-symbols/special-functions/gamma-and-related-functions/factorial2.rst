Factorial2
==========

`WMA link <https://reference.wolfram.com/language/ref/Factorial2.html>`_


:code:`Factorial2` [:math:`n`]
    same as

:code:`:math:`n`!!`
    computes the double factorial of :math:`n`.





The double factorial or semifactorial of a number :math:`n`, is the product of all the     integers from 1 up to n that have the same parity (odd or even) as :math:`n`.

>>> 5!!
    =

:math:`15.`


>>> Factorial2[-3]
    =

:math:`-1.`



:code:`Factorial2`  accepts Integers, Rationals, Reals, or Complex Numbers:

>>> I!! + 1
    =

:math:`3.71713+0.279527 I`



Irrationals can be handled by using numeric approximation:

>>> N[Pi!!, 6]
    =

:math:`3.35237`


