InputForm
=========

`WMA link <https://reference.wolfram.com/language/ref/InputForm.html>`_


:code:`InputForm` [:math:`expr`]
    displays :math:`expr` in an unambiguous form suitable for input.





>>> InputForm[a + b * c]
  = a + b*c
>>> InputForm["A string"]
  = "A string"
>>> InputForm[f'[x]]
  = Derivative[1][f][x]
>>> InputForm[Derivative[1, 0][f][x]]
  = Derivative[1, 0][f][x]
