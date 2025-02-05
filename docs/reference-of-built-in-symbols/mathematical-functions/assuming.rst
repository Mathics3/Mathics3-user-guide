Assuming
========

`WMA link <https://reference.wolfram.com/language/ref/Assuming.html>`_


:code:`Assuming` [:math:`cond`, :math:`expr`]
    Evaluates :math:`expr` assuming the conditions :math:`cond`.





>>> $Assumptions = { x > 0 }
  = {x > 0}
>>> Assuming[y>0, ConditionalExpression[y x^2, y>0]//Simplify]
  = x ^ 2 y
>>> Assuming[Not[y>0], ConditionalExpression[y x^2, y>0]//Simplify]
  = Undefined
>>> ConditionalExpression[y x ^ 2, y > 0]//Simplify
  = ConditionalExpression[x ^ 2 y, y > 0]
