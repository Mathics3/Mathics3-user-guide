PowerExpand
===========

`WMA link <https://reference.wolfram.com/language/ref/PowerExpand.html>`_


:code:`PowerExpand` [:math:`expr`]
    expands out powers of the form :math:`(x^y)^z` and :math:`(x y)^z` in :math:`expr`.





>>> PowerExpand[(a ^ b) ^ c]
  = a ^ (b c)
>>> PowerExpand[(a * b) ^ c]
  = a ^ c b ^ c

:code:`PowerExpand`  is not correct without certain assumptions:

>>> PowerExpand[(x ^ 2) ^ (1/2)]
  = x
