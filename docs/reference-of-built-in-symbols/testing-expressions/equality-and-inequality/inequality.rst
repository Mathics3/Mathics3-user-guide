Inequality
==========

`WMA link <https://reference.wolfram.com/language/ref/Inequality.html>`_


:code:`Inequality`
    is the head of expressions involving different inequality
    operators (at least temporarily). Thus, it is possible to
    write chains of inequalities.





>>> a < b <= c
  = a < b && b <= c
>>> Inequality[a, Greater, b, LessEqual, c]
  = a > b && b <= c
>>> 1 < 2 <= 3
  = True
>>> 1 < 2 > 0
  = True
>>> 1 < 2 < -1
  = False
