ToExpression
============

`WMA link <https://reference.wolfram.com/language/ref/ToExpression.html>`_

:code:`ToExpression` [:math:`input`]
    interprets a given string as Mathics input.

:code:`ToExpression` [:math:`input`, :math:`form`]
    reads the given input in the specified :math:`form`.

:code:`ToExpression` [:math:`input`, :math:`form`, :math:`h`]
    applies the head :math:`h` to the expression before evaluating it.





>>> ToExpression["1 + 2"]
  = 3
>>> ToExpression["{2, 3, 1}", InputForm, Max]
  = 3
>>> ToExpression["2 3", InputForm]
  = 6

Note that newlines are like semicolons, not blanks. So so the return value is the second-line value.

>>> ToExpression["2\[NewLine]3"]
  = 3
