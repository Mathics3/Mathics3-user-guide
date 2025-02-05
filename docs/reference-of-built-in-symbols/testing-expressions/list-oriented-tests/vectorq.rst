VectorQ
=======

`WMA link <https://reference.wolfram.com/language/ref/VectorQ.html>`_


:code:`VectorQ` [:math:`v`]
    returns :code:`True`  if :math:`v` is a list of elements which are not themselves lists.

:code:`VectorQ` [:math:`v`, :math:`f`]
    returns :code:`True`  if :math:`v` is a vector and :code:`:math:`f`[:math:`x`]`  returns :code:`True`  for each element :math:`x` of :math:`v`.





>>> VectorQ[{a, b, c}]
  = True
