HypergeometricU
===============

`Confluent hypergeometric function <https://en.wikipedia.org/wiki/Confluent_hypergeometric_function>`_ (`mpmath <https://mpmath.org/doc/current/functions/bessel.html#mpmath.hyperu>`_, `WMA <https://reference.wolfram.com/language/ref/HypergeometricU.html>`_)

:code:`HypergeometricU` [:math:`a`, :math:`b`, :math:`z`]
    returns :math:`U(a, b, z)`.





>>> HypergeometricU[3, 2, 1.]

    =
:math:`0.105479`



Plot :code:`U` [3, 2, x] from 0 to 2 in steps of 0.5:

>>> Plot[HypergeometricU[3, 2, x], {x, 0.5, 2}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Special_Functions_HypergeometricU_p_0agdua.png
    :align: center




We handle this special case:

>>> HypergeometricU[0, c, z]

    =
:math:`1`


