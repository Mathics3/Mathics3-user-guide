Infinity
========

`
Infinity <https://en.wikipedia.org/wiki/Infinity>`_ (`SymPy <https://docs.sympy.org/latest/modules/core.html#sympy.core.numbers.Infinity>`_, `WMA <https://reference.wolfram.com/language/ref/Infinity.html>`_)


:code:`Infinity`
    a symbol that represents an infinite real quantity.





:code:`Infinity`  sometimes appears as the result of a calculation:

>>> Precision[1]
    =

:math:`\infty`



But :code:`Infinity`  it often used as a value in expressions:

>>> 1 / Infinity
    =

:math:`0`


>>> Infinity + 100
    =

:math:`\infty`



:code:`Infinity`  often appears in sum and limit calculations:

>>> Sum[1/x^2, {x, 1, Infinity}]
    =

:math:`\frac{ \pi ^2}{6}`


>>> Limit[1/x, x->0]
    =

:math:`-\infty`



However, :code:`Infinity`  a shorthand for :code:`DirectedInfinity[1]` :

>>> FullForm[Infinity]
    =

:math:`\text{DirectedInfinity}\left[1\right]`



See also `:code:`DirectedInfinity`  </doc/reference-of-built-in-symbols/mathematical-functions/directedinfinity/>`_.