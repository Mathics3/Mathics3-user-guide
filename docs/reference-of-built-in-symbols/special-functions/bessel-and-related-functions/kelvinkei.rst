KelvinKei
=========

`Kelvin function kei <https://en.wikipedia.org/wiki/Kelvin_functions#kei(x)>`_ (`mpmath <https://mpmath.org/doc/current/functions/bessel.html#kei>`_, `WMA <https://reference.wolfram.com/language/ref/KelvinKei.html>`_)


:code:`KelvinKei` [:math:`z`]
    returns the Kelvin function :math:`kei(z)`.

:code:`KelvinKei` [:math:`n`, :math:`z`]
    returns the Kelvin function :math:`kei_n(z)`.





>>> KelvinKei[0.5]

    =
:math:`-0.671582`


>>> KelvinKei[1.5 + I]

    =
:math:`-0.248994+0.303326 I`


>>> KelvinKei[0.5, 0.25]

    =
:math:`-2.0517`


>>> Plot[KelvinKei[x], {x, 0, 10}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Special_Functions_KelvinKei_33b_akn2.png
    :align: center



