NestList
========

`WMA link <https://reference.wolfram.com/language/ref/NestList.html>`_


:code:`NestList` [:math:`f`, :math:`expr`, :math:`n`]
    starting with :math:`expr`, iteratively applies :math:`f` :math:`n` times and           returns a list of all intermediate results.





>>> NestList[f, x, 3]
  = {x, f[x], f[f[x]], f[f[f[x]]]}
>>> NestList[2 # &, 1, 8]
  = {1, 2, 4, 8, 16, 32, 64, 128, 256}

Chaos game rendition of the Sierpinski triangle:

>>> vertices = {{0,0}, {1,0}, {.5, .5 Sqrt[3]}};

>>> points = NestList[.5(vertices[[ RandomInteger[{1,3}] ]] + #) &, {0.,0.}, 500];

>>> Graphics[Point[points], ImageSize->Small]
  = -Graphics-
