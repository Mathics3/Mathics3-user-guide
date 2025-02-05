ArrayDepth
==========

`WMA link <https://reference.wolfram.com/language/ref/ArrayDepth.html>`_


:code:`ArrayDepth` [:math:`a`]
    returns the depth of the non-ragged array :math:`a`, defined as       :code:`Length[Dimensions[:math:`a`]]` .





>>> ArrayDepth[{{a,b},{c,d}}]
  = 2
>>> ArrayDepth[x]
  = 0
