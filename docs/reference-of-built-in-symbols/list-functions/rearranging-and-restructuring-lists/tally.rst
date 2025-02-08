Tally
=====

`WMA link <https://reference.wolfram.com/language/ref/Tally.html>`_


:code:`Tally` [:math:`list`]
    counts and returns the number of occurrences of objects and returns           the result as a list of pairs {object, count}.

:code:`Tally` [:math:`list`, :math:`test`]
    counts the number of occurrences of objects and uses :math:`test` to           determine if two objects should be counted in the same bin.





>>> Tally[{a, b, c, b, a}]
    =

:math:`\left\{\left\{a,2\right\},\left\{b,2\right\},\left\{c,1\right\}\right\}`



Tally always returns items in the order as they first appear in :math:`list`:

>>> Tally[{b, b, a, a, a, d, d, d, d, c}]
    =

:math:`\left\{\left\{b,2\right\},\left\{a,3\right\},\left\{d,4\right\},\left\{c,1\right\}\right\}`


