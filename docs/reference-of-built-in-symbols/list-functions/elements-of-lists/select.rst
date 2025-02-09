Select
======

`WMA link <https://reference.wolfram.com/language/ref/Select.html>`_


:code:`Select` [{:math:`e_1`, :math:`e_2`, ...}, :math:`crit`]
    returns a list of the elements :math:`ei` for which :math:`crit`[:math:`ei`] is :code:`True` .

:code:`Select` [{:math:`e_1`, :math:`e_2`, ...}, :math:`crit`, n]
    returns a list of the first :math:`n` elements :math:`ei` for which :math:`crit`[:math:`ei`] is :code:`True` .





Get a list of even numbers up to 10:

>>> Select[Range[10], EvenQ]

    =
:math:`\left\{2,4,6,8,10\right\}`



Find numbers that are greater than zero in a list:

>>> Select[{-3, 0, 10, 3, a}, #>0&]

    =
:math:`\left\{10,3\right\}`



Find the first number that is list greater than zero in a list:

>>> Select[{-3, 0, 10, 3, a}, #>0&, 1]

    =
:math:`\left\{10\right\}`



:code:`Select`  works on an expression with any head:

>>> Select[f[a, 2, 3], NumberQ]

    =
:math:`f\left[2,3\right]`


