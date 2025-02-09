Composition
===========

`WMA link <https://reference.wolfram.com/language/ref/Composition.html>`_


:code:`Composition` [:math:`f`, :math:`g`]
    returns the composition of two functions :math:`f` and :math:`g`.





>>> Composition[f, g][x]

    =
:math:`f\left[g\left[x\right]\right]`


>>> Composition[f, g, h][x, y, z]

    =
:math:`f\left[g\left[h\left[x,y,z\right]\right]\right]`


>>> Composition[]

    =
:math:`\text{Identity}`


>>> Composition[][x]

    =
:math:`x`


>>> Attributes[Composition]

    =
:math:`\left\{\text{Flat},\text{OneIdentity},\text{Protected}\right\}`


>>> Composition[f, Composition[g, h]]

    =
:math:`\text{Composition}\left[f,g,h\right]`


