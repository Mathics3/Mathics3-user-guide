Names
=====

`WMA link <https://reference.wolfram.com/language/ref/Names.html>`_

:code:`Names` [":math:`pattern`"]
    returns the list of names matching :math:`pattern`.





>>> Names["List"]
  = {List}

The wildcard :code:`*`  matches any character:

>>> Names["List*"]
  = {List, ListLinePlot, ListLogPlot, ListPlot, ListQ, ListStepPlot, Listable}

The wildcard :code:`@`  matches only lowercase characters:

>>> Names["List@"]
  = {Listable}
>>> x = 5;

>>> Names["Global`*"]
  = {x}

The number of built-in symbols:

>>> Length[Names["System`*"]]
  = ...
