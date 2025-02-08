Hash
====

`Hash function <https://en.wikipedia.org/wiki/Hash_function>`_     (`WMA link <https://reference.wolfram.com/language/ref/Hash.html>`_)


:code:`Hash` [:math:`expr`]
    returns an integer hash for the given :math:`expr`.

:code:`Hash` [:math:`expr`, :math:`type`]
    returns an integer hash of the specified :math:`type` for the given :math:`expr`.

    The types supported are "MD5", "Adler32", "CRC32", "SHA", "SHA224",           "SHA256", "SHA384", and "SHA512".

:code:`Hash` [:math:`expr`, :math:`type`, :math:`format`]
    Returns the hash in the specified format.





>>> Hash["The Adventures of Huckleberry Finn"]
    =

:math:`213425047836523694663619736686226550816`


>>> Hash["The Adventures of Huckleberry Finn", "SHA256"]
    =

:math:`95092649594590384288057183408609254918934351811669818342876362244564858646638`


>>> Hash[1/3]
    =

:math:`56073172797010645108327809727054836008`


>>> Hash[{a, b, {c, {d, e, f}}}]
    =

:math:`135682164776235407777080772547528225284`


>>> Hash[SomeHead[3.1415]]
    =

:math:`47205238268993602951487675588386522878`


>>> Hash[{a, b, c}, "xyzstr"]
    =

:math:`\text{Hash}\left[\left\{a,b,c\right\},\text{xyzstr},\text{Integer}\right]`


