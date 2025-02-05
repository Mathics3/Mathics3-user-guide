UndirectedEdge
==============

`WML link <https://reference.wolfram.com/language/ref/UndirectedEdge.html>`_


:code:`UndirectedEdge` [:math:`x`, :math:`y`, ...]
    displays :math:`x` ↔ :math:`y` ...
    
    Undirected edges are typically used in network graphs. In Mathics3, \ network graphs are supported through a Mathics3 module.
    
    Issue :code:`LoadModule["pymathics.graph"]`  after :code:`pip`  installing Python package :code:`pymathics-graph` .





>>> UndirectedEdge[x, y, z]
  = x ↔ y ↔ z
>>> a <-> b
  = a ↔ b
