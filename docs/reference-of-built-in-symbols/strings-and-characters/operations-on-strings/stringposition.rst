StringPosition
==============

`WMA link <https://reference.wolfram.com/language/ref/StringPosition.html>`_


:code:`StringPosition` [":math:`string`", :math:`patt`]
    gives a list of starting and ending positions where :math:`patt` matches ":math:`string`".

:code:`StringPosition` [":math:`string`", :math:`patt`, :math:`n`]
    returns the first :math:`n` matches only.

:code:`StringPosition` [":math:`string`", {:math:`patt_1`, :math:`patt_2`, ...}, :math:`n`]
    matches multiple patterns.

:code:`StringPosition` [{:math:`s_1`, :math:`s_2`, ...}, :math:`patt`]
    returns a list of matches for multiple strings.





>>> StringPosition["123ABCxyABCzzzABCABC", "ABC"]
  = {{4, 6}, {9, 11}, {15, 17}, {18, 20}}
>>> StringPosition["123ABCxyABCzzzABCABC", "ABC", 2]
  = {{4, 6}, {9, 11}}

:code:`StringPosition`  can be useful for searching through text.

>>> data = Import["ExampleData/EinsteinSzilLetter.txt", CharacterEncoding->"UTF8"];

>>> StringPosition[data, "uranium"]
  = {{299, 305}, {870, 876}, {1538, 1544}, {1671, 1677}, {2300, 2306}, {2784, 2790}, {3093, 3099}}
