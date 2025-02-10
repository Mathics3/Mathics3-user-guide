BinaryRead
==========

`WMA link <https://reference.wolfram.com/language/ref/BinaryRead.html>`_


:code:`BinaryRead` [:math:`stream`]
    reads one byte from the stream as an integer from 0 to 255.

:code:`BinaryRead` [:math:`stream`, :math:`type`]
    reads one object of specified type from the stream.

:code:`BinaryRead` [:math:`stream`, {:math:`type_1`, :math:`type_2`, ...}]
    reads a sequence of objects of specified types.





>>> strm = OpenWrite[BinaryFormat -> True]

    =
:math:`\text{OutputStream}\left[\text{/tmp/tmpspra5wta},3\right]`


>>> BinaryWrite[strm, {97, 98, 99}]

    =
:math:`\text{OutputStream}\left[\text{/tmp/tmpspra5wta},3\right]`


>>> Close[strm];


>>> strm = OpenRead[%, BinaryFormat -> True]

    =
:math:`\text{InputStream}\left[\text{/tmp/tmpspra5wta},3\right]`


>>> BinaryRead[strm, {"Character8", "Character8", "Character8"}]

    =
:math:`\left\{\text{a},\text{b},\text{c}\right\}`


>>> DeleteFile[Close[strm]];


