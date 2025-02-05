System`Convert`B64Dump`B64Encode
================================

`WMA link
 <https://reference.wolfram.com/language/ref/B64Encode.html>`_


:code:`System`Convert`B64Dump`B64Encode` [:math:`expr`]
    Encodes :math:`expr` in Base64 coding





>>> System`Convert`B64Dump`B64Encode["Hello world"]
  = SGVsbG8gd29ybGQ=
>>> System`Convert`B64Dump`B64Decode[%]
  = Hello world
>>> System`Convert`B64Dump`B64Encode[Integrate[f[x],{x,0,2}]]
  = SW50ZWdyYXRlW2ZbeF0sIHt4LCAwLCAyfV0=
>>> System`Convert`B64Dump`B64Decode[%]
  = Integrate[f[x], {x, 0, 2}]
