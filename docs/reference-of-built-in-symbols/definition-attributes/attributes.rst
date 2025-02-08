Attributes
==========

`WMA link <https://reference.wolfram.com/language/ref/Attributes.html>`_


:code:`Attributes` [:math:`symbol`]
    returns the attributes of :math:`symbol`.

:code:`Attributes` [":math:`string`"]
    returns the attributes of :code:`Symbol` [":math:`string`"].

:code:`Attributes` [:math:`symbol`] = {:math:`attr_1`, :math:`attr_2`}
    sets the attributes of :math:`symbol`, replacing any existing attributes.





>>> Attributes[Plus]
    =

:math:`\left\{\text{Flat},\text{Listable},\text{NumericFunction},\text{OneIdentity},\text{Orderless},\text{Protected}\right\}`


>>> Attributes["Plus"]
    =

:math:`\left\{\text{Flat},\text{Listable},\text{NumericFunction},\text{OneIdentity},\text{Orderless},\text{Protected}\right\}`



:code:`Attributes`  always considers the head of an expression:

>>> Attributes[a + b + c]
    =

:math:`\left\{\text{Flat},\text{Listable},\text{NumericFunction},\text{OneIdentity},\text{Orderless},\text{Protected}\right\}`



You can assign values to :code:`Attributes`  to set attributes:

>>> Attributes[f] = {Flat, Orderless}
    =

:math:`\left\{\text{Flat},\text{Orderless}\right\}`


>>> f[b, f[a, c]]
    =

:math:`f\left[a,b,c\right]`



Attributes must be symbols:

>>> Attributes[f] := {a + b}

    Attributes::sym Argument a + b at position 1 is expected to be a symbol.
    =

:math:`\text{\$Failed}`



Use :code:`Symbol`  to convert strings to symbols:

>>> Attributes[f] = Symbol["Listable"]
    =

:math:`\text{Listable}`


>>> Attributes[f]
    =

:math:`\left\{\text{Listable}\right\}`


