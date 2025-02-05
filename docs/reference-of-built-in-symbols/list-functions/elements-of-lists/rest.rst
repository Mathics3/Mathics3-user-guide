Rest
====

`WMA link <https://reference.wolfram.com/language/ref/Rest.html>`_


:code:`Rest` [:math:`expr`]
    returns :math:`expr` with the first element removed.





:code:`Rest[:math:`expr`]`  is equivalent to :code:`:math:`expr`[[2;;]]` .

>>> Rest[{a, b, c}]
  = {b, c}
>>> Rest[a + b + c]
  = b + c
>>> Rest[x]
  = Rest[x]
>>> Rest[{}]
  = Rest[{}]
