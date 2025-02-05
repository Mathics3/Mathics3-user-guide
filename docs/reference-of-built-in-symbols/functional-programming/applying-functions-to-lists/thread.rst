Thread
======

`WMA link <https://reference.wolfram.com/language/ref/Thread.html>`_


:code:`Thread[:math:`f`` [:math:`args`]]
    threads :math:`f` over any lists that appear in :math:`args`.

:code:`Thread[:math:`f`` [:math:`args`], :math:`h`]
    threads over any parts with head :math:`h`.





>>> Thread[f[{a, b, c}]]
  = {f[a], f[b], f[c]}
>>> Thread[f[{a, b, c}, t]]
  = {f[a, t], f[b, t], f[c, t]}
>>> Thread[f[a + b + c], Plus]
  = f[a] + f[b] + f[c]

Functions with attribute :code:`Listable`  are automatically threaded over lists:

>>> {a, b, c} + {d, e, f} + g
  = {a + d + g, b + e + g, c + f + g}
