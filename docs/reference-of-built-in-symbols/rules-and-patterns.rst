Rules and Patterns
==================

`WMA link <https://reference.wolfram.com/language/guide/RulesAndPatterns.html>`_


The concept of transformation rules for arbitrary symbolic patterns is key in \Mathics.

Also, functions can get applied or transformed depending on whether or not functions arguments match.

Some examples:

>>> a + b + c /. a + b -> t
    =

:math:`c+t`


>>> a + 2 + b + c + x * y /. n_Integer + s__Symbol + rest_ -> {n, s, rest}
    =

:math:`\left\{2,a,b+c+x y\right\}`


>>> f[a, b, c, d] /. f[first_, rest___] -> {first, {rest}}
    =

:math:`\left\{a,\left\{b,c,d\right\}\right\}`



Tests and Conditions:

>>> f[4] /. f[x_?(# > 0&)] -> x ^ 2
    =

:math:`16`


>>> f[4] /. f[x_] /; x > 0 -> x ^ 2
    =

:math:`16`



Elements in the beginning of a pattern rather match fewer elements:

>>> f[a, b, c, d] /. f[start__, end__] -> {{start}, {end}}
    =

:math:`\left\{\left\{a\right\},\left\{b,c,d\right\}\right\}`



Optional arguments using :code:`Optional` :

>>> f[a] /. f[x_, y_:3] -> {x, y}
    =

:math:`\left\{a,3\right\}`



Options using :code:`OptionsPattern`  and :code:`OptionValue` :

>>> f[y, a->3] /. f[x_, OptionsPattern[{a->2, b->5}]] -> {x, OptionValue[a], OptionValue[b]}
    =

:math:`\left\{y,3,5\right\}`



The attributes :code:`Flat` , :code:`Orderless` , and :code:`OneIdentity`  affect pattern matching.

.. toctree::
    :maxdepth: 2

    rules-and-patterns/basic-pattern-objects.rst
    rules-and-patterns/composite-patterns.rst
    rules-and-patterns/defining-applying-and-compiling-rules.rst
    rules-and-patterns/pattern-defaults.rst
    rules-and-patterns/restrictions-on-patterns.rst

