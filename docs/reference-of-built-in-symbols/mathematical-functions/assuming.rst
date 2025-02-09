Assuming
========

`WMA link <https://reference.wolfram.com/language/ref/Assuming.html>`_


:code:`Assuming` [:math:`cond`, :math:`expr`]
    Evaluates :math:`expr` assuming the conditions :math:`cond`.





>>> $Assumptions = { x > 0 }

    =
:math:`\left\{x>0\right\}`


>>> Assuming[y>0, ConditionalExpression[y x^2, y>0]//Simplify]

    =
:math:`x^2 y`


>>> Assuming[Not[y>0], ConditionalExpression[y x^2, y>0]//Simplify]

    =
:math:`\text{Undefined}`


>>> ConditionalExpression[y x ^ 2, y > 0]//Simplify

    =
:math:`\text{ConditionalExpression}\left[x^2 y,y>0\right]`


