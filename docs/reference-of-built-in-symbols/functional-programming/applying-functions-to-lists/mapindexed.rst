MapIndexed
==========

`WMA link <https://reference.wolfram.com/language/ref/MapIndexed.html>`_


:code:`MapIndexed` [:math:`f`, :math:`expr`]
    applies :math:`f` to each part on the first level of :math:`expr`, including the part positions in the call to :math:`f`.

:code:`MapIndexed` [:math:`f`, :math:`expr`, :math:`levelspec`]
    applies :math:`f` to each level specified by :math:`levelspec` of :math:`expr`.





>>> MapIndexed[f, {a, b, c}]
    =

:math:`\left\{f\left[a,\left\{1\right\}\right],f\left[b,\left\{2\right\}\right],f\left[c,\left\{3\right\}\right]\right\}`



Include heads (index 0):

>>> MapIndexed[f, {a, b, c}, Heads->True]
    =

:math:`f\left[\text{List},\left\{0\right\}\right]\left[f\left[a,\left\{1\right\}\right],f\left[b,\left\{2\right\}\right],f\left[c,\left\{3\right\}\right]\right]`



Map on levels 0 through 1 (outer expression gets index :code:`{}` ):

>>> MapIndexed[f, a + b + c * d, {0, 1}]
    =

:math:`f\left[f\left[a,\left\{1\right\}\right]+f\left[b,\left\{2\right\}\right]+f\left[c d,\left\{3\right\}\right],\left\{\right\}\right]`



Get the positions of atoms in an expression (convert operations to :code:`List`  first
to disable :code:`Listable`  functions):

>>> expr = a + b * f[g] * c ^ e;


>>> listified = Apply[List, expr, {0, Infinity}];


>>> MapIndexed[#2 &, listified, {-1}]
    =

:math:`\left\{\left\{1\right\},\left\{\left\{2,1\right\},\left\{\left\{2,2,1\right\}\right\},\left\{\left\{2,3,1\right\},\left\{2,3,2\right\}\right\}\right\}\right\}`



Replace the heads with their positions, too:

>>> MapIndexed[#2 &, listified, {-1}, Heads -> True]
    =

:math:`\left\{0\right\}\left[\left\{1\right\},\left\{2,0\right\}\left[\left\{2,1\right\},\left\{2,2,0\right\}\left[\left\{2,2,1\right\}\right],\left\{2,3,0\right\}\left[\left\{2,3,1\right\},\left\{2,3,2\right\}\right]\right]\right]`



The positions are given in the same format as used by :code:`Extract` .
Thus, mapping :code:`Extract`  on the indices given by :code:`MapIndexed`  re-constructs the original expression:

>>> MapIndexed[Extract[expr, #2] &, listified, {-1}, Heads -> True]
    =

:math:`a+b f\left[g\right] c^e`


