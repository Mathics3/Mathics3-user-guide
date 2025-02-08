Minus
=====

`Additive inverse <https://en.wikipedia.org/wiki/Additive_inverse>`_ (`WMA <https://reference.wolfram.com/language/ref/Minus.html>`_)


:code:`Minus` [:math:`expr`]
    is the negation of :math:`expr`.





>>> -a //FullForm
    =

:math:`\text{Times}\left[-1, a\right]`



:code:`Minus`  automatically distributes:

>>> -(x - 2/3)
    =

:math:`\frac{2}{3}-x`



:code:`Minus`  threads over lists:

>>> -Range[10]
    =

:math:`\left\{-1,-2,-3,-4,-5,-6,-7,-8,-9,-10\right\}`


