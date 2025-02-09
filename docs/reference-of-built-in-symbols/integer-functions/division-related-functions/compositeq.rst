CompositeQ
==========

`WMA link <https://reference.wolfram.com/language/ref/CompositeQ.html>`_


:code:`CompositeQ` [:math:`n`]
    returns :code:`True`  if :math:`n` is a composite number







- A composite number is a positive number that is the product of two           integers other than 1.

- For negative integer :math:`n`, :code:`CompositeQ[:math:`n`]`  is effectively equivalent           to :code:`CompositeQ[-:math:`n`]` .




>>> Table[CompositeQ[n], {n, 0, 10}]

    =
:math:`\left\{\text{False},\text{False},\text{False},\text{False},\text{True},\text{False},\text{True},\text{False},\text{True},\text{True},\text{True}\right\}`


