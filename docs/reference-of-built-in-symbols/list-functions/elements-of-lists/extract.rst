Extract
=======

`WMA link <https://reference.wolfram.com/language/ref/Extract.html>`_


:code:`Extract` [:math:`expr`, :math:`list`]
    extracts parts of :math:`expr` specified by :math:`list`.

:code:`Extract` [:math:`expr`, {:math:`list_1`, :math:`list_2`, ...}]
    extracts a list of parts.





:code:`Extract[:math:`expr`, :math:`i`, :math:`j`, ...]`  is equivalent to :code:`Part[:math:`expr`, {:math:`i`, :math:`j`, ...}]` .

>>> Extract[a + b + c, {2}]
  = b
>>> Extract[{{a, b}, {c, d}}, {{1}, {2, 2}}]
  = {{a, b}, d}
