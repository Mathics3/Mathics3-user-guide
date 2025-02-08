NumericFunction
===============

`WMA link <https://reference.wolfram.com/language/ref/NumericFunction.html>`_


:code:`NumericFunction`
    is an attribute that indicates that a symbol is the head of a numeric function.





Mathematical functions like :code:`Sqrt`  have attribute :code:`NumericFunction` :

>>> Attributes[Sqrt]
    =

:math:`\left\{\text{Listable},\text{NumericFunction},\text{Protected}\right\}`



Expressions with a head having this attribute, and with all the elements     being numeric expressions, are considered numeric expressions:

>>> NumericQ[Sqrt[1]]
    =

:math:`\text{True}`


>>> NumericQ[a]=True; NumericQ[Sqrt[a]]
    =

:math:`\text{True}`


>>> NumericQ[a]=False; NumericQ[Sqrt[a]]
    =

:math:`\text{False}`


