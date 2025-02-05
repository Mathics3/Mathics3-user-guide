Subtract
========

`Subtraction <https://en.wikipedia.org/wiki/Subtraction>`_, (`WMA <https://reference.wolfram.com/language/ref/Subtract.html>`_)


:code:`Subtract` [:math:`a`, :math:`b`]
    same as

:math:`a` :code:`-`  :math:`b`
    represents the subtraction of :math:`b` from :math:`a`.





>>> 5 - 3
  = 2
>>> a - b // FullForm
  = Plus[a, Times[-1, b]]
>>> a - b - c
  = a - b - c
>>> a - (b - c)
  = a - b + c
