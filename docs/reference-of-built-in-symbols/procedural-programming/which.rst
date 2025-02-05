Which
=====

`WMA link <https://reference.wolfram.com/language/ref/Which.html>`_


:code:`Which` [:math:`cond_1`, :math:`expr_1`, :math:`cond_2`, :math:`expr_2`, ...]
    yields :math:`expr_1` if :math:`cond_1` evaluates to :code:`True` , :math:`expr_2` if :math:`cond_2`           evaluates to :code:`True` , etc.





>>> n = 5;

>>> Which[n == 3, x, n == 5, y]
  = y
>>> f[x_] := Which[x < 0, -x, x == 0, 0, x > 0, x]

>>> f[-3]
  = 3
>>> Clear[f]


If no test yields :code:`True` , :code:`Which`  returns :code:`Null` :

>>> Which[False, a]


If a test does not evaluate to :code:`True`  or :code:`False` , evaluation stops
and a :code:`Which`  expression containing the remaining cases is
returned:

>>> Which[False, a, x, b, True, c]
  = Which[x, b, True, c]

:code:`Which`  must be called with an even number of arguments:

>>> Which[a, b, c]
  = Which[a, b, c]
