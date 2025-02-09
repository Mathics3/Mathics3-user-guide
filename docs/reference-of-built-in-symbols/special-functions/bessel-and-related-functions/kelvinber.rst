KelvinBer
=========

`Kelvin function ber <https://en.wikipedia.org/wiki/Kelvin_functions#ber(x)>`_ (`mpmath <https://mpmath.org/doc/current/functions/bessel.html#ber>`_, `WMA <https://reference.wolfram.com/language/ref/KelvinBer.html>`_)

:code:`KelvinBer` [:math:`z`]
    returns the Kelvin function :math:`ber(z)`.

:code:`KelvinBer` [:math:`n`, :math:`z`]
    returns the Kelvin function :math:`ber_n(z)`.





>>> KelvinBer[0.5]

    =
:math:`0.999023`


>>> KelvinBer[1.5 + I]

    =
:math:`1.1162-0.117944 I`


>>> KelvinBer[0.5, 0.25]

    =
:math:`0.148824`


>>> Plot[KelvinBer[x], {x, 0, 10}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Special_Functions_KelvinBer_9bqz6cbk.png
    :align: center



