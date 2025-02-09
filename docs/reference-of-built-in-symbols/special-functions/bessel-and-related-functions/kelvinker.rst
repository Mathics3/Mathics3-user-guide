KelvinKer
=========

`Kelvin function ker <https://en.wikipedia.org/wiki/Kelvin_functions#ker(x)>`_ (`mpmath <https://mpmath.org/doc/current/functions/bessel.html#ker>`_, `WMA <https://reference.wolfram.com/language/ref/KelvinKer.html>`_)


:code:`KelvinKer` [:math:`z`]
    returns the Kelvin function :math:`ker(z)`.

:code:`KelvinKer` [:math:`n`, :math:`z`]
    returns the Kelvin function :math:`ker_n(z)`.





>>> KelvinKer[0.5]

    =
:math:`0.855906`


>>> KelvinKer[1.5 + I]

    =
:math:`-0.167162-0.184404 I`


>>> KelvinKer[0.5, 0.25]

    =
:math:`0.450023`


>>> Plot[KelvinKer[x], {x, 0, 10}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Special_Functions_KelvinKer_62fz03jh.png
    :align: center



