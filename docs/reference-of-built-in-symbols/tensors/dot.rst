Dot
===

`Dot product <https://en.wikipedia.org/wiki/Dot_product>`_     (`WMA link <https://reference.wolfram.com/language/ref/Dot.html>`_)


:code:`Dot` [:math:`x`, :math:`y`]
    same as

:code:`:math:`x` . :math:`y``
    computes the vector dot product or matrix product :math:`x` . :math:`y`.





Scalar product of vectors:

>>> {a, b, c} . {x, y, z}
  = a x + b y + c z

Product of matrices and vectors:

>>> {{a, b}, {c, d}} . {x, y}
  = {a x + b y, c x + d y}

Matrix product:

>>> {{a, b}, {c, d}} . {{r, s}, {t, u}}
  = {{a r + b t, a s + b u}, {c r + d t, c s + d u}}
>>> a . b
  = a . b
