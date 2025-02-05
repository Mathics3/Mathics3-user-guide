Prefix
======

`WMA link <https://reference.wolfram.com/language/ref/Prefix.html>`_


:code:`:math:`f` @ :math:`x``
    is equivalent to :code:`:math:`f`[:math:`x`]` .





>>> a @ b
  = a[b]
>>> a @ b @ c
  = a[b[c]]
>>> Format[p[x_]] := Prefix[{x}, "*"]

>>> p[3]
  = *3
>>> Format[q[x_]] := Prefix[{x}, "~", 350]

>>> q[a+b]
  = ~(a + b)
>>> q[a*b]
  = ~a b
>>> q[a]+b
  = b + ~a

The prefix operator :code:`@`  is parsed to an expression before evaluation:

>>> Hold[a @ b @ c @ d @ e @ f @ x]
  = Hold[a[b[c[d[e[f[x]]]]]]]
