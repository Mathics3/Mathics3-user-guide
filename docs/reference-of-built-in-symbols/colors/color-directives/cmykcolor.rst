CMYKColor
=========

`CYMYK color model <https://en.wikipedia.org/wiki/CMYK_color_model>`_ (`WMA link <https://reference.wolfram.com/language/ref/CMYKColor.html>`_)


:code:`CMYKColor` [:math:`c`, :math:`m`, :math:`y`, :math:`k`]
    represents a color with the specified cyan, magenta,         yellow and black components.





>>> Graphics[MapIndexed[{CMYKColor @@ #1, Disk[2*#2 ~Join~ {0}]} &, IdentityMatrix[4]], ImageSize->Small]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Colors_CMYKColor_0uda6whi.png
    :align: center



