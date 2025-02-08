Except
======

`WMA link <https://reference.wolfram.com/language/ref/Except.html>`_


:code:`Except` [:math:`c`]
    represents a pattern object that matches any expression except           those matching :math:`c`.

:code:`Except` [:math:`c`, :math:`p`]
    represents a pattern object that matches :math:`p` but not :math:`c`.





>>> Cases[{x, a, b, x, c}, Except[x]]
    =

:math:`\left\{a,b,c\right\}`


>>> Cases[{a, 0, b, 1, c, 2, 3}, Except[1, _Integer]]
    =

:math:`\left\{0,2,3\right\}`



Except can also be used for string expressions:

>>> StringReplace["Hello world!", Except[LetterCharacter] -> ""]
    =

:math:`\text{Helloworld}`


