ConditionalExpression
=====================

`WMA link <https://reference.wolfram.com/language/ref/ConditionalExpression.html>`_


:code:`ConditionalExpression` [:math:`expr`, :math:`cond`]
    returns :math:`expr` if :math:`cond` evaluates to :math:`True`, :math:`Undefined` if :math:`cond`           evaluates to :math:`False`.





>>> ConditionalExpression[x^2, True]

    =
:math:`x^2`


>>> ConditionalExpression[x^2, False]

    =
:math:`\text{Undefined}`


>>> f = ConditionalExpression[x^2, x>0]

    =
:math:`\text{ConditionalExpression}\left[x^2,x>0\right]`


>>> f /. x -> 2

    =
:math:`4`


>>> f /. x -> -2

    =
:math:`\text{Undefined}`



:code:`ConditionalExpression`  uses assumptions to evaluate the condition:

>>> $Assumptions = x > 0;


>>> ConditionalExpression[x ^ 2, x>0]//Simplify

    =
:math:`x^2`


>>> $Assumptions = True;



# >> ConditionalExpression[ConditionalExpression[s,x>a], x<b]
# = ConditionalExpression[s, And[x>a, x<b]]