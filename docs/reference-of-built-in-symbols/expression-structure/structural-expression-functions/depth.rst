Depth
=====

`WMA link <https://reference.wolfram.com/language/ref/Depth.html>`_


:code:`Depth` [:math:`expr`]
    gives the depth of :math:`expr`.





The depth of an expression is defined as one plus the maximum
number of :code:`Part`  indices required to reach any part of :math:`expr`,
except for heads.

>>> Depth[x]

    =
:math:`1`


>>> Depth[x + y]

    =
:math:`2`


>>> Depth[{{{{x}}}}]

    =
:math:`5`



Complex numbers are atomic, and hence have depth 1:

>>> Depth[1 + 2 I]

    =
:math:`1`



:code:`Depth`  ignores heads:

>>> Depth[f[a, b][c]]

    =
:math:`2`


