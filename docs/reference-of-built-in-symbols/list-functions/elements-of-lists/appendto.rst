AppendTo
========

`WMA link <https://reference.wolfram.com/language/ref/AppendTo.html>`_


:code:`AppendTo` [:math:`s`, :math:`elem`]
    append :math:`elem` to value of :math:`s` and sets :math:`s` to the result.





>>> s = {};

>>> AppendTo[s, 1]
  = {1}
>>> s
  = {1}

:code:`Append`  works on expressions with heads other than :code:`List` :

>>> y = f[];

>>> AppendTo[y, x]
  = f[x]
>>> y
  = f[x]
