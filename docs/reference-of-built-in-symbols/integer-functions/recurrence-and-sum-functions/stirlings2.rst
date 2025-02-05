StirlingS2
==========

`Stirling numbers of second kind <https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind>`_ (`WMA link <https://reference.wolfram.com/language/ref/StirlingS2.html>`_)


:code:`StirlingS2` [:math:`n`, :math:`m`]
    gives the Stirling number of the second kind. Returns the number of ways       of partitioning a set of :math:`n` elements into :math:`m` non empty subsets.





>>> Table[StirlingS2[10, m], {m, 10}]
  = {1, 511, 9330, 34105, 42525, 22827, 5880, 750, 45, 1}
