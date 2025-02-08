SingularValueDecomposition
==========================

`Singular Value Decomposition <https://en.wikipedia.org/wiki/Singular_value_decomposition>`_     (`WMA link <https://reference.wolfram.com/language/ref/SingularValueDecomposition.html>`_)


:code:`SingularValueDecomposition` [:math:`m`]
    calculates the singular value decomposition for the matrix :math:`m`.





:code:`SingularValueDecomposition`  returns :math:`u`, :math:`s`, :math:`w` such that :math:`m`=:math:`u` :math:`s` :math:`v`,
:math:`u`:code:`:math:`u`=1, :math:`v`` :math:`v`=1, and :math:`s` is diagonal.

>>> SingularValueDecomposition[{{1.5, 2.0}, {2.5, 3.0}}]
    =

:math:`\left\{\left\{\left\{0.538954,0.842335\right\},\left\{0.842335,-0.538954\right\}\right\},\left\{\left\{4.63555,0.\right\},\left\{0.,0.107862\right\}\right\},\left\{\left\{0.628678,0.777666\right\},\left\{-0.777666,0.628678\right\}\right\}\right\}`


