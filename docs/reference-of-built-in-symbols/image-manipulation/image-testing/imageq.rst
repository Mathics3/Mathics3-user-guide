ImageQ
======

`WMA link <https://reference.wolfram.com/language/ref/ImageQ.html>`_


:code:`ImageQ[Image` [:math:`pixels`]]
    returns :code:`True`  if :math:`pixels` has dimensions from which an Image can be constructed, and :code:`False`  otherwise.





>>> ImageQ[Image[{{0, 1}, {1, 0}}]]

    =
:math:`\text{True}`


>>> ImageQ[Image[{{{0, 0, 0}, {0, 1, 0}}, {{0, 1, 0}, {0, 1, 1}}}]]

    =
:math:`\text{True}`


>>> ImageQ[Image[{{{0, 0, 0}, {0, 1}}, {{0, 1, 0}, {0, 1, 1}}}]]

    =
:math:`\text{False}`


>>> ImageQ[Image[{1, 0, 1}]]

    =
:math:`\text{False}`


>>> ImageQ["abc"]

    =
:math:`\text{False}`


