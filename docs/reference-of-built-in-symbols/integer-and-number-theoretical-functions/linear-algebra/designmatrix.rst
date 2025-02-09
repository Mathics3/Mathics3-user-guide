DesignMatrix
============

`WMA link <https://reference.wolfram.com/language/ref/DesignMatrix.html>`_


:code:`DesignMatrix` [:math:`m`, :math:`f`, :math:`x`]
    returns the design matrix for a linear model :math:`f` in the variables :math:`x`.





>>> DesignMatrix[{{2, 1}, {3, 4}, {5, 3}, {7, 6}}, x, x]

    =
:math:`\left\{\left\{1,2\right\},\left\{1,3\right\},\left\{1,5\right\},\left\{1,7\right\}\right\}`


>>> DesignMatrix[{{2, 1}, {3, 4}, {5, 3}, {7, 6}}, f[x], x]

    =
:math:`\left\{\left\{1,f\left[2\right]\right\},\left\{1,f\left[3\right]\right\},\left\{1,f\left[5\right]\right\},\left\{1,f\left[7\right]\right\}\right\}`


