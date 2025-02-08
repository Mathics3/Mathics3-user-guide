OneIdentity
===========

`WMA link <https://reference.wolfram.com/language/ref/OneIdentity.html>`_


:code:`OneIdentity`
    is an attribute assigned to a symbol, say :math:`f`, indicating that :math:`f[x]`, :math:`f[f[x]]`, etc. are all           equivalent to :math:`x` in pattern matching.





>>> a /. f[x_:0, u_] -> {u}
    =

:math:`a`



Here is how :code:`OneIdentity`  changes the pattern matched above :

>>> SetAttributes[f, OneIdentity]


>>> a /. f[x_:0, u_] -> {u}
    =

:math:`\left\{a\right\}`



However, without a default argument, the pattern does not match:

>>> a /. f[u_] -> {u}
    =

:math:`a`



:code:`OneIdentity`  does not change evaluation:

>>> f[a]
    =

:math:`f\left[a\right]`


