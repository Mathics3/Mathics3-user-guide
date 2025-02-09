KelvinBei
=========

`Kelvin function bei <https://en.wikipedia.org/wiki/Kelvin_functions#bei(x)>`_ (`mpmath <https://mpmath.org/doc/current/functions/bessel.html#bei>`_, `WMA <https://reference.wolfram.com/language/ref/KelvinBei.html>`_)


:code:`KelvinBei` [:math:`z`]
    returns the Kelvin function :math:`bei(z)`.

:code:`KelvinBei` [:math:`n`, :math:`z`]
    returns the Kelvin function :math:`bei_n(z)`.





>>> KelvinBei[0.5]

    =
:math:`0.0624932`


>>> KelvinBei[1.5 + I]

    =
:math:`0.326323+0.755606 I`


>>> KelvinBei[0.5, 0.25]

    =
:math:`0.370153`


>>> Plot[KelvinBei[x], {x, 0, 10}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Special_Functions_KelvinBei_9jcg_h9r.png
    :align: center



