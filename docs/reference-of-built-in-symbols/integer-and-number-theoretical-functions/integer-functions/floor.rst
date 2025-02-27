Floor
=====

`WMA link <https://reference.wolfram.com/language/ref/Floor.html>`_


:code:`Floor` [:math:`x`]
    gives the greatest integer less than or equal to :math:`x`.

:code:`Floor` [:math:`x`, :math:`a`]
    gives the greatest multiple of :math:`a` less than or equal to :math:`x`.





>>> Floor[10.4]

    =
:math:`10`


>>> Floor[10/3]

    =
:math:`3`


>>> Floor[10]

    =
:math:`10`


>>> Floor[21, 2]

    =
:math:`20`


>>> Floor[2.6, 0.5]

    =
:math:`2.5`


>>> Floor[-10.4]

    =
:math:`-11`



For complex :math:`x`, take the floor of real an imaginary parts.

>>> Floor[1.5 + 2.7 I]

    =
:math:`1+2 I`



For negative :math:`a`, the smallest multiple of :math:`a` greater than or equal to :math:`x`
is returned.

>>> Floor[10.4, -1]

    =
:math:`11`


>>> Floor[-10.4, -1]

    =
:math:`-10`


