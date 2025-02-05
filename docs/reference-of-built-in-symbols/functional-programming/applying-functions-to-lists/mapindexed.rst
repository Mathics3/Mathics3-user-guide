MapIndexed
==========

`WMA link <https://reference.wolfram.com/language/ref/MapIndexed.html>`_


:code:`MapIndexed` [:math:`f`, :math:`expr`]
    applies :math:`f` to each part on the first level of :math:`expr`, including the part positions in the call to :math:`f`.

:code:`MapIndexed` [:math:`f`, :math:`expr`, :math:`levelspec`]
    applies :math:`f` to each level specified by :math:`levelspec` of :math:`expr`.





>>> MapIndexed[f, {a, b, c}]
  = {f[a, {1}], f[b, {2}], f[c, {3}]}

Include heads (index 0):

>>> MapIndexed[f, {a, b, c}, Heads->True]
  = f[List, {0}][f[a, {1}], f[b, {2}], f[c, {3}]]

Map on levels 0 through 1 (outer expression gets index :code:`{}` ):

>>> MapIndexed[f, a + b + c * d, {0, 1}]
  = f[f[a, {1}] + f[b, {2}] + f[c d, {3}], {}]

Get the positions of atoms in an expression (convert operations to :code:`List`  first
to disable :code:`Listable`  functions):

>>> expr = a + b * f[g] * c ^ e;

>>> listified = Apply[List, expr, {0, Infinity}];

>>> MapIndexed[#2 &, listified, {-1}]
  = {{1}, {{2, 1}, {{2, 2, 1}}, {{2, 3, 1}, {2, 3, 2}}}}

Replace the heads with their positions, too:

>>> MapIndexed[#2 &, listified, {-1}, Heads -> True]
  = {0}[{1}, {2, 0}[{2, 1}, {2, 2, 0}[{2, 2, 1}], {2, 3, 0}[{2, 3, 1}, {2, 3, 2}]]]

The positions are given in the same format as used by :code:`Extract` .
Thus, mapping :code:`Extract`  on the indices given by :code:`MapIndexed`  re-constructs the original expression:

>>> MapIndexed[Extract[expr, #2] &, listified, {-1}, Heads -> True]
  = a + b f[g] c ^ e
