ByteArray
=========

`WMA link <https://reference.wolfram.com/language/ref/ByteArray.html>`_


:code:`ByteArray` [{:math:`b_1`, :math:`b_2`, ...}]
    Represents a sequence of Bytes :math:`b_1`, :math:`b_2`, ...

:code:`ByteArray` [":math:`string`"]
    Constructs a byte array where bytes comes from decode a b64-encoded String





>>> A=ByteArray[{1, 25, 3}]
  = ByteArray[<3>]
>>> A[[2]]
  = 25
>>> Normal[A]
  = {1, 25, 3}
>>> ToString[A]
  = ByteArray[<3>]
>>> ByteArray["ARkD"]
  = ByteArray[<3>]
>>> B=ByteArray["asy"]
  = $Failed
