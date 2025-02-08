Variables
=========

`WMA link <https://reference.wolfram.com/language/ref/Variables.html>`_


:code:`Variables` [:math:`expr`]
    gives a list of the variables that appear in the polynomial :math:`expr`.





>>> Variables[a x^2 + b x + c]
    =

:math:`\left\{a,b,c,x\right\}`


>>> Variables[{a + b x, c y^2 + x/2}]
    =

:math:`\left\{a,b,c,x,y\right\}`


>>> Variables[x + Sin[y]]
    =

:math:`\left\{x,\text{Sin}\left[y\right]\right\}`


