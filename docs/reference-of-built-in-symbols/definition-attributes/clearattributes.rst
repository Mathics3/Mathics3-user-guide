ClearAttributes
===============

`WMA link <https://reference.wolfram.com/language/ref/ClearAttributes.html>`_


:code:`ClearAttributes` [:math:`symbol`, :math:`attrib`]
    removes :math:`attrib` from :math:`symbol`'s attributes.





>>> SetAttributes[f, Flat]

>>> Attributes[f]
  = {Flat}
>>> ClearAttributes[f, Flat]

>>> Attributes[f]
  = {}

Attributes that are not even set are simply ignored:

>>> ClearAttributes[{f}, {Flat}]

>>> Attributes[f]
  = {}
