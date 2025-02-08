PowerMod
========

Modular exponentiaion.
See `https://en.wikipedia.org/wiki/Modular_exponentiation <https://en.wikipedia.org/wiki/Modular_exponentiation>`_.


:code:`PowerMod` [:math:`x`, :math:`y`, :math:`m`]
    computes :math:`x`^:math:`y` modulo :math:`m`.





>>> PowerMod[2, 10000000, 3]
    =

:math:`1`


>>> PowerMod[3, -2, 10]
    =

:math:`9`


>>> PowerMod[0, -1, 2]

    PowerMod::ninv 0 is not invertible modulo 2.
    =

:math:`\text{PowerMod}\left[0,-1,2\right]`


>>> PowerMod[5, 2, 0]

    PowerMod::divz The argument 0 should be nonzero.
    =

:math:`\text{PowerMod}\left[5,2,0\right]`



:code:`PowerMod`  does not support rational coefficients (roots) yet.