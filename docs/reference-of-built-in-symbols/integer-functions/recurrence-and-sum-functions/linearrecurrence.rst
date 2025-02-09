LinearRecurrence
================

`Linear recurrence with constant coefficients <https://en.wikipedia.org/wiki/Linear_recurrence_with_constant_coefficients>`_, `WMA link <https://reference.wolfram.com/language/ref/LinearRecurrence.html>`_


:code:`LinearRecurrence` [:math:`ker`, :math:`init`, :math:`n`]
    computes :math:`n` terms of the linear recurrence with kernel :math:`ker` and initial values :math:`init`.

:code:`LinearRecurrence` [:math:`ker`, :math:`init`, {:math:`n`}]
    computes the :math:`n`-th term.

:code:`LinearRecurrence` [:math:`ker`, :math:`init`, {:math:`n_{min}`, :math:`n_{max}`}]
    computes :math:`n` terms of the linear recurrence with kernel :math:`ker` and initial values :math:`init`.





Generate first 10 items of the Fibonacci Sequence, :code:`F` [0]=1, :code:`F` [1]=1:

>>> LinearRecurrence[{1, 1}, {1, 1}, 10]

    =
:math:`\left\{1,1,2,3,5,8,13,21,34,55\right\}`



Extract the 3rd to 5th elements:

>>> LinearRecurrence[{1, 1}, {1, 1}, {3, 5}]

    =
:math:`\left\{2,3,5\right\}`



Now just the 6th element:

>>> LinearRecurrence[{1, 1}, {1, 1}, {6}]

    =
:math:`8`



See also `Fibonacci </doc/reference-of-built-in-symbols/integer-functions/recurrence-and-sum-functions/fibonacci>`_.