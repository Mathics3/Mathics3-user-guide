Power
=====

`Exponentiation <https://en.wikipedia.org/wiki/Exponentiation>`_ (`SymPy <https://docs.sympy.org/latest/modules/core.html#sympy.core.power.Pow>`_, `WMA <https://reference.wolfram.com/language/ref/Power.html>`_)


:code:`Power` [:math:`a`, :math:`b`]
    same as

:math:`a` :code:`^`  :math:`b`
    represents :math:`a` raised to the power of :math:`b`.





>>> 4 ^ (1/2)
    =

:math:`2`


>>> 4 ^ (1/3)
    =

:math:`2^{\frac{2}{3}}`


>>> 3^123
    =

:math:`48519278097689642681155855396759336072749841943521979872827`


>>> (y ^ 2) ^ (1/2)
    =

:math:`\sqrt{y^2}`


>>> (y ^ 2) ^ 3
    =

:math:`y^6`


>>> Plot[Evaluate[Table[x^y, {y, 1, 5}]], {x, -1.5, 1.5}, AspectRatio -> 1]
    =

.. image:: tmppomcj2ex.png
    :align: center




Use a decimal point to force numeric evaluation:

>>> 4.0 ^ (1/3)
    =

:math:`1.5874`



:code:`Power`  has default value 1 for its second argument:

>>> DefaultValues[Power]
    =

:math:`\left\{\text{HoldPattern}\left[\text{Default}\left[\text{Power},2\right]\right]\text{:>}1\right\}`


>>> a /. x_ ^ n_. :> {x, n}
    =

:math:`\left\{a,1\right\}`



:code:`Power`  can be used with complex numbers:

>>> (1.5 + 1.0 I) ^ 3.5
    =

:math:`-3.68294+6.95139 I`


>>> (1.5 + 1.0 I) ^ (3.5 + 1.5 I)
    =

:math:`-3.19182+0.645659 I`


