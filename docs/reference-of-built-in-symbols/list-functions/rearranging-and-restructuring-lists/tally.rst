Tally
=====

`WMA link <https://reference.wolfram.com/language/ref/Tally.html>`_


:code:`Tally` [:math:`list`]
    counts and returns the number of occurrences of objects and returns           the result as a list of pairs {object, count}.

:code:`Tally` [:math:`list`, :math:`test`]
    counts the number of occurrences of objects and uses :math:`test` to           determine if two objects should be counted in the same bin.





>>> Tally[{a, b, c, b, a}]
  = {{a, 2}, {b, 2}, {c, 1}}

Tally always returns items in the order as they first appear in :math:`list`:

>>> Tally[{b, b, a, a, a, d, d, d, d, c}]
  = {{b, 2}, {a, 3}, {d, 4}, {c, 1}}
