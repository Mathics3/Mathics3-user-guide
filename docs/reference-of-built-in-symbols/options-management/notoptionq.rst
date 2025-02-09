NotOptionQ
==========

`WMA link <https://reference.wolfram.com/language/ref/NotOptionQ.html>`_


:code:`NotOptionQ` [:math:`expr`]
    returns :code:`True`  if :math:`expr` does not have the form of a valid           option specification.





>>> NotOptionQ[x]

    =
:math:`\text{True}`


>>> NotOptionQ[2]

    =
:math:`\text{True}`


>>> NotOptionQ["abc"]

    =
:math:`\text{True}`


>>> NotOptionQ[a -> True]

    =
:math:`\text{False}`


