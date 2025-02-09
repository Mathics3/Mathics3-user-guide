Colorize
========

`WMA link <https://reference.wolfram.com/language/ref/Colorize.html>`_


:code:`Colorize` [:math:`values`]
    returns an image where each number in the rectangular matrix           :math:`values` is a pixel and each occurrence of the same number is           displayed in the same unique color, which is different from the           colors of all non-identical numbers.

:code:`Colorize` [:math:`image`]
    gives a colorized version of :math:`image`.





>>> Colorize[{{1.3, 2.1, 1.5}, {1.3, 1.3, 2.1}, {1.3, 2.1, 1.5}}]

    =
.. image:: tmp7b_mnzbo.png
    :align: center



>>> Colorize[{{1, 2}, {2, 2}, {2, 3}}, ColorFunction -> (Blend[{White, Blue}, #]&)]

    =
.. image:: tmp1x3vfegb.png
    :align: center



