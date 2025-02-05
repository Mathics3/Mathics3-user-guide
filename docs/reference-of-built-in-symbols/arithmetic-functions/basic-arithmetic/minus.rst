Minus
=====

`Additive inverse <https://en.wikipedia.org/wiki/Additive_inverse>`_ (`WMA <https://reference.wolfram.com/language/ref/Minus.html>`_)


:code:`Minus` [:math:`expr`]
    is the negation of :math:`expr`.





>>> -a //FullForm
  = Times[-1, a]

:code:`Minus`  automatically distributes:

>>> -(x - 2/3)
  = 2 / 3 - x

:code:`Minus`  threads over lists:

>>> -Range[10]
  = {-1, -2, -3, -4, -5, -6, -7, -8, -9, -10}
