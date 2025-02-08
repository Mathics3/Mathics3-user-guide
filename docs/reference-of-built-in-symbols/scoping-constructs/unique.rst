Unique
======

`WMA link <https://reference.wolfram.com/language/ref/Unique.html>`_


:code:`Unique[]`
    generates a new symbol and gives a name of the form :code:`$number` .

:code:`Unique[x]`
    generates a new symbol and gives a name of the form :code:`x$number` .

:code:`Unique[{x, y, ...}]`
    generates a list of new symbols.

:code:`Unique["xxx"]`
    generates a new symbol and gives a name of the form :code:`xxxnumber` .





Create a unique symbol with no particular name:

>>> Unique[]
    =

:math:`\text{\$3}`



Create a unique symbol whose name begins with x:

>>> Unique["x"]
    =

:math:`\text{x4}`


