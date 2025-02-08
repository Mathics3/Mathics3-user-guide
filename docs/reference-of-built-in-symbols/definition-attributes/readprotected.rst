ReadProtected
=============

`WMA link <https://reference.wolfram.com/language/ref/ReadProtected.html>`_


:code:`ReadProtected`
    is an attribute that prevents values on a symbol from           being read.





Values associated with :code:`ReadProtected`  symbols cannot be seen in     :code:`Definition` :

>>> ClearAll[p]


>>> p = 3;


>>> Definition[p]
    =

:math:`\begin{array}{l} p=3\end{array}`


>>> SetAttributes[p, ReadProtected]


>>> Definition[p]
    =

:math:`\begin{array}{l} \text{Attributes}\left[p\right]=\left\{\text{ReadProtected}\right\}\end{array}`


