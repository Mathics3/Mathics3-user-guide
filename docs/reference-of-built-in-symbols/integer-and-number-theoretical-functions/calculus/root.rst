Root
====

`WMA link <https://reference.wolfram.com/language/ref/Root.html>`_


:code:`Root` [:math:`f`, :math:`i`]
    represents the i-th complex root of the polynomial :math:`f`.





>>> Root[#1 ^ 2 - 1&, 1]
  = -1
>>> Root[#1 ^ 2 - 1&, 2]
  = 1

Roots that can't be represented by radicals:

>>> Root[#1 ^ 5 + 2 #1 + 1&, 2]
  = Root[1 + #1 ^ 5 + 2 #1&, 2]
