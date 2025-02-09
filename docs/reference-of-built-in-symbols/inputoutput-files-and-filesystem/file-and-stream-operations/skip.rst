Skip
====

`WMA link <https://reference.wolfram.com/language/ref/Skip.html>`_


:code:`Skip` [:math:`stream`, :math:`type`]
    skips ahead in an input steream by one object of the specified :math:`type`.

:code:`Skip` [:math:`stream`, :math:`type`, :math:`n`]
    skips ahead in an input steream by :math:`n` objects of the specified :math:`type`.





>>> stream = StringToStream["a b c d"];


>>> Read[stream, Word]

    =
:math:`\text{a}`


>>> Skip[stream, Word]


>>> Read[stream, Word]

    =
:math:`\text{c}`


>>> Close[stream];
    = `

>>> stream = StringToStream["a b c d"];


>>> Read[stream, Word]

    =
:math:`\text{a}`


>>> Skip[stream, Word, 2]


>>> Read[stream, Word]

    =
:math:`\text{d}`


>>> Skip[stream, Word]

    =
:math:`\text{EndOfFile}`


>>> Close[stream];
    = `

