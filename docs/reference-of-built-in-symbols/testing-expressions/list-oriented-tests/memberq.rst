MemberQ
=======

`WMA link <https://reference.wolfram.com/language/ref/MemberQ.html>`_


:code:`MemberQ` [:math:`list`, :math:`pattern`]
    returns :code:`True`  if :math:`pattern` matches any element of :math:`list`, or :code:`False`  otherwise.





>>> MemberQ[{a, b, c}, b]
  = True
>>> MemberQ[{a, b, c}, d]
  = False
>>> MemberQ[{"a", b, f[x]}, _?NumericQ]
  = False
>>> MemberQ[_List][{{}}]
  = True
