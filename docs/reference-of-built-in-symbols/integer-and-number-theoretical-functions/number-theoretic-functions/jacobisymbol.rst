JacobiSymbol
============

`Jacobi symbol <https://en.wikipedia.org/wiki/Jacobi_symbol>`_ (`WMA <https://reference.wolfram.com/language/ref/JacobiSymbol.html>`_)

:code:`JacobiSymbol` [:math:`a`, :math:`n`]
    returns the Jacobi symbol (:math:`a`/:math:`n`).





>>> Table[JacobiSymbol[n, m], {n, 0, 10}, {m, 1, n, 2}]
  = {{}, {1}, {1}, {1, 0}, {1, 1}, {1, -1, 0}, {1, 0, 1}, {1, 1, -1, 0}, {1, -1, -1, 1}, {1, 0, 1, 1, 0}, {1, 1, 0, -1, 1}}
