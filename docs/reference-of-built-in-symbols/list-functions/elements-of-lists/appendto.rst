AppendTo
========

`WMA link <https://reference.wolfram.com/language/ref/AppendTo.html>`_


:code:`AppendTo` [:math:`s`, :math:`elem`]
    append :math:`elem` to value of :math:`s` and sets :math:`s` to the result.





>>> s = {};


>>> AppendTo[s, 1]
    =

:math:`\left\{1\right\}`


>>> s
    =

:math:`\left\{1\right\}`



:code:`Append`  works on expressions with heads other than :code:`List` :

>>> y = f[];


>>> AppendTo[y, x]
    =

:math:`f\left[x\right]`


>>> y
    =

:math:`f\left[x\right]`


