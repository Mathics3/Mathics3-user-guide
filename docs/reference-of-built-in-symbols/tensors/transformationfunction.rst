TransformationFunction
======================

`WMA link <https://reference.wolfram.com/language/ref/TransformationFunction.html>`_


:code:`TransformationFunction` [:math:`m`]
    represents a transformation.





>>> RotationTransform[Pi].TranslationTransform[{1, -1}]

    =
:math:`\text{TransformationFunction}\left[\left\{\left\{-1,0,-1\right\},\left\{0,-1,1\right\},\left\{0,0,1\right\}\right\}\right]`


>>> TranslationTransform[{1, -1}].RotationTransform[Pi]

    =
:math:`\text{TransformationFunction}\left[\left\{\left\{-1,0,1\right\},\left\{0,-1,-1\right\},\left\{0,0,1\right\}\right\}\right]`


