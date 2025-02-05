TranslationTransform
====================

`WMA link <https://reference.wolfram.com/language/ref/TranslationTransform.html>`_


:code:`TranslationTransform` [:math:`v`]
    gives a :code:`TransformationFunction`  that translates points by vector :math:`v`.





>>> t = TranslationTransform[{x0, y0}]
  = TransformationFunction[{{1, 0, x0}, {0, 1, y0}, {0, 0, 1}}]
>>> t[{x, y}]
  = {x + x0, y + y0}

From `Creating a Sierpinsky gasket with the missing triangles filled in <"https://mathematica.stackexchange.com/questions/7360/creating-a-sierpinski-gasket-with-the-missing-triangles-filled-in/7361#7361>`_:

>>> Show[Graphics[Table[Polygon[TranslationTransform[{Sqrt[3] (i - j/2), 3 j/2}] /@ {{Sqrt[3]/2, -1/2}, {0, 1}, {-Sqrt[3]/2, -1/2}}], {i, 7}, {j, i}]]]
  = -Graphics-
