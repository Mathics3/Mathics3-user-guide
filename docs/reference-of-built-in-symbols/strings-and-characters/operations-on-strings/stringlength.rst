StringLength
============

`WMA link <https://reference.wolfram.com/language/ref/StringLength.html>`_


:code:`StringLength` [":math:`string`"]
    gives the length of :math:`string`.





>>> StringLength["abc"]

    =
:math:`3`



:code:`StringLength`  is listable:

>>> StringLength[{"a", "bc"}]

    =
:math:`\left\{1,2\right\}`


>>> StringLength[x]

    StringLength::string String expected.

    =
:math:`\text{StringLength}\left[x\right]`


