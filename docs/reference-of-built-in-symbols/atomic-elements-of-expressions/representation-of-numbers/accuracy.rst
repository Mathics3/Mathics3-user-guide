Accuracy
========

`Accuracy <https://en.wikipedia.org/wiki/Accuracy_and_precision>`_    (WMA `Accuracy <https://reference.wolfram.com/language/ref/Accuracy.html>`_)


:code:`Accuracy` [:math:`x`]
    examines the number of significant digits of :math:`expr` after the       decimal point in the number x.





*Notice that the result could be slightly different from the result obtained     in WMA, due to differences in the internal representation of the real numbers.*

:code:`Accuracy`  of a real number is estimated from its value and its precision:

>>> Accuracy[3.1416`2]

    =
:math:`1.50298`



Notice that the value is not exactly equal to the obtained in WMA:     This is due to the different way in which :code:`Precision`  is handled in SymPy.

Accuracy for exact atoms is :code:`Infinity` :

>>> Accuracy[1]

    =
:math:`\infty`


>>> Accuracy[A]

    =
:math:`\infty`



For Complex numbers, the accuracy is estimated as (minus) the base-10 log
of the square root of the squares of the errors on the real and complex parts:

>>> z=Complex[3.00``2, 4.00``2];


>>> Accuracy[z] == -Log[10, Sqrt[10^(-2 Accuracy[Re[z]]) + 10^(-2 Accuracy[Im[z]])]]

    =
:math:`\text{True}`



Accuracy of expressions is given by the minimum accuracy of its elements:

>>> Accuracy[F[1, Pi, A]]

    =
:math:`\infty`


>>> Accuracy[F[1.3, Pi, A]]

    =
:math:`15.8406`



:code:`Accuracy`  for the value 0 is a fixed-precision Real number:

>>> 0``2

    =
:math:`0.00`


>>> Accuracy[0.``2]

    =
:math:`2.`



For 0.`, the accuracy satisfies:

>>> Accuracy[0.`] == $MachinePrecision - Log[10, $MinMachineNumber]

    =
:math:`\text{True}`



In compound expressions, the :code:`Accuracy`  is fixed by the number with
the lowest :code:`Accuracy` :

>>> Accuracy[{{1, 1.`},{1.``5, 1.``10}}]

    =
:math:`5.`



See also `:code:`Precision`  </doc/reference-of-built-in-symbols/atomic-elements-of-expressions/representation-of-numbers/precision/>`_.