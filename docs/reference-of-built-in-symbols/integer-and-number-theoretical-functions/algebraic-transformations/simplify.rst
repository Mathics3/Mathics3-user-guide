Simplify
========

`SymPy <https://docs.sympy.org/latest/modules/simplify/simplify.html>`_, `WMA <https://reference.wolfram.com/language/ref/Simplify.html>`_


:code:`Simplify` [:math:`expr`]
    simplifies :math:`expr`.

:code:`Simplify` [:math:`expr`, :math:`assump`]
    simplifies :math:`expr` assuming :math:`assump` instead of :code:`$Assumptions` .





>>> Simplify[2*Sin[x]^2 + 2*Cos[x]^2]

    =
:math:`2`


>>> Simplify[x]

    =
:math:`x`


>>> Simplify[f[x]]

    =
:math:`f\left[x\right]`



Simplify over conditional expressions uses :code:`$Assumptions` , or :math:`assump`
to evaluate the condition:

>>> $Assumptions={a <= 0};


>>> Simplify[ConditionalExpression[1, a > 0]]

    =
:math:`\text{Undefined}`



The :math:`assump` option  override :code:`$Assumption` :

>>> Simplify[ConditionalExpression[1, a > 0] ConditionalExpression[1, b > 0], { b > 0 }]

    =
:math:`\text{ConditionalExpression}\left[1,a>0\right]`



On the other hand, :code:`Assumptions`  option does not override :code:`$Assumptions` , but add to them:

>>> Simplify[ConditionalExpression[1, a > 0] ConditionalExpression[1, b > 0], Assumptions -> { b > 0 }]

    =
:math:`\text{ConditionalExpression}\left[1,a>0\right]`



Passing both options overwrites :code:`$Assumptions`  with the union of :math:`assump` the option

>>> Simplify[ConditionalExpression[1, a > 0] ConditionalExpression[1, b > 0], {a>0},Assumptions -> { b > 0 }]

    =
:math:`1`


>>> $Assumptions={};



The option :code:`ComplexityFunction`  allows to control the way in which the evaluator decides if one expression is simpler than another. For example, by default, :code:`Simplify`  tries to avoid expressions involving numbers with many digits:

>>> Simplify[20 Log[2]]

    =
:math:`20 \text{Log}\left[2\right]`



This behaviour can be modified by setting :code:`LeafCount`  as the :code:`ComplexityFunction` :

>>> Simplify[20 Log[2], ComplexityFunction->LeafCount]

    =
:math:`\text{Log}\left[1048576\right]`


