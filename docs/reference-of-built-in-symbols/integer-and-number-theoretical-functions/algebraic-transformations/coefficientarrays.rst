CoefficientArrays
=================

`WMA link <https://reference.wolfram.com/language/ref/CoefficientArrays.html>`_


:code:`CoefficientArrays` [:math:`polys`, :math:`vars`]
    returns a list of arrays of coefficients of the variables :math:`vars`           in the polynomial  :math:`poly`.





>>> CoefficientArrays[1 + x^3, x]
    =

:math:`\left\{1,\left\{0\right\},\left\{\left\{0\right\}\right\},\left\{\left\{\left\{1\right\}\right\}\right\}\right\}`


>>> CoefficientArrays[1 + x y+ x^3, {x, y}]
    =

:math:`\left\{1,\left\{0,0\right\},\left\{\left\{0,1\right\},\left\{0,0\right\}\right\},\left\{\left\{\left\{1,0\right\},\left\{0,0\right\}\right\},\left\{\left\{0,0\right\},\left\{0,0\right\}\right\}\right\}\right\}`


>>> CoefficientArrays[{1 + x^2, x y}, {x, y}]
    =

:math:`\left\{\left\{1,0\right\},\left\{\left\{0,0\right\},\left\{0,0\right\}\right\},\left\{\left\{\left\{1,0\right\},\left\{0,0\right\}\right\},\left\{\left\{0,1\right\},\left\{0,0\right\}\right\}\right\}\right\}`


>>> CoefficientArrays[(x+y+Sin[z])^3, {x,y}]
    =

:math:`\left\{\text{Sin}\left[z\right]^3,\left\{3 \text{Sin}\left[z\right]^2,3 \text{Sin}\left[z\right]^2\right\},\left\{\left\{3 \text{Sin}\left[z\right],6 \text{Sin}\left[z\right]\right\},\left\{0,3 \text{Sin}\left[z\right]\right\}\right\},\left\{\left\{\left\{1,3\right\},\left\{0,3\right\}\right\},\left\{\left\{0,0\right\},\left\{0,1\right\}\right\}\right\}\right\}`


>>> CoefficientArrays[(x + y + Sin[z])^3, {x, z}]

    CoefficientArrays::poly (x + y + Sin[z]) ^ 3 is not a polynomial in {x, z}
    =

:math:`\text{CoefficientArrays}\left[\left(x+y+\text{Sin}\left[z\right]\right)^3,\left\{x,z\right\}\right]`


