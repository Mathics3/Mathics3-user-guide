Protected
=========

`WMA link <https://reference.wolfram.com/language/ref/Protected.html>`_


:code:`Protected`
    is an attribute that prevents values on a symbol from
    being modified.





Values of :code:`Protected`  symbols cannot be modified:

>>> Attributes[p] = {Protected};

>>> p = 2;

>>> f[p] ^= 3;

>>> Format[p] = "text";


However, attributes might still be set:

>>> SetAttributes[p, Flat]

>>> Attributes[p]
  = {Flat, Protected}

Thus, you can easily remove the attribute :code:`Protected` :

>>> Attributes[p] = {};

>>> p = 2
  = 2

You can also use :code:`Protect`  or :code:`Unprotect` , resp.

>>> Protect[p]

>>> Attributes[p]
  = {Protected}
>>> Unprotect[p]


If a symbol is :code:`Protected`  and :code:`Locked` , it can never be changed again:

>>> SetAttributes[p, {Protected, Locked}]

>>> p = 2
  = 2
>>> Unprotect[p]

