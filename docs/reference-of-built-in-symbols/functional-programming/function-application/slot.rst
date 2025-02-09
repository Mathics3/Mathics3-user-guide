Slot
====

`WMA link <https://reference.wolfram.com/language/ref/Slot.html>`_


:code:`#:math:`n``
    represents the :math:`n`-th argument to a pure function.

:code:`#`
    is short-hand for :code:`#1` .

:code:`#0`
    represents the pure function itself.





>>> #

    =
:math:`\text{\#1}`



Unused arguments are simply ignored:

>>> {#1, #2, #3}&[1, 2, 3, 4, 5]

    =
:math:`\left\{1,2,3\right\}`



Recursive pure functions can be written using :code:`#0` :

>>> If[#1<=1, 1, #1 #0[#1-1]]& [10]

    =
:math:`3628800`


