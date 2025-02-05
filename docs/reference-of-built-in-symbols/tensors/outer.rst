Outer
=====

`Outer product <https://en.wikipedia.org/wiki/Outer_product>`_     (`WMA link <https://reference.wolfram.com/language/ref/Outer.html>`_)


:code:`Outer` [:math:`f`, :math:`x`, :math:`y`]
    computes a generalised outer product of :math:`x` and :math:`y`, using the function :math:`f` in place of multiplication.





>>> Outer[f, {a, b}, {1, 2, 3}]
  = {{f[a, 1], f[a, 2], f[a, 3]}, {f[b, 1], f[b, 2], f[b, 3]}}

Outer product of two matrices:

>>> Outer[Times, {{a, b}, {c, d}}, {{1, 2}, {3, 4}}]
  = {{{{a, 2 a}, {3 a, 4 a}}, {{b, 2 b}, {3 b, 4 b}}}, {{{c, 2 c}, {3 c, 4 c}}, {{d, 2 d}, {3 d, 4 d}}}}

Outer product of two sparse arrays:

>>> Outer[Times, SparseArray[{{1, 2} -> a, {2, 1} -> b}], SparseArray[{{1, 2} -> c, {2, 1} -> d}]]
  = SparseArray[Automatic, {2, 2, 2, 2}, 0, {{1, 2, 1, 2} -> a c, {1, 2, 2, 1} -> a d, {2, 1, 1, 2} -> b c, {2, 1, 2, 1} -> b d}]

:code:`Outer`  of multiple lists:

>>> Outer[f, {a, b}, {x, y, z}, {1, 2}]
  = {{{f[a, x, 1], f[a, x, 2]}, {f[a, y, 1], f[a, y, 2]}, {f[a, z, 1], f[a, z, 2]}}, {{f[b, x, 1], f[b, x, 2]}, {f[b, y, 1], f[b, y, 2]}, {f[b, z, 1], f[b, z, 2]}}}

:code:`Outer`  converts input sparse arrays to lists if f=!=Times, or if the input is a mixture of sparse arrays and lists:

>>> Outer[f, SparseArray[{{1, 2} -> a, {2, 1} -> b}], SparseArray[{{1, 2} -> c, {2, 1} -> d}]]
  = {{{{f[0, 0], f[0, c]}, {f[0, d], f[0, 0]}}, {{f[a, 0], f[a, c]}, {f[a, d], f[a, 0]}}}, {{{f[b, 0], f[b, c]}, {f[b, d], f[b, 0]}}, {{f[0, 0], f[0, c]}, {f[0, d], f[0, 0]}}}}
>>> Outer[Times, SparseArray[{{1, 2} -> a, {2, 1} -> b}], {c, d}]
  = {{{0, 0}, {a c, a d}}, {{b c, b d}, {0, 0}}}

Arrays can be ragged:

>>> Outer[Times, {{1, 2}}, {{a, b}, {c, d, e}}]
  = {{{{a, b}, {c, d, e}}, {{2 a, 2 b}, {2 c, 2 d, 2 e}}}}

Word combinations:

>>> Outer[StringJoin, {"", "re", "un"}, {"cover", "draw", "wind"}, {"", "ing", "s"}] // InputForm
  = {{{"cover", "covering", "covers"}, {"draw", "drawing", "draws"}, {"wind", "winding", "winds"}}, {{"recover", "recovering", "recovers"}, {"redraw", "redrawing", "redraws"}, {"rewind", "rewinding", "rewinds"}}, {{"uncover", "uncovering", "uncovers"}, {"undraw", "undrawing", "undraws"}, {"unwind", "unwinding", "unwinds"}}}

Compositions of trigonometric functions:

>>> trigs = Outer[Composition, {Sin, Cos, Tan}, {ArcSin, ArcCos, ArcTan}]
  = {{Composition[Sin, ArcSin], Composition[Sin, ArcCos], Composition[Sin, ArcTan]}, {Composition[Cos, ArcSin], Composition[Cos, ArcCos], Composition[Cos, ArcTan]}, {Composition[Tan, ArcSin], Composition[Tan, ArcCos], Composition[Tan, ArcTan]}}

Evaluate at 0:

>>> Map[#[0] &, trigs, {2}]
  = {{0, 1, 0}, {1, 0, 1}, {0, ComplexInfinity, 0}}
