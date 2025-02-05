MatrixQ
=======

`WMA link <https://reference.wolfram.com/language/ref/MatrixQ.html>`_


:code:`MatrixQ` [:math:`m`]
    gives :code:`True`  if :math:`m` is a list of equal-length lists.

:code:`MatrixQ` [:math:`m`, :math:`f`]
    gives :code:`True`  only if :code:`:math:`f`[:math:`x`]`  returns :code:`True`  for when applied to          element :math:`x` of the matrix :math:`m`.





>>> MatrixQ[{{1, 3}, {4.0, 3/2}}, NumberQ]
  = True

These are not matrices:

>>> MatrixQ[{{1}, {1, 2}}] (* first row should have length two *)
  = False
>>> MatrixQ[Array[a, {1, 1, 2}]]
  = False

Supply a test function parameter to generalize and specialize:

>>> MatrixQ[{{1, 2}, {3, 4 + 5}}, Positive]
  = True
>>> MatrixQ[{{1, 2 I}, {3, 4 + 5}}, Positive]
  = False
