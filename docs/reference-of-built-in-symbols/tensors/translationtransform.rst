TranslationTransform
====================

`WMA link <https://reference.wolfram.com/language/ref/TranslationTransform.html>`_


:code:`TranslationTransform` [:math:`v`]
    gives a :code:`TransformationFunction`  that translates points by vector :math:`v`.





>>> t = TranslationTransform[{x0, y0}]

    =
:math:`\text{TransformationFunction}\left[\left\{\left\{1,0,\text{x0}\right\},\left\{0,1,\text{y0}\right\},\left\{0,0,1\right\}\right\}\right]`


>>> t[{x, y}]

    =
:math:`\left\{x+\text{x0},y+\text{y0}\right\}`



From `Creating a Sierpinsky gasket with the missing triangles filled in <"https://mathematica.stackexchange.com/questions/7360/creating-a-sierpinski-gasket-with-the-missing-triangles-filled-in/7361#7361>`_:

>>> Show[Graphics[Table[Polygon[TranslationTransform[{Sqrt[3] (i - j/2), 3 j/2}] /@ {{Sqrt[3]/2, -1/2}, {0, 1}, {-Sqrt[3]/2, -1/2}}], {i, 7}, {j, i}]]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Tensors_TranslationTransform_7soc0056.png
    :align: center



