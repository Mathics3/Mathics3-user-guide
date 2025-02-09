SympyForm
=========


:code:`SympyForm` [:math:`expr`]
    returns an Sympy :math:`expr` in Python. Sympy is used internally
    to implement a number of Mathics functions, like Simplify.





>>> SympyForm[Pi^2]

    =
:math:`\text{pi**2}`


>>> E^2 + 3E // SympyForm

    =
:math:`\text{exp(2) + 3*E}`


