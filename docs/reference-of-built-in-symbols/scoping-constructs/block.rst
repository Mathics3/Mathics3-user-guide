Block
=====

`WMA link <https://reference.wolfram.com/language/ref/Block.html>`_


:code:`Block` [{:math:`x`, :math:`y`, ...}, :math:`expr`]
    temporarily removes the definitions of the given variables, evaluates           :math:`expr`, and restores the original definitions afterwards.

:code:`Block` [{:math:`x`=:math:`x_0`, :math:`y`=:math:`y_0`, ...}, :math:`expr`]
    assigns temporary values to the variables during the evaluation of :math:`expr`.





>>> n = 10
  = 10
>>> Block[{n = 5}, n ^ 2]
  = 25
>>> n
  = 10

Values assigned to block variables are evaluated at the beginning of the block.
Keep in mind that the result of :code:`Block`  is evaluated again, so a returned block variable
will get its original value.

>>> Block[{x = n+2, n}, {x, n}]
  = {12, 10}

If the variable specification is not of the described form, an error message is raised.

>>> Block[{x + y}, x]
  = x

Variable names may not appear more than once:

>>> Block[{x, x}, x]
  = x
