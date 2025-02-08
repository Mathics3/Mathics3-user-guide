Locked
======

`WMA link <https://reference.wolfram.com/language/ref/Locked.html>`_


:code:`Locked`
    is an attribute that prevents attributes on a symbol from         being modified.





The attributes of :code:`Locked`  symbols cannot be modified:

>>> Attributes[lock] = {Flat, Locked};


>>> SetAttributes[lock, {}]

    SetAttributes::locked Symbol lock is locked.


>>> ClearAttributes[lock, Flat]

    ClearAttributes::locked Symbol lock is locked.


>>> Attributes[lock] = {}

    Attributes::locked Symbol lock is locked.
    =

:math:`\left\{\right\}`


>>> Attributes[lock]
    =

:math:`\left\{\text{Flat},\text{Locked}\right\}`



However, their values might be modified (as long as they are not :code:`Protected`  too):

>>> lock = 3
    =

:math:`3`


