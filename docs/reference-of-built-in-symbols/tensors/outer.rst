Outer
=====

`Outer product <https://en.wikipedia.org/wiki/Outer_product>`_     (`WMA link <https://reference.wolfram.com/language/ref/Outer.html>`_)


:code:`Outer` [:math:`f`, :math:`x`, :math:`y`]
    computes a generalised outer product of :math:`x` and :math:`y`, using the function :math:`f` in place of multiplication.





>>> Outer[f, {a, b}, {1, 2, 3}]
    =

:math:`\left\{\left\{f\left[a,1\right],f\left[a,2\right],f\left[a,3\right]\right\},\left\{f\left[b,1\right],f\left[b,2\right],f\left[b,3\right]\right\}\right\}`



Outer product of two matrices:

>>> Outer[Times, {{a, b}, {c, d}}, {{1, 2}, {3, 4}}]
    =

:math:`\left\{\left\{\left\{\left\{a,2 a\right\},\left\{3 a,4 a\right\}\right\},\left\{\left\{b,2 b\right\},\left\{3 b,4 b\right\}\right\}\right\},\left\{\left\{\left\{c,2 c\right\},\left\{3 c,4 c\right\}\right\},\left\{\left\{d,2 d\right\},\left\{3 d,4 d\right\}\right\}\right\}\right\}`



Outer product of two sparse arrays:

>>> Outer[Times, SparseArray[{{1, 2} -> a, {2, 1} -> b}], SparseArray[{{1, 2} -> c, {2, 1} -> d}]]
    =

:math:`\text{SparseArray}\left[\text{Automatic},\left\{2,2,2,2\right\},0,\left\{\left\{1,2,1,2\right\}->a c,\left\{1,2,2,1\right\}->a d,\left\{2,1,1,2\right\}->b c,\left\{2,1,2,1\right\}->b d\right\}\right]`



:code:`Outer`  of multiple lists:

>>> Outer[f, {a, b}, {x, y, z}, {1, 2}]
    =

:math:`\left\{\left\{\left\{f\left[a,x,1\right],f\left[a,x,2\right]\right\},\left\{f\left[a,y,1\right],f\left[a,y,2\right]\right\},\left\{f\left[a,z,1\right],f\left[a,z,2\right]\right\}\right\},\left\{\left\{f\left[b,x,1\right],f\left[b,x,2\right]\right\},\left\{f\left[b,y,1\right],f\left[b,y,2\right]\right\},\left\{f\left[b,z,1\right],f\left[b,z,2\right]\right\}\right\}\right\}`



:code:`Outer`  converts input sparse arrays to lists if f=!=Times, or if the input is a mixture of sparse arrays and lists:

>>> Outer[f, SparseArray[{{1, 2} -> a, {2, 1} -> b}], SparseArray[{{1, 2} -> c, {2, 1} -> d}]]
    =

:math:`\left\{\left\{\left\{\left\{f\left[0,0\right],f\left[0,c\right]\right\},\left\{f\left[0,d\right],f\left[0,0\right]\right\}\right\},\left\{\left\{f\left[a,0\right],f\left[a,c\right]\right\},\left\{f\left[a,d\right],f\left[a,0\right]\right\}\right\}\right\},\left\{\left\{\left\{f\left[b,0\right],f\left[b,c\right]\right\},\left\{f\left[b,d\right],f\left[b,0\right]\right\}\right\},\left\{\left\{f\left[0,0\right],f\left[0,c\right]\right\},\left\{f\left[0,d\right],f\left[0,0\right]\right\}\right\}\right\}\right\}`


>>> Outer[Times, SparseArray[{{1, 2} -> a, {2, 1} -> b}], {c, d}]
    =

:math:`\left\{\left\{\left\{0,0\right\},\left\{a c,a d\right\}\right\},\left\{\left\{b c,b d\right\},\left\{0,0\right\}\right\}\right\}`



Arrays can be ragged:

>>> Outer[Times, {{1, 2}}, {{a, b}, {c, d, e}}]
    =

:math:`\left\{\left\{\left\{\left\{a,b\right\},\left\{c,d,e\right\}\right\},\left\{\left\{2 a,2 b\right\},\left\{2 c,2 d,2 e\right\}\right\}\right\}\right\}`



Word combinations:

>>> Outer[StringJoin, {"", "re", "un"}, {"cover", "draw", "wind"}, {"", "ing", "s"}] // InputForm
    =

:math:`\left\{\left\{\left\{\text{\`{}\`{}cover''}, \text{\`{}\`{}covering''}, \text{\`{}\`{}covers''}\right\}, \left\{\text{\`{}\`{}draw''}, \text{\`{}\`{}drawing''}, \text{\`{}\`{}draws''}\right\}, \left\{\text{\`{}\`{}wind''}, \text{\`{}\`{}winding''}, \text{\`{}\`{}winds''}\right\}\right\}, \left\{\left\{\text{\`{}\`{}recover''}, \text{\`{}\`{}recovering''}, \text{\`{}\`{}recovers''}\right\}, \left\{\text{\`{}\`{}redraw''}, \text{\`{}\`{}redrawing''}, \text{\`{}\`{}redraws''}\right\}, \left\{\text{\`{}\`{}rewind''}, \text{\`{}\`{}rewinding''}, \text{\`{}\`{}rewinds''}\right\}\right\}, \left\{\left\{\text{\`{}\`{}uncover''}, \text{\`{}\`{}uncovering''}, \text{\`{}\`{}uncovers''}\right\}, \left\{\text{\`{}\`{}undraw''}, \text{\`{}\`{}undrawing''}, \text{\`{}\`{}undraws''}\right\}, \left\{\text{\`{}\`{}unwind''}, \text{\`{}\`{}unwinding''}, \text{\`{}\`{}unwinds''}\right\}\right\}\right\}`



Compositions of trigonometric functions:

>>> trigs = Outer[Composition, {Sin, Cos, Tan}, {ArcSin, ArcCos, ArcTan}]
    =

:math:`\left\{\left\{\text{Composition}\left[\text{Sin},\text{ArcSin}\right],\text{Composition}\left[\text{Sin},\text{ArcCos}\right],\text{Composition}\left[\text{Sin},\text{ArcTan}\right]\right\},\left\{\text{Composition}\left[\text{Cos},\text{ArcSin}\right],\text{Composition}\left[\text{Cos},\text{ArcCos}\right],\text{Composition}\left[\text{Cos},\text{ArcTan}\right]\right\},\left\{\text{Composition}\left[\text{Tan},\text{ArcSin}\right],\text{Composition}\left[\text{Tan},\text{ArcCos}\right],\text{Composition}\left[\text{Tan},\text{ArcTan}\right]\right\}\right\}`



Evaluate at 0:

>>> Map[#[0] &, trigs, {2}]
    =

:math:`\left\{\left\{0,1,0\right\},\left\{1,0,1\right\},\left\{0,\text{ComplexInfinity},0\right\}\right\}`


