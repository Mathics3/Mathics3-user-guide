Divide
======

`Division <https://en.wikipedia.org/wiki/Division_(mathematics)>`_ (`WMA link <https://reference.wolfram.com/language/ref/Divide.html>`_)


:code:`Divide` [:math:`a`, :math:`b`]
    same as

:math:`a` :code:`/`  :math:`b`
    represents the division of :math:`a` by :math:`b`.





>>> 30 / 5

    =
:math:`6`


>>> 1 / 8

    =
:math:`\frac{1}{8}`


>>> Pi / 4

    =
:math:`\frac{ \pi }{4}`



Use :code:`N`  or a decimal point to force numeric evaluation:

>>> Pi / 4.0

    =
:math:`0.785398`


>>> 1 / 8

    =
:math:`\frac{1}{8}`


>>> N[%]

    =
:math:`0.125`



Nested divisions:

>>> a / b / c

    =
:math:`\frac{a}{b c}`


>>> a / (b / c)

    =
:math:`\frac{a c}{b}`


>>> a / b / (c / (d / e))

    =
:math:`\frac{a d}{b c e}`


>>> a / (b ^ 2 * c ^ 3 / e)

    =
:math:`\frac{a e}{b^2 c^3}`


