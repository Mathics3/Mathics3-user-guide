FileHash
========

`WMA link <https://reference.wolfram.com/language/ref/FileHash.html>`_


:code:`FileHash` [:math:`file`]
    returns an integer hash for the given :math:`file`.

:code:`FileHash` [:math:`file`, :math:`type`]
    returns an integer hash of the specified :math:`type` for the given :math:`file`.

    The types supported are "MD5", "Adler32", "CRC32", "SHA", "SHA224", "SHA256",           "SHA384", and "SHA512".

:code:`FileHash` [:math:`file`, :math:`type`, :math:`format`]
    gives a hash code in the specified format.





>>> FileHash["ExampleData/sunflowers.jpg"]
  = 109937059621979839952736809235486742106
>>> FileHash["ExampleData/sunflowers.jpg", "MD5"]
  = 109937059621979839952736809235486742106
>>> FileHash["ExampleData/sunflowers.jpg", "Adler32"]
  = 1607049478
>>> FileHash["ExampleData/sunflowers.jpg", "SHA256"]
  = 111619807552579450300684600241129773909359865098672286468229443390003894913065
