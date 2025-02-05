SplitBy
=======

`WMA link <https://reference.wolfram.com/language/ref/SplitBy.html>`_


:code:`SplitBy` [:math:`list`, :math:`f`]
    splits :math:`list` into collections of consecutive elements
    that give the same result when :math:`f` is applied.





>>> SplitBy[Range[1, 3, 1/3], Round]
  = {{1, 4 / 3}, {5 / 3, 2, 7 / 3}, {8 / 3, 3}}
>>> SplitBy[{1, 2, 1, 1.2}, {Round, Identity}]
  = {{{1}}, {{2}}, {{1}, {1.2}}}
