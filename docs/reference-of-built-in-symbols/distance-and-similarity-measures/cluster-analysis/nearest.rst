Nearest
=======

`WMA link <https://reference.wolfram.com/language/ref/Nearest.html>`_


:code:`Nearest` [:math:`list`, :math:`x`]
    returns the one item in :math:`list` that is nearest to :math:`x`.

:code:`Nearest` [:math:`list`, :math:`x`, :math:`n`]
    returns the :math:`n` nearest items.

:code:`Nearest` [:math:`list`, :math:`x`, {:math:`n`, :math:`r`}]
    returns up to :math:`n` nearest items that are not farther from :math:`x` than :math:`r`.

:code:`Nearest` [{:math:`p_1` -> :math:`q_1`, :math:`p_2` -> :math:`q_2`, ...}, :math:`x`]
    returns :math:`q_1`, :math:`q_2`, ... but measures the distances using :math:`p_1`, :math:`p_2`, ...

:code:`Nearest` [{:math:`p_1`, :math:`p_2`, ...} -> {:math:`q_1`, :math:`q_2`, ...}, :math:`x`]
    returns :math:`q_1`, :math:`q_2`, ... but measures the distances using :math:`p_1`, :math:`p_2`, ...





>>> Nearest[{5, 2.5, 10, 11, 15, 8.5, 14}, 12]

    =
:math:`\left\{11\right\}`



Return all items within a distance of 5:

>>> Nearest[{5, 2.5, 10, 11, 15, 8.5, 14}, 12, {All, 5}]

    =
:math:`\left\{11,10,14\right\}`


>>> Nearest[{Blue -> "blue", White -> "white", Red -> "red", Green -> "green"}, {Orange, Gray}]

    =
:math:`\left\{\left\{\text{red}\right\},\left\{\text{white}\right\}\right\}`


>>> Nearest[{{0, 1}, {1, 2}, {2, 3}} -> {a, b, c}, {1.1, 2}]

    =
:math:`\left\{b\right\}`


