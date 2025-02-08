ExpandAll
=========

`WMA link <https://reference.wolfram.com/language/ref/ExpandAll.html>`_


:code:`ExpandAll` [:math:`expr`]
    expands out negative integer powers and products of sums in :math:`expr`.

:code:`ExpandAll` [:math:`expr`, :math:`target`]
    just expands those parts involving :math:`target`.





>>> ExpandAll[(a + b) ^ 2 / (c + d)^2]
    =

:math:`\frac{a^2}{c^2+2 c d+d^2}+\frac{2 a b}{c^2+2 c d+d^2}+\frac{b^2}{c^2+2 c d+d^2}`



:code:`ExpandAll`  descends into sub expressions

>>> ExpandAll[(a + Sin[x (1 + y)])^2]
    =

:math:`2 a \text{Sin}\left[x+x y\right]+a^2+\text{Sin}\left[x+x y\right]^2`


>>> ExpandAll[Sin[(x+y)^2]]
    =

:math:`\text{Sin}\left[x^2+2 x y+y^2\right]`


>>> ExpandAll[Sin[(x+y)^2], Trig->True]
    =

:math:`\text{Cos}\left[x^2\right] \text{Cos}\left[2 x y\right] \text{Sin}\left[y^2\right]+\text{Cos}\left[x^2\right] \text{Cos}\left[y^2\right] \text{Sin}\left[2 x y\right]+\text{Cos}\left[2 x y\right] \text{Cos}\left[y^2\right] \text{Sin}\left[x^2\right]-\text{Sin}\left[x^2\right] \text{Sin}\left[2 x y\right] \text{Sin}\left[y^2\right]`



:code:`ExpandAll`  also expands heads

>>> ExpandAll[((1 + x)(1 + y))[x]]
    =

:math:`\left(1+x+y+x y\right)\left[x\right]`



:code:`ExpandAll`  can also work in finite fields

>>> ExpandAll[(1 + a) ^ 6 / (x + y)^3, Modulus -> 3]
    =

:math:`\frac{1+2 a^3+a^6}{x^3+y^3}`


