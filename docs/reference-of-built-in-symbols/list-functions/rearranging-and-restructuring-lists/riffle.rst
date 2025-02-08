Riffle
======

`WMA link <https://reference.wolfram.com/language/ref/Riffle.html>`_


:code:`Riffle` [:math:`list`, :math:`x`]
    inserts a copy of :math:`x` between each element of :math:`list`.

:code:`Riffle` [{:math:`a_1`, :math:`a_2`, ...}, {:math:`b_1`, :math:`b_2`, ...}]
    interelements the elements of both lists, returning :code:`{:math:`a_1`, :math:`b_1`, :math:`a_2`, :math:`b_2`, ...}` .





>>> Riffle[{a, b, c}, x]
    =

:math:`\left\{a,x,b,x,c\right\}`


>>> Riffle[{a, b, c}, {x, y, z}]
    =

:math:`\left\{a,x,b,y,c,z\right\}`


>>> Riffle[{a, b, c, d, e, f}, {x, y, z}]
    =

:math:`\left\{a,x,b,y,c,z,d,x,e,y,f\right\}`


