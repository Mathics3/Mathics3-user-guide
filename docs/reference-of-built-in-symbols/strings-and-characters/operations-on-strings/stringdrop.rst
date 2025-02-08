StringDrop
==========

`WMA link <https://reference.wolfram.com/language/ref/StringDrop.html>`_


:code:`StringDrop` [":math:`string`", :math:`n`]
    gives :math:`string` with the first :math:`n` characters dropped.

:code:`StringDrop` [":math:`string`", -:math:`n`]
    gives :math:`string` with the last :math:`n` characters dropped.

:code:`StringDrop` [":math:`string`", {:math:`n`}]
    gives :math:`string` with the :math:`n`-th character dropped.

:code:`StringDrop` [":math:`string`", {:math:`m`, :math:`n`}]
    gives :math:`string` with the characters :math:`m` through :math:`n` dropped.





>>> StringDrop["abcde", 2]
    =

:math:`\text{cde}`


>>> StringDrop["abcde", -2]
    =

:math:`\text{abc}`


>>> StringDrop["abcde", {2}]
    =

:math:`\text{acde}`


>>> StringDrop["abcde", {2,3}]
    =

:math:`\text{ade}`


>>> StringDrop["abcd",{3,2}]
    =

:math:`\text{abcd}`


>>> StringDrop["abcd",0]
    =

:math:`\text{abcd}`


