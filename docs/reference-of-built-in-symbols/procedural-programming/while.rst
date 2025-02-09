While
=====

`WMA link <https://reference.wolfram.com/language/ref/While.html>`_


:code:`While` [:math:`test`, :math:`body`]
    evaluates :math:`body` as long as :math:`test` evaluates to :code:`True` .

:code:`While` [:math:`test`]
    runs the loop without any body.





Compute the GCD of two numbers:

>>> {a, b} = {27, 6};


>>> While[b != 0, {a, b} = {b, Mod[a, b]}];


>>> a

    =
:math:`3`


