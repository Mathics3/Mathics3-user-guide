OutputForm
==========

`WMA link <https://reference.wolfram.com/language/ref/OutputForm.html>`_


:code:`OutputForm` [:math:`expr`]
    displays :math:`expr` in a plain-text form.





>>> OutputForm[f'[x]]
  = f'[x]
>>> OutputForm[Derivative[1, 0][f][x]]
  = Derivative[1, 0][f][x]

:code:`OutputForm`  is used by default:

>>> OutputForm[{"A string", a + b}]
  = {A string, a + b}
>>> {"A string", a + b}
  = {A string, a + b}
>>> OutputForm[Graphics[Rectangle[]]]
  = -Graphics-
