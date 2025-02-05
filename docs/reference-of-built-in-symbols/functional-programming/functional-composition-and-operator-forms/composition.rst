Composition
===========

`WMA link <https://reference.wolfram.com/language/ref/Composition.html>`_


:code:`Composition` [:math:`f`, :math:`g`]
    returns the composition of two functions :math:`f` and :math:`g`.





>>> Composition[f, g][x]
  = f[g[x]]
>>> Composition[f, g, h][x, y, z]
  = f[g[h[x, y, z]]]
>>> Composition[]
  = Identity
>>> Composition[][x]
  = x
>>> Attributes[Composition]
  = {Flat, OneIdentity, Protected}
>>> Composition[f, Composition[g, h]]
  = Composition[f, g, h]
