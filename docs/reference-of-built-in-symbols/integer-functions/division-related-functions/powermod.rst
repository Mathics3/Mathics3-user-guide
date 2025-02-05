PowerMod
========

Modular exponentiaion.
See `https://en.wikipedia.org/wiki/Modular_exponentiation <https://en.wikipedia.org/wiki/Modular_exponentiation>`_.


:code:`PowerMod` [:math:`x`, :math:`y`, :math:`m`]
    computes :math:`x`^:math:`y` modulo :math:`m`.





>>> PowerMod[2, 10000000, 3]
  = 1
>>> PowerMod[3, -2, 10]
  = 9
>>> PowerMod[0, -1, 2]
  = PowerMod[0, -1, 2]
>>> PowerMod[5, 2, 0]
  = PowerMod[5, 2, 0]

:code:`PowerMod`  does not support rational coefficients (roots) yet.