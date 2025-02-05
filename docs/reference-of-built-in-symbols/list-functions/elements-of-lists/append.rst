Append
======

`WMA link <https://reference.wolfram.com/language/ref/Append.html>`_


:code:`Append` [:math:`expr`, :math:`elem`]
    returns :math:`expr` with :math:`elem` appended.





>>> Append[{1, 2, 3}, 4]
  = {1, 2, 3, 4}

:code:`Append`  works on expressions with heads other than :code:`List` :

>>> Append[f[a, b], c]
  = f[a, b, c]

Unlike :code:`Join` , :code:`Append`  does not flatten lists in :math:`item`:

>>> Append[{a, b}, {c, d}]
  = {a, b, {c, d}}
