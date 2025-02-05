Normal
======

`WMA link <https://reference.wolfram.com/language/ref/Normal.html>`_


:code:`Normal[expr_]`
    Brings special expressions to a normal expression from different special            forms.





>>> Normal[Pi]
  = Pi
>>> Series[Exp[x], {x, 0, 5}]
  = 1 + x + 1 / 2 x ^ 2 + 1 / 6 x ^ 3 + 1 / 24 x ^ 4 + 1 / 120 x ^ 5 + O[x] ^ 6
>>> Normal[%]
  = 1 + x + x ^ 2 / 2 + x ^ 3 / 6 + x ^ 4 / 24 + x ^ 5 / 120
