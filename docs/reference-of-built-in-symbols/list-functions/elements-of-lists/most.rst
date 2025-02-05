Most
====

`WMA link <https://reference.wolfram.com/language/ref/Most.html>`_


:code:`Most` [:math:`expr`]
    returns :math:`expr` with the last element removed.





:code:`Most[:math:`expr`]`  is equivalent to :code:`:math:`expr`[[;;-2]]` .

>>> Most[{a, b, c}]
  = {a, b}
>>> Most[a + b + c]
  = a + b
>>> Most[x]
  = Most[x]
