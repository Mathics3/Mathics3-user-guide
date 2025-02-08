Beta
====

`Euler beta function <https://en.wikipedia.org/wiki/Beta_function>`_ (`SymPy <https://docs.sympy.org/latest/modules/functions/special.html#sympy.functions.special.beta_functions.beta>`_, `WMA <https://reference.wolfram.com/language/ref/Beta.html>`_)


:code:`Beta` [:math:`a`, :math:`b`]
    is the Euler's Beta function.

:code:`Beta` [:math:`z`, :math:`a`, :math:`b`]
    gives the incomplete Beta function.





The Beta function satisfies the property
Beta[x, y] = Integrate[t^(x-1)(1-t)^(y-1),{t,0,1}] = Gamma[a] Gamma[b] / Gamma[a + b]

>>> Beta[2, 3]
    =

:math:`\frac{1}{12}`


>>> 12* Beta[1., 2, 3]
    =

:math:`1.`


