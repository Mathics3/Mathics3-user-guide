PolyLog
=======

`Polylogarithm <https://en.wikipedia.org/wiki/Polylogarithm>`_ (`WMA <https://reference.wolfram.com/language/ref/PolyLog.html>`_)


:code:`PolyLog` [:math:`n`, :math:`z`]
    returns the polylogarithm function :math:`Li_n(z)`.





>>> PolyLog[s, 1]

    =
:math:`\text{Zeta}\left[s\right]`


>>> PolyLog[-7, I] //Chop

    =
:math:`136.`



Dilogarithm function :math:`Li_2(x)`:

>>> Plot[PolyLog[2,x], {x, -20, 1}]
    = -Graphics-`

