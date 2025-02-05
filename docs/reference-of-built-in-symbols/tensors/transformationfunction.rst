TransformationFunction
======================

`WMA link <https://reference.wolfram.com/language/ref/TransformationFunction.html>`_


:code:`TransformationFunction` [:math:`m`]
    represents a transformation.





>>> RotationTransform[Pi].TranslationTransform[{1, -1}]
  = TransformationFunction[{{-1, 0, -1}, {0, -1, 1}, {0, 0, 1}}]
>>> TranslationTransform[{1, -1}].RotationTransform[Pi]
  = TransformationFunction[{{-1, 0, 1}, {0, -1, -1}, {0, 0, 1}}]
