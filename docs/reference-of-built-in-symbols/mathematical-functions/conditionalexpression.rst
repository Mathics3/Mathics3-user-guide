ConditionalExpression
=====================

`WMA link <https://reference.wolfram.com/language/ref/ConditionalExpression.html>`_


:code:`ConditionalExpression` [:math:`expr`, :math:`cond`]
    returns :math:`expr` if :math:`cond` evaluates to :math:`True`, :math:`Undefined` if :math:`cond`           evaluates to :math:`False`.





>>> ConditionalExpression[x^2, True]
  = x ^ 2
>>> ConditionalExpression[x^2, False]
  = Undefined
>>> f = ConditionalExpression[x^2, x>0]
  = ConditionalExpression[x ^ 2, x > 0]
>>> f /. x -> 2
  = 4
>>> f /. x -> -2
  = Undefined

:code:`ConditionalExpression`  uses assumptions to evaluate the condition:

>>> $Assumptions = x > 0;

>>> ConditionalExpression[x ^ 2, x>0]//Simplify
  = x ^ 2
>>> $Assumptions = True;


# >> ConditionalExpression[ConditionalExpression[s,x>a], x<b]
# = ConditionalExpression[s, And[x>a, x<b]]