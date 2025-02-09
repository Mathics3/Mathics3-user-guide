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

    =
:math:`\left\{\left\{4,6\right\},\left\{9,11\right\},\left\{15,17\right\},\left\{18,20\right\}\right\}`


>>> StringPosition["123ABCxyABCzzzABCABC", "ABC", 2]

    =
:math:`\left\{\left\{4,6\right\},\left\{9,11\right\}\right\}`



:code:`StringPosition`  can be useful for searching through text.

>>> data = Import["ExampleData/EinsteinSzilLetter.txt", CharacterEncoding->"UTF8"];


>>> StringPosition[data, "uranium"]

    =
:math:`\left\{\left\{299,305\right\},\left\{870,876\right\},\left\{1538,1544\right\},\left\{1671,1677\right\},\left\{2300,2306\right\},\left\{2784,2790\right\},\left\{3093,3099\right\}\right\}`


