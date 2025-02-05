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
  = {1, {{3, 1}}}
>>> Reap[Sow[2, {x, x, x}]; Sow[3, x]; Sow[4, y]; Sow[4, 1], {_Symbol, _Integer, x}, f]
  = {4, {{f[x, {2, 2, 2, 3}], f[y, {4}]}, {f[1, {4}]}, {f[x, {2, 2, 2, 3}]}}}

Find the unique elements of a list, keeping their order:

>>> Reap[Sow[Null, {a, a, b, d, c, a}], _, # &][[2]]
  = {a, b, d, c}

Sown values are reaped by the innermost matching :code:`Reap` :

>>> Reap[Reap[Sow[a, x]; Sow[b, 1], _Symbol, Print["Inner: ", #1]&];, _, f]
  = {Null, {f[1, {b}]}}

When no value is sown, an empty list is returned:

>>> Reap[x]
  = {x, {}}
