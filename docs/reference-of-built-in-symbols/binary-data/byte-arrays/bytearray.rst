ByteArray
=========

`WMA link <https://reference.wolfram.com/language/ref/ByteArray.html>`_


:code:`ByteArray` [{:math:`b_1`, :math:`b_2`, ...}]
    Represents a sequence of Bytes :math:`b_1`, :math:`b_2`, ...

:code:`ByteArray` [":math:`string`"]
    Constructs a byte array where bytes comes from decode a b64-encoded String





>>> A=ByteArray[{1, 25, 3}]

    =
:math:`\text{ByteArray}\left[\text{<3>}\right]`


>>> A[[2]]

    =
:math:`25`


>>> Normal[A]

    =
:math:`\left\{1,25,3\right\}`


>>> ToString[A]

    =
:math:`\text{ByteArray[<3>]}`


>>> ByteArray["ARkD"]

    =
:math:`\text{ByteArray}\left[\text{<3>}\right]`


>>> B=ByteArray["asy"]

    ByteArray::lend The first argument in Bytearray[asy] should be a B64 encoded string or a vector of integers.

    =
:math:`\text{\$Failed}`


