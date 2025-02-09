AngleVector
===========

`WMA link <https://reference.wolfram.com/language/ref/AngleVector.html>`_


:code:`AngleVector` [:math:`\phi`]
    returns the point at angle :math:`\phi` on the unit circle.

:code:`AngleVector` [{:math:`r`, :math:`\phi`}]
    returns the point at angle :math:`\phi` on a circle of radius :math:`r`.

:code:`AngleVector` [{:math:`x`, :math:`y`}, :math:`\phi`]
    returns the point at angle :math:`\phi` on a circle of radius 1 centered at {:math:`x`, :math:`y`}.

:code:`AngleVector` [{:math:`x`, :math:`y`}, {:math:`r`, :math:`\phi`}]
    returns point at angle :math:`\phi` on a circle of radius :math:`r` centered at {:math:`x`, :math:`y`}.





>>> AngleVector[90 Degree]

    =
:math:`\left\{0,1\right\}`


>>> AngleVector[{1, 10}, a]

    =
:math:`\left\{1+\text{Cos}\left[a\right],10+\text{Sin}\left[a\right]\right\}`


