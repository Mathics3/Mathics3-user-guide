DiscretePlot
============

`WMA link <https://reference.wolfram.com/language/ref/DiscretePlot.html>`_

:code:`DiscretePlot` [:math:`expr`, {:math:`x`, :math:`n_{max}`}]
    plots :math:`expr` with :math:`x` ranging from 1 to :math:`n_{max}`.

:code:`DiscretePlot` [:math:`expr`, {:math:`x`, :math:`n_{min}`, :math:`n_{max}`}]
    plots :math:`expr` with :math:`x` ranging from :math:`n_{min}` to :math:`n_{max}`.

:code:`DiscretePlot` [:math:`expr`, {:math:`x`, :math:`n_{min}`, :math:`n_{max}`, :math:`dn`}]
    plots :math:`expr` with :math:`x` ranging from :math:`n_{min}` to :math:`n_{max}` usings steps :math:`dn`.

:code:`DiscretePlot` [{:math:`expr_1`, :math:`expr_2`, ...}, ...]
    plots the values of all :math:`expri`.





The number of primes for a number :math:`k`:

>>> DiscretePlot[PrimePi[k], {k, 1, 100}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_DiscretePlot_vc5pr884.png
    :align: center




is about the same as :code:`Sqrt[k] * 2.5` :

>>> DiscretePlot[2.5 Sqrt[k], {k, 100}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_DiscretePlot_4ama7fir.png
    :align: center




Notice in the above that when the starting value, :math:`n_{min}`,  is 1, we can     omit it.

A plot can contain several functions, using the same parameter, here :math:`x`:

>>> DiscretePlot[{Sin[Pi x/20], Cos[Pi x/20]}, {x, 0, 40}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_DiscretePlot_x938ytlg.png
    :align: center




Compare with `:code:`Plot`  </doc/reference-of-built-in-symbols/graphics-and-drawing/plotting-data/plot/>`_.