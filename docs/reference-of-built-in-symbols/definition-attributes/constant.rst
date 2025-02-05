Constant
========

`WMA link <https://reference.wolfram.com/language/ref/Constant.html>`_


:code:`Constant`
    is an attribute that indicates that a symbol is a constant.





Mathematical constants like :code:`E`  have attribute :code:`Constant` :

>>> Attributes[E]
  = {Constant, Protected, ReadProtected}

Constant symbols cannot be used as variables in :code:`Solve`  and
related functions:

>>> Solve[x + E == 0, E]
  = Solve[x + E == 0, E]
