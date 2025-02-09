RepeatedNull
============

`WMA link <https://reference.wolfram.com/language/ref/RepeatedNull.html>`_


:code:`RepeatedNull` [:math:`pat`]
    matches zero or more occurrences of :math:`pat`.





>>> a___Integer...//FullForm

    =
:math:`\text{RepeatedNull}\left[\text{Pattern}\left[a, \text{BlankNullSequence}\left[\text{Integer}\right]\right]\right]`


>>> f[x] /. f[x, 0...] -> t

    =
:math:`t`


