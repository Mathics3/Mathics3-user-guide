LogPlot
=======

`Semi-log plot <https://en.wikipedia.org/wiki/Semi-log_plot>`_     (`WMA link <https://reference.wolfram.com/language/ref/LogPlot.html>`_)

:code:`LogPlot` [:math:`f`, {:math:`x`, :math:`x_{min}`, :math:`x_{max}`}]
    log plots :math:`f` with :math:`x` ranging from :math:`x_{min}` to :math:`x_{max}`.

:code:`Plot` [{:math:`f_1`, :math:`f_2`, ...}, {:math:`x`, :math:`x_{min}`, :math:`x_{max}`}]
    log plots several functions :math:`f_1`, :math:`f_2`, ...





>>> LogPlot[x^x, {x, 1, 5}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_LogPlot_0e_yhofv.png
    :align: center



>>> LogPlot[{x^x, Exp[x], x!}, {x, 1, 5}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_LogPlot_tg44shkq.png
    :align: center



