StringReplace
=============

`WMA link <https://reference.wolfram.com/language/ref/StringReplace.html>`_


:code:`StringReplace` [":math:`string`", ":math:`a`"->":math:`b`"]
    replaces each occurrence of :math:`old` with :math:`new` in :math:`string`.

:code:`StringReplace` [":math:`string`", {":math:`s_1`"->":math:`sp_1`", ":math:`s_2`"->":math:`sp_2`"}]
    performs multiple replacements of each :math:`si` by the
    corresponding :math:`spi` in :math:`string`.

:code:`StringReplace` [":math:`string`", :math:`srules`, :math:`n`]
    only performs the first :math:`n` replacements.

:code:`StringReplace` [{":math:`string_1`", ":math:`string_2`", ...}, :math:`srules`]
    performs the replacements specified by :math:`srules` on a list
    of strings.





StringReplace replaces all occurrences of one substring with another:

>>> StringReplace["xyxyxyyyxxxyyxy", "xy" -> "A"]
    =

:math:`\text{AAAyyxxAyA}`



Multiple replacements can be supplied:

>>> StringReplace["xyzwxyzwxxyzxyzw", {"xyz" -> "A", "w" -> "BCD"}]
    =

:math:`\text{ABCDABCDxAABCD}`



Only replace the first 2 occurrences:

>>> StringReplace["xyxyxyyyxxxyyxy", "xy" -> "A", 2]
    =

:math:`\text{AAxyyyxxxyyxy}`



Also works for multiple rules:

>>> StringReplace["abba", {"a" -> "A", "b" -> "B"}, 2]
    =

:math:`\text{ABba}`



StringReplace acts on lists of strings too:

>>> StringReplace[{"xyxyxxy", "yxyxyxxxyyxy"}, "xy" -> "A"]
    =

:math:`\left\{\text{AAxA},\text{yAAxxAyA}\right\}`



StringReplace also can be used as an operator:

>>> StringReplace["y" -> "ies"]["city"]
    =

:math:`\text{cities}`


