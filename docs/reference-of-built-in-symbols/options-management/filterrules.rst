FilterRules
===========

`WMA link <https://reference.wolfram.com/language/ref/FilterRules.html>`_


:code:`FilterRules` [:math:`rules`, :math:`pattern`]
    gives those :math:`rules` that have a left side that matches :math:`pattern`.

:code:`FilterRules` [:math:`rules`, {:math:`pattern_1`, :math:`pattern_2`, ...}]
    gives those :math:`rules` that have a left side that match at least one of :math:`pattern_1`, :math:`pattern_2`, ...





>>> FilterRules[{x -> 100, y -> 1000}, x]
    =

:math:`\left\{x->100\right\}`


>>> FilterRules[{x -> 100, y -> 1000, z -> 10000}, {a, b, x, z}]
    =

:math:`\left\{x->100,z->10000\right\}`


