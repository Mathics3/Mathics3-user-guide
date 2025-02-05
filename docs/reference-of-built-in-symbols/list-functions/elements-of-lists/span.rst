Span
====

`WMA link <https://reference.wolfram.com/language/ref/Span.html>`_


:code:`Span`
    is the head of span ranges like :code:`1;;3` .





>>> ;; // FullForm
  = Span[1, All]
>>> 1;;4;;2 // FullForm
  = Span[1, 4, 2]
>>> 2;;-2 // FullForm
  = Span[2, -2]
>>> ;;3 // FullForm
  = Span[1, 3]
