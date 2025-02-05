PrependTo
=========

`WMA link <https://reference.wolfram.com/language/ref/PrependTo.html>`_


:code:`PrependTo` [:math:`s`, :math:`item`]
    prepends :math:`item` to value of :math:`s` and sets :math:`s` to the result.





Assign s to a list

>>> s = {1, 2, 4, 9}
  = {1, 2, 4, 9}

Add a new value at the beginning of the list:

>>> PrependTo[s, 0]
  = {0, 1, 2, 4, 9}

The value assigned to s has changed:

>>> s
  = {0, 1, 2, 4, 9}

:code:`PrependTo`  works with a head other than :code:`List` :

>>> y = f[a, b, c];

>>> PrependTo[y, x]
  = f[x, a, b, c]
>>> y
  = f[x, a, b, c]
