FirstPosition
=============

`WMA link <https://reference.wolfram.com/language/ref/FirstPosition.html>`_


:code:`FirstPosition` [:math:`expr`, :math:`pattern`]
    gives the position of the first element in :math:`expr` that matches :math:`pattern`, or Missing["NotFound"] if no such element is found.

:code:`FirstPosition` [:math:`expr`, :math:`pattern`, :math:`default`]
    gives default if no element matching :math:`pattern` is found.

:code:`FirstPosition` [:math:`expr`, :math:`pattern`, :math:`default`, :math:`levelspec`]
    finds only objects that appear on levels specified by :math:`levelspec`.





>>> FirstPosition[{a, b, a, a, b, c, b}, b]

    =
:math:`\left\{2\right\}`


>>> FirstPosition[{{a, a, b}, {b, a, a}, {a, b, a}}, b]

    =
:math:`\left\{1,3\right\}`


>>> FirstPosition[{x, y, z}, b]

    =
:math:`\text{Missing}\left[\text{NotFound}\right]`



Find the first position at which x^2 to appears:

>>> FirstPosition[{1 + x^2, 5, x^4, a + (1 + x^2)^2}, x^2]

    =
:math:`\left\{1,2\right\}`


