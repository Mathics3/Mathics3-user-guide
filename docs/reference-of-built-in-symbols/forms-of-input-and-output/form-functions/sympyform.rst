SympyForm
=========


:code:`SympyForm` [:math:`expr`]
    returns an Sympy :math:`expr` in Python. Sympy is used internally
    to implement a number of Mathics functions, like Simplify.





>>> SympyForm[Pi^2]
  = pi**2
>>> E^2 + 3E // SympyForm
  = exp(2) + 3*E
