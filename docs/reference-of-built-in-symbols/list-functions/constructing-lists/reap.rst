Reap
====

`WMA link <https://reference.wolfram.com/language/ref/Reap.html>`_


:code:`Reap` [:math:`expr`]
    gives the result of evaluating :math:`expr`, together with all values           sown during this evaluation. Values sown with different tags           are given in different lists.

:code:`Reap` [:math:`expr`, :math:`pattern`]
    only yields values sown with a tag matching :math:`pattern`.
    :code:`Reap[:math:`expr`]`  is equivalent to :code:`Reap[:math:`expr`, _]` .

:code:`Reap` [:math:`expr`, {:math:`pattern_1`, :math:`pattern_2`, ...}]
    uses multiple patterns.

:code:`Reap` [:math:`expr`, :math:`pattern`, :math:`f`]
    applies :math:`f` on each tag and the corresponding values sown           in the form :code:`:math:`f`[:math:`tag`, {:math:`e_1`, :math:`e_2`, ...}]` .





>>> Reap[Sow[3]; Sow[1]]

    =
:math:`\left\{1,\left\{\left\{3,1\right\}\right\}\right\}`


>>> Reap[Sow[2, {x, x, x}]; Sow[3, x]; Sow[4, y]; Sow[4, 1], {_Symbol, _Integer, x}, f]

    =
:math:`\left\{4,\left\{\left\{f\left[x,\left\{2,2,2,3\right\}\right],f\left[y,\left\{4\right\}\right]\right\},\left\{f\left[1,\left\{4\right\}\right]\right\},\left\{f\left[x,\left\{2,2,2,3\right\}\right]\right\}\right\}\right\}`



Find the unique elements of a list, keeping their order:

>>> Reap[Sow[Null, {a, a, b, d, c, a}], _, # &][[2]]

    =
:math:`\left\{a,b,d,c\right\}`



Sown values are reaped by the innermost matching :code:`Reap` :

>>> Reap[Reap[Sow[a, x]; Sow[b, 1], _Symbol, Print["Inner: ", #1]&];, _, f]

    Inner: x

    =
:math:`\left\{\text{Null},\left\{f\left[1,\left\{b\right\}\right]\right\}\right\}`



When no value is sown, an empty list is returned:

>>> Reap[x]

    =
:math:`\left\{x,\left\{\right\}\right\}`


