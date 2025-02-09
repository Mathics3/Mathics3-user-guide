BinaryWrite
===========

`WMA link <https://reference.wolfram.com/language/ref/BinaryWrite.html>`_


:code:`BinaryWrite` [:math:`channel`, :math:`b`]
    writes a single byte given as an integer from 0 to 255.

:code:`BinaryWrite` [:math:`channel`, {b1, b2, ...}]
    writes a sequence of byte.

:code:`BinaryWrite` [:math:`channel`, "string"]
    writes the raw characters in a string.

:code:`BinaryWrite` [:math:`channel`, :math:`x`, :math:`type`]
    writes :math:`x` as the specified type.

:code:`BinaryWrite` [:math:`channel`, {:math:`x_1`, :math:`x_2`, ...}, :math:`type`]
    writes a sequence of objects as the specified type.

:code:`BinaryWrite` [:math:`channel`, {:math:`x_1`, :math:`x_2`, ...}, {:math:`type_1`, :math:`type_2`, ...}]
    writes a sequence of objects using a sequence of specified types.





>>> strm = OpenWrite[BinaryFormat -> True]

    =
:math:`\text{OutputStream}\left[\text{/tmp/tmpyb77d55y},3\right]`


>>> BinaryWrite[strm, {39, 4, 122}]

    =
:math:`\text{OutputStream}\left[\text{/tmp/tmpyb77d55y},3\right]`


>>> Close[strm];


>>> strm = OpenRead[%, BinaryFormat -> True]

    =
:math:`\text{InputStream}\left[\text{/tmp/tmpyb77d55y},3\right]`


>>> BinaryRead[strm]

    =
:math:`39`


>>> BinaryRead[strm, "Byte"]

    =
:math:`4`


>>> BinaryRead[strm, "Character8"]

    =
:math:`\text{z}`


>>> DeleteFile[Close[strm]];



Write a String

>>> strm = OpenWrite[BinaryFormat -> True]

    =
:math:`\text{OutputStream}\left[\text{/tmp/tmpqdesctaf},3\right]`


>>> BinaryWrite[strm, "abc123"]

    =
:math:`\text{OutputStream}\left[\text{/tmp/tmpqdesctaf},3\right]`


>>> pathname = Close[%]

    =
:math:`\text{/tmp/tmpqdesctaf}`



Read as Bytes

>>> strm = OpenRead[%, BinaryFormat -> True]

    =
:math:`\text{InputStream}\left[\text{/tmp/tmpqdesctaf},3\right]`


>>> BinaryRead[strm, {"Character8", "Character8", "Character8", "Character8", "Character8", "Character8", "Character8"}]

    =
:math:`\left\{\text{a},\text{b},\text{c},\text{1},\text{2},\text{3},\text{EndOfFile}\right\}`


>>> pathname = Close[strm]

    =
:math:`\text{/tmp/tmpqdesctaf}`



Read as Characters

>>> strm = OpenRead[%, BinaryFormat -> True]

    =
:math:`\text{InputStream}\left[\text{/tmp/tmpqdesctaf},3\right]`


>>> BinaryRead[strm, {"Byte", "Byte", "Byte", "Byte", "Byte", "Byte", "Byte"}]

    =
:math:`\left\{97,98,99,49,50,51,\text{EndOfFile}\right\}`


>>> DeleteFile[Close[strm]];



Write Type

>>> strm = OpenWrite[BinaryFormat -> True]

    =
:math:`\text{OutputStream}\left[\text{/tmp/tmpt498zf0g},3\right]`


>>> BinaryWrite[strm, 97, "Byte"]

    =
:math:`\text{OutputStream}\left[\text{/tmp/tmpt498zf0g},3\right]`


>>> BinaryWrite[strm, {97, 98, 99}, {"Byte", "Byte", "Byte"}]

    =
:math:`\text{OutputStream}\left[\text{/tmp/tmpt498zf0g},3\right]`


>>> DeleteFile[Close[%]];


