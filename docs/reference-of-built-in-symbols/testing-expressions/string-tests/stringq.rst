StringQ
=======

`WMA link <https://reference.wolfram.com/language/ref/StringQ.html>`_

:code:`StringQ` [:math:`expr`]
    returns :code:`True`  if :math:`expr` is a :code:`String` , or :code:`False`  otherwise.





>>> StringQ["abc"]
  = True
>>> StringQ[1.5]
  = False
>>> Select[{"12", 1, 3, 5, "yz", x, y}, StringQ]
  = {12, yz}
