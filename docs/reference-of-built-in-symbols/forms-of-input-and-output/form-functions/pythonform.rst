PythonForm
==========


:code:`PythonForm` [:math:`expr`]
    returns an approximate equivalent of :math:`expr` in Python, when that is possible. We assume
    that Python has SymPy imported. No explicit import will be include in the result.





>>> PythonForm[Infinity]
  = math.inf
>>> PythonForm[Pi]
  = sympy.pi
>>> E // PythonForm
  = sympy.E
>>> {1, 2, 3} // PythonForm
  = [1, 2, 3]
