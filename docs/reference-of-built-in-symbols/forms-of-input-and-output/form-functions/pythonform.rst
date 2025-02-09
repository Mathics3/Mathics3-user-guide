PythonForm
==========


:code:`PythonForm` [:math:`expr`]
    returns an approximate equivalent of :math:`expr` in Python, when that is possible. We assume
    that Python has SymPy imported. No explicit import will be include in the result.





>>> PythonForm[Infinity]

    =
:math:`\text{math.inf}`


>>> PythonForm[Pi]

    =
:math:`\text{sympy.pi}`


>>> E // PythonForm

    =
:math:`\text{sympy.E}`


>>> {1, 2, 3} // PythonForm

    =
:math:`\text{[1, 2, 3]}`


