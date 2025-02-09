ColorDistance
=============

`Color difference <https://en.wikipedia.org/wiki/Color_difference>`_ (`WMA link <https://reference.wolfram.com/language/ref/ColorDistance.html>`_)


:code:`ColorDistance` [:math:`c_1`, :math:`c_2`]
    returns a measure of color distance between the colors :math:`c_1` and :math:`c_2`.

:code:`ColorDistance` [:math:`list`, :math:`c_2`]
    returns a list of color distances between the colors in :math:`list` and :math:`c_2`.





The option DistanceFunction specifies the method used to measure the color
distance. Available options are:



- `CIE76 <https://en.wikipedia.org/wiki/Color_difference#CIE76>`_: Euclidean distance in the LABColor space

- `CIE94 <https://en.wikipedia.org/wiki/Color_difference#CIE94>`_: Euclidean distance in the LCHColor space

- CIE2000 or `CIEDE2000 <https://en.wikipedia.org/wiki/Color_difference#CIEDE2000>`_: CIE94 distance with corrections

- CMC: Color Measurement Committee metric (1984)

- DeltaL: difference in the L component of LCHColor

- DeltaC: difference in the C component of LCHColor

- DeltaH: difference in the H component of LCHColor




It is also possible to specify a custom distance.

>>> ColorDistance[Magenta, Green]

    =
:math:`2.2507`


>>> ColorDistance[{Red, Blue}, {Green, Yellow}, DistanceFunction -> {"CMC", "Perceptibility"}]

    =
:math:`\left\{1.0495,1.27455\right\}`


