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
  = {Flat, Listable, NumericFunction, OneIdentity, Orderless, Protected}
>>> Attributes["Plus"]
  = {Flat, Listable, NumericFunction, OneIdentity, Orderless, Protected}

:code:`Attributes`  always considers the head of an expression:

>>> Attributes[a + b + c]
  = {Flat, Listable, NumericFunction, OneIdentity, Orderless, Protected}

You can assign values to :code:`Attributes`  to set attributes:

>>> Attributes[f] = {Flat, Orderless}
  = {Flat, Orderless}
>>> f[b, f[a, c]]
  = f[a, b, c]

Attributes must be symbols:

>>> Attributes[f] := {a + b}
  = $Failed

Use :code:`Symbol`  to convert strings to symbols:

>>> Attributes[f] = Symbol["Listable"]
  = Listable
>>> Attributes[f]
  = {Listable}
