StringJoin
==========

`WMA link <https://reference.wolfram.com/language/ref/StringJoin.html>`_


:code:`StringJoin` [":math:`s_1`", ":math:`s_2`", ...]
    returns the concatenation of the strings :math:`s_1`, :math:`s_2`,  .





>>> StringJoin["a", "b", "c"]
  = abc
>>> "a" <> "b" <> "c" // InputForm
  = "abc"

:code:`StringJoin`  flattens lists out:

>>> StringJoin[{"a", "b"}] // InputForm
  = "ab"
>>> Print[StringJoin[{"Hello", " ", {"world"}}, "!"]]

