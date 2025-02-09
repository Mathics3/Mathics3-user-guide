ColorData
=========

`WMA link <https://reference.wolfram.com/language/ref/ColorData.html>`_

:code:`ColorData` [":math:`name`"]
    returns a color function with the given :math:`name`.





Define a user-defined color function:

>>> Unprotect[ColorData]; ColorData["test"] := ColorDataFunction["test", "Gradients", {0, 1}, Blend[{Red, Green, Blue}, #1] &]; Protect[ColorData]



Compare it to the default color function, :code:`LakeColors` :

>>> {DensityPlot[x + y, {x, -1, 1}, {y, -1, 1}], DensityPlot[x + y, {x, -1, 1}, {y, -1, 1}, ColorFunction->"test"]}
    = {-Graphics-, -Graphics-}`

