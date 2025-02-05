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
  = abc123
>>> Read[stream, String]
  = EndOfFile
>>> Close[stream];

>>> stream = StringToStream["abc 123"];

>>> Read[stream, Word]
  = abc
>>> Read[stream, Word]
  = 123
>>> Read[stream, Word]
  = EndOfFile
>>> Close[stream];

>>> stream = StringToStream["123, 4"];

>>> Read[stream, Number]
  = 123
>>> Read[stream, Number]
  = 4
>>> Read[stream, Number]
  = EndOfFile
>>> Close[stream];

>>> stream = StringToStream["2+2\n2+3"];


:code:`Read`  with a :code:`Hold[Expression]`  returns the expression it reads unevaluated so it can be later inspected and evaluated:

>>> Read[stream, Hold[Expression]]
  = Hold[2 + 2]
>>> Read[stream, Expression]
  = 5
>>> Close[stream];


Reading a comment, a non-expression, will return :code:`Hold[Null]` 

>>> stream = StringToStream["(* ::Package:: *)"];

>>> Read[stream, Hold[Expression]]
  = Hold[Null]
>>> Close[stream];

>>> stream = StringToStream["123 abc"];

>>> Read[stream, {Number, Word}]
  = {123, abc}
>>> Read[stream, {Number, Word}]
  = EndOfFile
>>> Close[stream];


Multiple lines:

>>> stream = StringToStream["\"Tengo una\nvaca lechera.\""]; Read[stream]
  = Tengo una
    vaca lechera.
