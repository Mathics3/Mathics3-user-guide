TimeConstrained
===============

`WMA link <https://reference.wolfram.com/language/ref/TimeConstrained.html>`_


:code:`TimeConstrained` [:math:`expr`, :math:`t`]
    :code:`evaluates :math:`expr`, stopping after :math:`t` seconds.`

:code:`TimeConstrained` [:math:`expr`, :math:`t`, :math:`failexpr`]
    :code:`returns :math:`failexpr` if the time constraint is not met.`





Possible issues: for certain time-consuming functions (like simplify)
which are based on sympy or other libraries, it is possible that
the evaluation continues after the timeout. However, at the end of the evaluation, the function will return :code:`$Aborted`  and the results will not affect
the state of the Mathics3 kernel.