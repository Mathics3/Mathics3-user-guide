IntegerPartitions
=================

`Integer partition <https://en.wikipedia.org/wiki/Integer_partition>`_ (`SymPy <https://docs.sympy.org/latest/modules/utilities/iterables.html#sympy.utilities.iterables.ordered_partitions>`_, `WMA <https://reference.wolfram.com/language/ref/IntegerPartitions.html>`_)


:code:`IntegerPartitions` [:math:`n`]
    lists all possible ways to partition integer :math:`n` into smaller integers.

:code:`IntegerPartitions` [:math:`n`, :math:`k`]
    lists all partitions into at most :math:`k` integers.

:code:`IntegerPartitions` [:math:`n`, {:math:`k`}]
    lists all partitions with exactly :math:`k` integers.

:code:`IntegerPartitions` [:math:`n`, {:math:`k_{min}`, :math:`k_{max}`}]
    lists partitions between :math:`k_{min}` and :math:`k_{max}` integers.

:code:`IntegerPartitions` [:math:`n`, :math:`kspec`, {:math:`s_1`, :math:`s_2`, ...}]
    lists partitions involving only the :math:`s_i`.





All partitions of positive integers that add to 5:

>>> IntegerPartitions[5]
    =

:math:`\left\{\left\{5\right\},\left\{4,1\right\},\left\{3,2\right\},\left\{3,1,1\right\},\left\{2,2,1\right\},\left\{2,1,1,1\right\},\left\{1,1,1,1,1\right\}\right\}`



Limit the above to just the first 3 elements:

>>> IntegerPartitions[5, All, All, 3]
    =

:math:`\left\{\left\{5\right\},\left\{4,1\right\},\left\{3,2\right\}\right\}`



Partitions of 5 with at most 3 integers:

>>> IntegerPartitions[5, 3]
    =

:math:`\left\{\left\{5\right\},\left\{4,1\right\},\left\{3,2\right\},\left\{3,1,1\right\},\left\{2,2,1\right\}\right\}`



Partitions of 5 with exactly 3 integers; this is a subset of "at most 3" above:

>>> IntegerPartitions[5, {3}]
    =

:math:`\left\{\left\{3,1,1\right\},\left\{2,2,1\right\}\right\}`



Partitions of 5 that involve only integers 1, and 2:

>>> IntegerPartitions[5, All, {1, 2}]
    =

:math:`\left\{\left\{2,2,1\right\},\left\{2,1,1,1\right\},\left\{1,1,1,1,1\right\}\right\}`



Partitions of 4 with exactly 2 elements and involve only integers -1, 0, 1, 4, and 5:

>>> IntegerPartitions[4, {2}, {-1, 0, 1, 4, 5}]
    =

:math:`\left\{\left\{5,-1\right\},\left\{4,0\right\}\right\}`


