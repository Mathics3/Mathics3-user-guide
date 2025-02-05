FresnelS
========

`Fresnel integral <https://en.wikipedia.org/wiki/Fresnel_integral>`_ (`mpmath <https://mpmath.org/doc/current/functions/expintegrals.html#mpmath.fresnels>`_,    `WMA <https://reference.wolfram.com/language/ref/FresnelS.html>`_)


:code:`FresnelS` [:math:`z`]
    is the Fresnel S integral :math:`S`(:math:`z`).





>>> FresnelS[{0, Infinity}]
  = {0, 1 / 2}
>>> Integrate[Sin[x^2 Pi/2], {x, 0, z}]
  = FresnelS[z]
