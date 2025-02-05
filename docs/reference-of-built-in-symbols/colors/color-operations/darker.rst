Darker
======

`WMA link <https://reference.wolfram.com/language/ref/Darker.html>`_


:code:`Darker` [:math:`c`, :math:`f`]
    is equivalent to :code:`Blend` [{:math:`c`, :code:`Black` }, :math:`f`].

:code:`Darker` [:math:`c`]
    is equivalent to :code:`Darker` [:math:`c`, :code:`1/3` ].





>>> Graphics[{Darker[Red], Disk[]}]
  = -Graphics-
>>> Graphics3D[{Darker[Green], Sphere[]}]
  = -Graphics3D-
>>> Graphics[Table[{Darker[Yellow, x], Disk[{12x, 0}]}, {x, 0, 1, 1/6}]]
  = -Graphics-
