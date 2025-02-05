ProductLog
==========

`WMA link <https://reference.wolfram.com/language/ref/ProductLog.html>`_


:code:`ProductLog` [:math:`z`]
    returns the principle solution for :math:`w` in :math:`z == wE^w`.

:code:`ProductLog` [:math:`k`, :math:`z`]
    gives the :math:`k`-th solution.





The defining equation:

>>> z == ProductLog[z] * E ^ ProductLog[z]
  = True

Some special values:

>>> ProductLog[0]
  = 0
>>> ProductLog[E]
  = 1
>>> ProductLog[-1.5]
  = -0.0327837 + 1.54964 I

The graph of :code:`ProductLog` :

>>> Plot[ProductLog[x], {x, -1/E, E}]
  = -Graphics-
