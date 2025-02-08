DirectedEdge
============

`WML link <https://reference.wolfram.com/language/ref/DirectedEdge.html>`_


:code:`DirectedEdge` [:math:`x`, :math:`y`, ...]
    displays :math:`x` → :math:`y` → ...
    
    Directed edges are typically used in network graphs. In Mathics3, network graphs are supported through a Mathics3 module.
    
    Issue :code:`LoadModule["pymathics.graph"]`  after :code:`pip`  installing Python package :code:`pymathics-graph` .





>>> DirectedEdge[x, y, z]
    =

:math:`x \rightarrow y \rightarrow z`


>>> a \[DirectedEdge] b
    =

:math:`a \rightarrow b`


