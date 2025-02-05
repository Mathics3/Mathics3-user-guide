ToCharacterCode
===============

`WMA link <https://reference.wolfram.com/language/ref/ToCharacterCode.html>`_


:code:`ToCharacterCode` [":math:`string`"]
    converts the string to a list of character codes (Unicode
    codepoints).

:code:`ToCharacterCode` [{":math:`string_1`", ":math:`string_2`", ...}]
    converts a list of strings to character codes.





>>> ToCharacterCode["abc"]
  = {97, 98, 99}
>>> FromCharacterCode[%]
  = abc
>>> ToCharacterCode["\[Alpha]\[Beta]\[Gamma]"]
  = {945, 946, 947}
>>> ToCharacterCode["ä", "UTF8"]
  = {195, 164}
>>> ToCharacterCode["ä", "ISO8859-1"]
  = {228}
>>> ToCharacterCode[{"ab", "c"}]
  = {{97, 98}, {99}}
>>> ToCharacterCode[{"ab", x}]
  = ToCharacterCode[{ab, x}]
>>> ListPlot[ToCharacterCode["plot this string"], Filling -> Axis]
  = -Graphics-
