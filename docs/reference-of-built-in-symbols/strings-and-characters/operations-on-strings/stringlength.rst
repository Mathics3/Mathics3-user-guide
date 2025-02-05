StringLength
============

`WMA link <https://reference.wolfram.com/language/ref/StringLength.html>`_


:code:`StringLength` [":math:`string`"]
    gives the length of :math:`string`.





>>> StringLength["abc"]
  = 3

:code:`StringLength`  is listable:

>>> StringLength[{"a", "bc"}]
  = {1, 2}
>>> StringLength[x]
  = StringLength[x]
