Level
=====

`WMA link <https://reference.wolfram.com/language/ref/Level.html>`_


:code:`Level` [:math:`expr`, :math:`levelspec`]
    gives a list of all subexpressions of :math:`expr` at the
    level(s) specified by :math:`levelspec`.





Level uses standard level specifications:


:math:`n`
    levels 1 through :math:`n`

:code:`Infinity`
    all levels from level 1

:code:`{:math:`n`}`
    level :math:`n` only

:code:`{:math:`m`, :math:`n`}`
    levels :math:`m` through :math:`n`





Level 0 corresponds to the whole expression.

A negative level :code:`-:math:`n``  consists of parts with depth :math:`n`.

Level -1 is the set of atoms in an expression:

>>> Level[a + b ^ 3 * f[2 x ^ 2], {-1}]

    =
:math:`\left\{a,b,3,2,x,2\right\}`


>>> Level[{{{{a}}}}, 3]

    =
:math:`\left\{\left\{a\right\},\left\{\left\{a\right\}\right\},\left\{\left\{\left\{a\right\}\right\}\right\}\right\}`


>>> Level[{{{{a}}}}, -4]

    =
:math:`\left\{\left\{\left\{\left\{a\right\}\right\}\right\}\right\}`


>>> Level[{{{{a}}}}, -5]

    =
:math:`\left\{\right\}`


>>> Level[h0[h1[h2[h3[a]]]], {0, -1}]

    =
:math:`\left\{a,\text{h3}\left[a\right],\text{h2}\left[\text{h3}\left[a\right]\right],\text{h1}\left[\text{h2}\left[\text{h3}\left[a\right]\right]\right],\text{h0}\left[\text{h1}\left[\text{h2}\left[\text{h3}\left[a\right]\right]\right]\right]\right\}`



Use the option :code:`Heads -> True`  to include heads:

>>> Level[{{{{a}}}}, 3, Heads -> True]

    =
:math:`\left\{\text{List},\text{List},\text{List},\left\{a\right\},\left\{\left\{a\right\}\right\},\left\{\left\{\left\{a\right\}\right\}\right\}\right\}`


>>> Level[x^2 + y^3, 3, Heads -> True]

    =
:math:`\left\{\text{Plus},\text{Power},x,2,x^2,\text{Power},y,3,y^3\right\}`


>>> Level[a ^ 2 + 2 * b, {-1}, Heads -> True]

    =
:math:`\left\{\text{Plus},\text{Power},a,2,\text{Times},2,b\right\}`


>>> Level[f[g[h]][x], {-1}, Heads -> True]

    =
:math:`\left\{f,g,h,x\right\}`


>>> Level[f[g[h]][x], {-2, -1}, Heads -> True]

    =
:math:`\left\{f,g,h,g\left[h\right],x,f\left[g\left[h\right]\right]\left[x\right]\right\}`


