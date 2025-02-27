Flat
====

`WMA link <https://reference.wolfram.com/language/ref/Flat.html>`_


:code:`Flat`
    is an attribute that specifies that nested occurrences of         a function should be automatically flattened.





A symbol with the :code:`Flat`  attribute represents an associative     mathematical operation:

>>> SetAttributes[f, Flat]


>>> f[a, f[b, c]]

    =
:math:`f\left[a,b,c\right]`



:code:`Flat`  is taken into account in pattern matching:

>>> f[a, b, c] /. f[a, b] -> d

    =
:math:`f\left[d,c\right]`


