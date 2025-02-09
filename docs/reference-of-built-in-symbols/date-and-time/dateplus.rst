DatePlus
========

`WMA link <https://reference.wolfram.com/language/ref/DatePlus.html>`_


:code:`DatePlus` [:math:`date`, :math:`n`]
    finds the date :math:`n` days after :math:`date`.

:code:`DatePlus` [:math:`date`, {:math:`n`, ":math:`unit`"}]
    finds the date :math:`n` units after :math:`date`.

:code:`DatePlus` [:math:`date`, {{:math:`n_1`, ":math:`unit_1`"}, {:math:`n_2`, ":math:`unit_2`"}, ...}]
    finds the date which is :math:`n_i` specified units after :math:`date`.

:code:`DatePlus` [:math:`n`]
    finds the date :math:`n` days after the current date.

:code:`DatePlus` [:math:`offset`]
    finds the date which is offset from the current date.





Add 73 days to Feb 5, 2010:

>>> DatePlus[{2010, 2, 5}, 73]

    =
:math:`\left\{2010,4,19\right\}`



Add 8 weeks and 1 day to March 16, 1999:

>>> DatePlus[{2010, 2, 5}, {{8, "Week"}, {1, "Day"}}]

    =
:math:`\left\{2010,4,3\right\}`


