Locked
======

`WMA link <https://reference.wolfram.com/language/ref/Locked.html>`_


:code:`Locked`
    is an attribute that prevents attributes on a symbol from         being modified.





The attributes of :code:`Locked`  symbols cannot be modified:

>>> Attributes[lock] = {Flat, Locked};

>>> SetAttributes[lock, {}]

>>> ClearAttributes[lock, Flat]

>>> Attributes[lock] = {}
  = {}
>>> Attributes[lock]
  = {Flat, Locked}

However, their values might be modified (as long as they are not :code:`Protected`  too):

>>> lock = 3
  = 3
