StringQ
=======

`WMA link <https://reference.wolfram.com/language/ref/StringQ.html>`_

:code:`StringQ` [:math:`expr`]
    returns :code:`True`  if :math:`expr` is a :code:`String` , or :code:`False`  otherwise.





>>> StringQ["abc"]
    =

:math:`\text{True}`


>>> StringQ[1.5]
    =

:math:`\text{False}`


>>> Select[{"12", 1, 3, 5, "yz", x, y}, StringQ]
    =

:math:`\left\{\text{12},\text{yz}\right\}`


