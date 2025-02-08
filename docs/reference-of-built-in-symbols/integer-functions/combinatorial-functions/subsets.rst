Subsets
=======

`Subset <https://en.wikipedia.org/wiki/Subset>`_ (`WMA link <https://reference.wolfram.com/language/ref/Subsets.html>`_)


:code:`Subsets` [:math:`list`]
    finds a list of all possible subsets of :math:`list`.

:code:`Subsets` [:math:`list`, :math:`n`]
    finds a list of all possible subsets containing at most :math:`n` elements.

:code:`Subsets` [:math:`list`, {:math:`n`}]
    finds a list of all possible subsets containing exactly :math:`n` elements.

:code:`Subsets` [:math:`list`, {:math:`min`, :math:`max`}]
    finds a list of all possible subsets containing between :math:`min` and           :math:`max` elements.

:code:`Subsets` [:math:`list`, :math:`spec`, :math:`n`]
    finds a list of the first :math:`n` possible subsets.

:code:`Subsets` [:math:`list`, :math:`spec`, {:math:`n`}]
    finds the :math:`n`-th possible subset.





All possible subsets (power set):

>>> Subsets[{a, b, c}]
    =

:math:`\left\{\left\{\right\},\left\{a\right\},\left\{b\right\},\left\{c\right\},\left\{a,b\right\},\left\{a,c\right\},\left\{b,c\right\},\left\{a,b,c\right\}\right\}`



All possible subsets containing up to 2 elements:

>>> Subsets[{a, b, c, d}, 2]
    =

:math:`\left\{\left\{\right\},\left\{a\right\},\left\{b\right\},\left\{c\right\},\left\{d\right\},\left\{a,b\right\},\left\{a,c\right\},\left\{a,d\right\},\left\{b,c\right\},\left\{b,d\right\},\left\{c,d\right\}\right\}`



Subsets containing exactly 2 elements:

>>> Subsets[{a, b, c, d}, {2}]
    =

:math:`\left\{\left\{a,b\right\},\left\{a,c\right\},\left\{a,d\right\},\left\{b,c\right\},\left\{b,d\right\},\left\{c,d\right\}\right\}`



The first 5 subsets containing 3 elements:

>>> Subsets[{a, b, c, d, e}, {3}, 5]
    =

:math:`\left\{\left\{a,b,c\right\},\left\{a,b,d\right\},\left\{a,b,e\right\},\left\{a,c,d\right\},\left\{a,c,e\right\}\right\}`



All subsets with even length:

>>> Subsets[{a, b, c, d}, {0, 4, 2}]
    =

:math:`\left\{\left\{\right\},\left\{a,b\right\},\left\{a,c\right\},\left\{a,d\right\},\left\{b,c\right\},\left\{b,d\right\},\left\{c,d\right\},\left\{a,b,c,d\right\}\right\}`



The 25th subset:

>>> Subsets[Range[5], All, {25}]
    =

:math:`\left\{\left\{2,4,5\right\}\right\}`



The odd-numbered subsets of {:math:`a`,:math:`b`,:math:`c`,:math:`d`} in reverse order:

>>> Subsets[{a, b, c, d}, All, {15, 1, -2}]
    =

:math:`\left\{\left\{b,c,d\right\},\left\{a,b,d\right\},\left\{c,d\right\},\left\{b,c\right\},\left\{a,c\right\},\left\{d\right\},\left\{b\right\},\left\{\right\}\right\}`


