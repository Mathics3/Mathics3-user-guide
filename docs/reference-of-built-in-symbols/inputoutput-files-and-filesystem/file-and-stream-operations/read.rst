Read
====

`WMA link <https://reference.wolfram.com/language/ref/Read.html>`_


:code:`Read` [:math:`stream`]
    reads the input stream and returns one expression.

:code:`Read` [:math:`stream`, :math:`type`]
    reads the input stream and returns an object of the given type.

:code:`Read` [:math:`stream`, :math:`type`]
    reads the input stream and returns an object of the given type.

:code:`Read[:math:`stream`, Hold[Expression]]`
    reads the input stream for an Expression and puts it inside :code:`Hold` .





:math:`type` is one of:


- Byte

- Character

- Expression

- HoldExpression

- Number

- Real

- Record

- String

- Word




>>> stream = StringToStream["abc123"];


>>> Read[stream, String]

    =
:math:`\text{abc123}`


>>> Read[stream, String]

    =
:math:`\text{EndOfFile}`


>>> Close[stream];
    = `

>>> stream = StringToStream["abc 123"];


>>> Read[stream, Word]

    =
:math:`\text{abc}`


>>> Read[stream, Word]

    =
:math:`\text{123}`


>>> Read[stream, Word]

    =
:math:`\text{EndOfFile}`


>>> Close[stream];
    = `

>>> stream = StringToStream["123, 4"];


>>> Read[stream, Number]

    =
:math:`123`


>>> Read[stream, Number]

    =
:math:`4`


>>> Read[stream, Number]

    =
:math:`\text{EndOfFile}`


>>> Close[stream];
    = `

>>> stream = StringToStream["2+2\n2+3"];



:code:`Read`  with a :code:`Hold[Expression]`  returns the expression it reads unevaluated so it can be later inspected and evaluated:

>>> Read[stream, Hold[Expression]]

    =
:math:`\text{Hold}\left[2+2\right]`


>>> Read[stream, Expression]

    =
:math:`5`


>>> Close[stream];
    = `


Reading a comment, a non-expression, will return :code:`Hold[Null]` 

>>> stream = StringToStream["(* ::Package:: *)"];


>>> Read[stream, Hold[Expression]]

    =
:math:`\text{Hold}\left[\text{Null}\right]`


>>> Close[stream];
    = `

>>> stream = StringToStream["123 abc"];


>>> Read[stream, {Number, Word}]

    =
:math:`\left\{123,\text{abc}\right\}`


>>> Read[stream, {Number, Word}]

    =
:math:`\text{EndOfFile}`


>>> Close[stream];
    = `


Multiple lines:

>>> stream = StringToStream["\"Tengo una\nvaca lechera.\""]; Read[stream]

    =

.. math::
    \text{Tengo una\newline
    vaca lechera.}



