NestWhile
=========

`WMA link <https://reference.wolfram.com/language/ref/NestWhile.html>`_


:code:`NestWhile` [:math:`f`, :math:`expr`, :math:`test`]
    applies a function :math:`f` repeatedly on an expression :math:`expr`, until           applying :math:`test` on the result no longer yields :code:`True` .

:code:`NestWhile` [:math:`f`, :math:`expr`, :math:`test`, :math:`m`]
    supplies the last :math:`m` results to :math:`test` (default value: 1).

:code:`NestWhile` [:math:`f`, :math:`expr`, :math:`test`, All]
    supplies all results gained so far to :math:`test`.





Divide by 2 until the result is no longer an integer:

>>> NestWhile[#/2&, 10000, IntegerQ]

    =
:math:`\frac{625}{2}`



Calculate the sum of third powers of the digits of a number until the
same result appears twice:

>>> NestWhile[Total[IntegerDigits[#]^3] &, 5, UnsameQ, All]

    =
:math:`371`



Print the intermediate results:

>>> NestWhile[Total[IntegerDigits[#]^3] &, 5, (Print[{##}]; UnsameQ[##]) &, All]

    {5}

    {5, 125}

    {5, 125, 134}

    {5, 125, 134, 92}

    {5, 125, 134, 92, 737}

    {5, 125, 134, 92, 737, 713}

    {5, 125, 134, 92, 737, 713, 371}

    {5, 125, 134, 92, 737, 713, 371, 371}

    =
:math:`371`


