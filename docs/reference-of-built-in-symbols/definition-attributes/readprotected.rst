ReadProtected
=============

`WMA link <https://reference.wolfram.com/language/ref/ReadProtected.html>`_


:code:`ReadProtected`
    is an attribute that prevents values on a symbol from           being read.





Values associated with :code:`ReadProtected`  symbols cannot be seen in     :code:`Definition` :

>>> ClearAll[p]

>>> p = 3;

>>> Definition[p]
  = p = 3
>>> SetAttributes[p, ReadProtected]

>>> Definition[p]
  = Attributes[p] = {ReadProtected}
