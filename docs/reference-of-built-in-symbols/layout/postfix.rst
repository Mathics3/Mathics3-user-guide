Postfix
=======

`WMA link <https://reference.wolfram.com/language/ref/Postfix.html>`_


:code:`:math:`x` // :math:`f``
    is equivalent to :code:`:math:`f`[:math:`x`]` .





>>> b // a
  = a[b]
>>> c // b // a
  = a[b[c]]

The postfix operator :code:`//`  is parsed to an expression before evaluation:

>>> Hold[x // a // b // c // d // e // f]
  = Hold[f[e[d[c[b[a[x]]]]]]]
