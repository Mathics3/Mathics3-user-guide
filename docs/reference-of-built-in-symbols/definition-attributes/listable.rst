Listable
========

`WMA link <https://reference.wolfram.com/language/ref/Listable.html>`_


:code:`Listable`
    is an attribute specifying that a function should be         automatically applied to each element of a list.





>>> SetAttributes[f, Listable]

>>> f[{1, 2, 3}, {4, 5, 6}]
  = {f[1, 4], f[2, 5], f[3, 6]}
>>> f[{1, 2, 3}, 4]
  = {f[1, 4], f[2, 4], f[3, 4]}
>>> {{1, 2}, {3, 4}} + {5, 6}
  = {{6, 7}, {9, 10}}
