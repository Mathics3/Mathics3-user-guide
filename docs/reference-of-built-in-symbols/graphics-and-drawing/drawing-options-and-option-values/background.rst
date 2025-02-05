Background
==========

`WMA link <https://reference.wolfram.com/language/ref/Background.html>`_


:code:`Background`
    is an option that specifies the color of the background.





The specification must be a Color specification or :code:`Automatic` :

>>> Graphics3D[{Arrow[{{0,0,0},{1,0,1},{0,-1,0},{1,1,1}}]}, Background -> Red]
  = -Graphics3D-

Notice that opacity cannot be specified by passing a :code:`List`  containing :code:`Opacity`      together with a color specification like :code:`{Red, Opacity[.1]}` . Use a color     directive with an alpha channel instead:

>>> Plot[{Sin[x], Cos[x], x / 3}, {x, -Pi, Pi}, Background -> RGBColor[0.5, .5, .5, 0.1]]
  = -Graphics-
