Nest
====

`WMA link <https://reference.wolfram.com/language/ref/Nest.html>`_


:code:`Nest` [:math:`f`, :math:`expr`, :math:`n`]
    starting with :math:`expr`, iteratively applies :math:`f` :math:`n` times and returns the final result.





>>> Nest[f, x, 3]
  = f[f[f[x]]]
>>> Nest[(1+#) ^ 2 &, x, 2]
  = (1 + (1 + x) ^ 2) ^ 2
>>> Nest[Subsuperscript[#,#,#]&,0,5]
  = ...
