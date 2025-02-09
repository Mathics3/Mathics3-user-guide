Protected
=========

`WMA link <https://reference.wolfram.com/language/ref/Protected.html>`_


:code:`Protected`
    is an attribute that prevents values on a symbol from
    being modified.





Values of :code:`Protected`  symbols cannot be modified:

>>> Attributes[p] = {Protected};


>>> p = 2;

    Set::wrsym Symbol p is Protected.


>>> f[p] ^= 3;

    UpSet::write Tag p in f[p] is Protected.


>>> Format[p] = "text";

    Set::wrsym Symbol p is Protected.



However, attributes might still be set:

>>> SetAttributes[p, Flat]


>>> Attributes[p]

    =
:math:`\left\{\text{Flat},\text{Protected}\right\}`



Thus, you can easily remove the attribute :code:`Protected` :

>>> Attributes[p] = {};


>>> p = 2

    =
:math:`2`



You can also use :code:`Protect`  or :code:`Unprotect` , resp.

>>> Protect[p]


>>> Attributes[p]

    =
:math:`\left\{\text{Protected}\right\}`


>>> Unprotect[p]



If a symbol is :code:`Protected`  and :code:`Locked` , it can never be changed again:

>>> SetAttributes[p, {Protected, Locked}]


>>> p = 2

    Set::wrsym Symbol p is Protected.

    =
:math:`2`


>>> Unprotect[p]

    ClearAttributes::locked Symbol p is locked.


