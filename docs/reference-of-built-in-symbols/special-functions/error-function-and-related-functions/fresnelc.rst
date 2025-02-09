FresnelC
========

`Fresnel integral <https://en.wikipedia.org/wiki/Fresnel_integral>`_ (`mpmath <https://mpmath.org/doc/current/functions/expintegrals.html?mpmath.fresnelc>`_,    `WMA <https://reference.wolfram.com/language/ref/FresnelC.html>`_)

:code:`FresnelC` [:math:`z`]
    is the Fresnel C integral :math:`C`(:math:`z`).





>>> FresnelC[{0, Infinity}]

    =
:math:`\left\{0,\frac{1}{2}\right\}`


>>> Integrate[Cos[x^2 Pi/2], {x, 0, z}]

    =
:math:`\text{FresnelC}\left[z\right]`


