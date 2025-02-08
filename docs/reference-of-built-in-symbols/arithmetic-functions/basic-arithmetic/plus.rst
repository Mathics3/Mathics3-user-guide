Plus
====

`Addition <https://en.wikipedia.org/wiki/Addition>`_ (`SymPy <https://docs.sympy.org/latest/modules/core.html#id48>`_, `WMA <https://reference.wolfram.com/language/ref/Plus.html>`_)


:code:`Plus` [:math:`a`, :math:`b`, ...]
    same as

:math:`a` + :math:`b` + ...
    represents the sum of the terms :math:`a`, :math:`b`, ...





>>> 1 + 2
    =

:math:`3`



:code:`Plus`  performs basic simplification of terms:

>>> a + b + a
    =

:math:`2 a+b`


>>> a + a + 3 * a
    =

:math:`5 a`


>>> a + b + 4.5 + a + b + a + 2 + 1.5 b
    =

:math:`6.5+3 a+3.5 b`



Apply :code:`Plus`  on a list to sum up its elements:

>>> Plus @@ {2, 4, 6}
    =

:math:`12`



The sum of the first 1000 integers:

>>> Plus @@ Range[1000]
    =

:math:`500500`



:code:`Plus`  has default value 0:

>>> DefaultValues[Plus]
    =

:math:`\left\{\text{HoldPattern}\left[\text{Default}\left[\text{Plus}\right]\right]\text{:>}0\right\}`


>>> a /. n_. + x_ :> {n, x}
    =

:math:`\left\{0,a\right\}`



The sum of 2 red circles and 3 red circles is...

>>> 2 Graphics[{Red,Disk[]}] + 3 Graphics[{Red,Disk[]}]
    =


.. math::
    5 
    \includegraphics[]{/tmp/tmps4bni88m.png}



