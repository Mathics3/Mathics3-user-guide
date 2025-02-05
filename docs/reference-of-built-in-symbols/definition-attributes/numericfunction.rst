NumericFunction
===============

`WMA link <https://reference.wolfram.com/language/ref/NumericFunction.html>`_


:code:`NumericFunction`
    is an attribute that indicates that a symbol is the head of a numeric function.





Mathematical functions like :code:`Sqrt`  have attribute :code:`NumericFunction` :

>>> Attributes[Sqrt]
  = {Listable, NumericFunction, Protected}

Expressions with a head having this attribute, and with all the elements     being numeric expressions, are considered numeric expressions:

>>> NumericQ[Sqrt[1]]
  = True
>>> NumericQ[a]=True; NumericQ[Sqrt[a]]
  = True
>>> NumericQ[a]=False; NumericQ[Sqrt[a]]
  = False
