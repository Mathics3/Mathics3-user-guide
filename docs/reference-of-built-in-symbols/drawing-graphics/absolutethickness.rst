AbsoluteThickness
=================

`WMA link <https://reference.wolfram.com/language/ref/AbsoluteThickness.html>`_


:code:`AbsoluteThickness` [:math:`p`]
    sets the line thickness for subsequent graphics primitives to :math:`p`           points.





>>> Graphics[Table[{AbsoluteThickness[t], Line[{{20 t, 10}, {20 t, 80}}], Text[ToString[t]<>"pt", {20 t, 0}]}, {t, 0, 10}]]
  = -Graphics-
