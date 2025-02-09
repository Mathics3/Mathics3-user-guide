Names
=====

`WMA link <https://reference.wolfram.com/language/ref/Names.html>`_

:code:`Names` [":math:`pattern`"]
    returns the list of names matching :math:`pattern`.





>>> Names["List"]

    =
:math:`\left\{\text{List}\right\}`



The wildcard :code:`*`  matches any character:

>>> Names["List*"]

    =
:math:`\left\{\text{List},\text{ListLinePlot},\text{ListLogPlot},\text{ListPlot},\text{ListQ},\text{ListStepPlot},\text{Listable}\right\}`



The wildcard :code:`@`  matches only lowercase characters:

>>> Names["List@"]

    =
:math:`\left\{\text{Listable}\right\}`


>>> x = 5;


>>> Names["Global`*"]

    =
:math:`\left\{\text{x}\right\}`



The number of built-in symbols:

>>> Length[Names["System`*"]]

    =
:math:`1497`


