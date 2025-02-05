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
  = OutputStream[...]
>>> BinaryWrite[strm, {39, 4, 122}]
  = OutputStream[...]
>>> Close[strm];

>>> strm = OpenRead[%, BinaryFormat -> True]
  = InputStream[...]
>>> BinaryRead[strm]
  = 39
>>> BinaryRead[strm, "Byte"]
  = 4
>>> BinaryRead[strm, "Character8"]
  = z
>>> DeleteFile[Close[strm]];


Write a String

>>> strm = OpenWrite[BinaryFormat -> True]
  = OutputStream[...]
>>> BinaryWrite[strm, "abc123"]
  = OutputStream[...]
>>> pathname = Close[%]
  = ...

Read as Bytes

>>> strm = OpenRead[%, BinaryFormat -> True]
  = InputStream[...]
>>> BinaryRead[strm, {"Character8", "Character8", "Character8", "Character8", "Character8", "Character8", "Character8"}]
  = {a, b, c, 1, 2, 3, EndOfFile}
>>> pathname = Close[strm]
  = ...

Read as Characters

>>> strm = OpenRead[%, BinaryFormat -> True]
  = InputStream[...]
>>> BinaryRead[strm, {"Byte", "Byte", "Byte", "Byte", "Byte", "Byte", "Byte"}]
  = {97, 98, 99, 49, 50, 51, EndOfFile}
>>> DeleteFile[Close[strm]];


Write Type

>>> strm = OpenWrite[BinaryFormat -> True]
  = OutputStream[...]
>>> BinaryWrite[strm, 97, "Byte"]
  = OutputStream[...]
>>> BinaryWrite[strm, {97, 98, 99}, {"Byte", "Byte", "Byte"}]
  = OutputStream[...]
>>> DeleteFile[Close[%]];

