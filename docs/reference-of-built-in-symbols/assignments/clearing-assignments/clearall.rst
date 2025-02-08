ClearAll
========

`WMA link <https://reference.wolfram.com/language/ref/ClearAll.html>`_


:code:`ClearAll` [:math:`symb_1`, :math:`symb_2`, ...]
    clears all values, attributes, messages and options associated with the given symbols.
    The arguments can also be given as strings containing symbol names.





>>> x = 2;


>>> ClearAll[x]


>>> x
    =

:math:`x`


>>> Attributes[r] = {Flat, Orderless};


>>> ClearAll[r]


>>> Attributes[r]
    =

:math:`\left\{\right\}`



:code:`ClearAll`  may not be called for :code:`Protected`  or :code:`Locked`  symbols.

>>> Attributes[lock] = {Locked};


>>> ClearAll[lock]

    ClearAll::locked Symbol lock is locked.


