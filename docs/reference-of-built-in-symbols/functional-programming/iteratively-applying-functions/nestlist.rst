NestList
========

`WMA link <https://reference.wolfram.com/language/ref/NestList.html>`_


:code:`NestList` [:math:`f`, :math:`expr`, :math:`n`]
    starting with :math:`expr`, iteratively applies :math:`f` :math:`n` times and           returns a list of all intermediate results.





>>> NestList[f, x, 3]

    =
:math:`\left\{x,f\left[x\right],f\left[f\left[x\right]\right],f\left[f\left[f\left[x\right]\right]\right]\right\}`


>>> NestList[2 # &, 1, 8]

    =
:math:`\left\{1,2,4,8,16,32,64,128,256\right\}`



Chaos game rendition of the Sierpinski triangle:

>>> vertices = {{0,0}, {1,0}, {.5, .5 Sqrt[3]}};


>>> points = NestList[.5(vertices[[ RandomInteger[{1,3}] ]] + #) &, {0.,0.}, 500];


>>> Graphics[Point[points], ImageSize->Small]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Functional_Programming_NestList__fk3ugn1.png
    :align: center



