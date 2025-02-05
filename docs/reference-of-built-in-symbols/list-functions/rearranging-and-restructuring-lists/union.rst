Union
=====

`WMA link <https://reference.wolfram.com/language/ref/Union.html>`_


:code:`Union` [:math:`a`, :math:`b`, ...]
    gives the union of the given set or sets. The resulting list           will be sorted and each element will only occur once.





>>> Union[{5, 1, 3, 7, 1, 8, 3}]
  = {1, 3, 5, 7, 8}
>>> Union[{a, b, c}, {c, d, e}]
  = {a, b, c, d, e}
>>> Union[{c, b, a}]
  = {a, b, c}
>>> Union[{{a, 1}, {b, 2}}, {{c, 1}, {d, 3}}, SameTest->(SameQ[Last[#1],Last[#2]]&)]
  = {{b, 2}, {c, 1}, {d, 3}}
>>> Union[{1, 2, 3}, {2, 3, 4}, SameTest->Less]
  = {1, 2, 2, 3, 4}
