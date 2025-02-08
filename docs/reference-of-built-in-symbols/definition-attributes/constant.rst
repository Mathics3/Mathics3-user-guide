Constant
========

`WMA link <https://reference.wolfram.com/language/ref/Constant.html>`_


:code:`Constant`
    is an attribute that indicates that a symbol is a constant.





Mathematical constants like :code:`E`  have attribute :code:`Constant` :

>>> Attributes[E]
    =

:math:`\left\{\text{Constant},\text{Protected},\text{ReadProtected}\right\}`



Constant symbols cannot be used as variables in :code:`Solve`  and
related functions:

>>> Solve[x + E == 0, E]

    Solve::ivar E is not a valid variable.
    =

:math:`\text{Solve}\left[x+E\text{==}0,E\right]`


