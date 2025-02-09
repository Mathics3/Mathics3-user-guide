Precedence
==========

on, logic, comparison, datentime, attributes and binary)


:code:`Precedence` [:math:`op`]
    returns the precedence of the built-in operator :math:`op`.





>>> Precedence[Plus]

    =
:math:`310.`


>>> Precedence[Plus] < Precedence[Times]

    =
:math:`\text{True}`



Unknown symbols have precedence 670:

>>> Precedence[f]

    =
:math:`670.`



Other expressions have precedence 1000:

>>> Precedence[a + b]

    =
:math:`1000.`


