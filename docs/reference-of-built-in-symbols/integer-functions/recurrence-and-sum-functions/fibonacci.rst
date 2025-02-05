Fibonacci
=========

`Fibonacci Sequence <https://en.wikipedia.org/wiki/Fibonacci_sequence>`_, `(:WMA link:https://reference.wolfram.com/language/ref/Fibonacci.html <(:WMA link:https://reference.wolfram.com/language/ref/Fibonacci.html>`_)


:code:`Fibonacci` [:math:`n`]
    computes the :math:`n`-th Fibonacci number.

:code:`Fibonacci` [:math:`n`, :math:`x`]
    computes the Fibonacci polynomial :math:`F_n(x)`.





>>> Fibonacci[0]
  = 0
>>> Fibonacci[1]
  = 1
>>> Fibonacci[10]
  = 55
>>> Fibonacci[200]
  = 280571172992510140037611932413038677189525
>>> Fibonacci[7, x]
  = 1 + 6 x ^ 2 + 5 x ^ 4 + x ^ 6

See also `LinearRecurrence </doc/reference-of-built-in-symbols/integer-functions/recurrence-and-sum-functions/linearrecurrence>`_.