ToCharacterCode
===============

`WMA link <https://reference.wolfram.com/language/ref/ToCharacterCode.html>`_


:code:`ToCharacterCode` [":math:`string`"]
    converts the string to a list of character codes (Unicode
    codepoints).

:code:`ToCharacterCode` [{":math:`string_1`", ":math:`string_2`", ...}]
    converts a list of strings to character codes.





>>> ToCharacterCode["abc"]
    =

:math:`\left\{97,98,99\right\}`


>>> FromCharacterCode[%]
    =

:math:`\text{abc}`


>>> ToCharacterCode["\[Alpha]\[Beta]\[Gamma]"]
    =

:math:`\left\{945,946,947\right\}`


>>> ToCharacterCode["ä", "UTF8"]
    =

:math:`\left\{195,164\right\}`


>>> ToCharacterCode["ä", "ISO8859-1"]
    =

:math:`\left\{228\right\}`


>>> ToCharacterCode[{"ab", "c"}]
    =

:math:`\left\{\left\{97,98\right\},\left\{99\right\}\right\}`


>>> ToCharacterCode[{"ab", x}]

    ToCharacterCode::strse String or list of strings expected at position 1 in ToCharacterCode[{ab, x}].
    =

:math:`\text{ToCharacterCode}\left[\left\{\text{ab},x\right\}\right]`


>>> ListPlot[ToCharacterCode["plot this string"], Filling -> Axis]
    =

.. image:: tmpxcxbab_h.png
    :align: center



