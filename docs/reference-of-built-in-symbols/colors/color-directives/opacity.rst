Opacity
=======

`Alpha compositing <https://en.wikipedia.org/wiki/Alpha_compositing>`_ (`WMA link <https://reference.wolfram.com/language/ref/Opacity.html>`_)


:code:`Opacity` [:math:`level`]
    is a graphics directive that sets the opacity to :math:`level`; :math:`level` is a            value between 0 and 1.





>>> Graphics[{Blue, Disk[{.5, 1}, 1], Opacity[.4], Red, Disk[], Opacity[.2], Green, Disk[{-.5, 1}, 1]}]
  = -Graphics-
>>> Graphics3D[{Blue, Sphere[], Opacity[.4], Red, Cuboid[]}]
  = -Graphics3D-

Notice that :code:`Opacity`  does not overwrite the value of the alpha channel if it is set in a color directive:

>>> Graphics[{Blue, Disk[], RGBColor[1,0,0,1],Opacity[.2], Rectangle[{0,0},{1,1}]}]
  = -Graphics-
