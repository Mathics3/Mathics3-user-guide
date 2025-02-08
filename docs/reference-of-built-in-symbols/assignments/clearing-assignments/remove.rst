Remove
======

`WMA link <https://reference.wolfram.com/language/ref/Remove.html>`_


:code:`Remove` [:math:`x`]
    removes the definition associated to :math:`x`.





>>> a := 2


>>> Names["Global`a"]
    =

:math:`\left\{\text{a}\right\}`


>>> Remove[a]


>>> Names["Global`a"]
    =

:math:`\left\{\right\}`


