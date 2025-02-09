Sort
====

`WMA link <https://reference.wolfram.com/language/ref/Sort.html>`_


:code:`Sort` [:math:`list`]
    sorts :math:`list` (or the elements of any other expression) according           to canonical ordering.

:code:`Sort` [:math:`list`, :math:`p`]
    sorts using :math:`p` to determine the order of two elements.





>>> Sort[{4, 1.0, a, 3+I}]

    =
:math:`\left\{1.,3+I,4,a\right\}`



Sort uses :code:`OrderedQ`  to determine ordering by default.
You can sort patterns according to their precedence using :code:`PatternsOrderedQ` :

>>> Sort[{items___, item_, OptionsPattern[], item_symbol, item_?test}, PatternsOrderedQ]

    =
:math:`\left\{\text{item\_symbol},\text{item\_}?\text{test},\text{item\_},\text{items\_\_\_},\text{OptionsPattern}\left[\right]\right\}`



When sorting patterns, values of atoms do not matter:

>>> Sort[{a, b/;t}, PatternsOrderedQ]

    =
:math:`\left\{b\text{/;}t,a\right\}`


>>> Sort[{2+c_, 1+b__}, PatternsOrderedQ]

    =
:math:`\left\{2+\text{c\_},1+\text{b\_\_}\right\}`


>>> Sort[{x_ + n_*y_, x_ + y_}, PatternsOrderedQ]

    =
:math:`\left\{\text{x\_}+\text{n\_} \text{y\_},\text{x\_}+\text{y\_}\right\}`



See also `ReverseSort </doc/reference-of-built-in-symbols/descriptive-statistics/order-statistics/reversesort/>`_.