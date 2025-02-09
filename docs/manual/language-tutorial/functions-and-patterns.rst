Functions and Patterns
======================

Functions can be defined in the following way:

>>> f[x_] := x ^ 2



This tells \Mathics to replace every occurrence of :code:`f`  with one (arbitrary) parameter :code:`x`  with :code:`x ^ 2` .

>>> f[3]

    =
:math:`9`


>>> f[a]

    =
:math:`a^2`



The definition of :code:`f`  does not specify anything for two parameters, so any such call will stay unevaluated:

>>> f[1, 2]

    =
:math:`f\left[1,2\right]`



In fact, `<functions>`_ in \Mathics are just one aspect of `<patterns>`_: :code:`f[x_]`  is a pattern that `<matches>`_ expressions like :code:`f[3]`  and :code:`f[a]` . The following patterns are available:

:code:`_`  or :code:`Blank[]`
    matches one expression.

:code:`Pattern` [:math:`x`, :math:`p`]
    matches the pattern :math:`p` and stores the matching sub-expression into :math:`x`.

:math:`x`:code:`_`  or :code:`Pattern[` :math:`x`, :code:`Blank[]]`
    matches one expression and stores it in :math:`x`.

:code:`__`  or :code:`BlankSequence[]`
    matches a sequence of one or more expressions.

:code:`___`  or :code:`BlankNullSequence[]`
    matches a sequence of zero or more expressions.

:code:`_` :math:`h` or :code:`Blank` [:math:`h`]
    matches one expression with head :math:`h`.

:math:`x`:code:`_` :math:`h` or :code:`Pattern[` :math:`x`, :code:`Blank[` :math:`h`:code:`]]`
    matches one expression with head :math:`h` and stores it in :math:`x`.

:math:`p` | :math:`q` or :code:`Alternatives[` :math:`p`, :math:`q`:code:`]`
    matches either pattern :math:`p` or :math:`q`.

:math:`p` :code:`?`  :math:`t` or :code:`PatternTest[` :math:`p`, :math:`t`:code:`]`
    matches :math:`p` if the test :math:`t[p]` yields :code:`True` .

:math:`p` :code:`/;`  :math:`c` or :code:`Condition[` :math:`p`, :math:`c`:code:`]`
    matches :math:`p` if condition :math:`c` holds.

:code:`Verbatim` [:math:`p`]
    matches an expression that equals :math:`p`, without regarding patterns inside :math:`p`.





As before, patterns can be used to define functions:

>>> g[s___] := Plus[s] ^ 2


>>> g[1, 2, 3]

    =
:math:`36`



:code:`MatchQ[:math:`e`, :math:`p`]`  tests whether :math:`e` matches :math:`p`:

>>> MatchQ[a + b, x_ + y_]

    =
:math:`\text{True}`


>>> MatchQ[6, _Integer]

    =
:math:`\text{True}`



:code:`ReplaceAll`  (:code:`/.` ) replaces all occurrences of a pattern in an expression using a :code:`Rule`  given by :code:`->` :

>>> {2, "a", 3, 2.5, "b", c} /. x_Integer -> x ^ 2

    =
:math:`\left\{4,\text{a},9,2.5,\text{b},c\right\}`



You can also specify a list of rules:

>>> {2, "a", 3, 2.5, "b", c} /. {x_Integer -> x ^ 2.0, y_String -> 10}

    =
:math:`\left\{4.,10,9.,2.5,10,c\right\}`



:code:`ReplaceRepeated`  (:code:`//.` ) applies a set of rules repeatedly, until the expression doesn't change anymore:

>>> {2, "a", 3, 2.5, "b", c} //. {x_Integer -> x ^ 2.0, y_String -> 10}

    =
:math:`\left\{4.,100.,9.,2.5,100.,c\right\}`



There is a "delayed" version of :code:`Rule`  which can be specified by :code:`:>`  (similar to the relation of :code:`:=`  to :code:`=` ):

>>> a :> 1 + 2

    =
:math:`a\text{:>}1+2`


>>> a -> 1 + 2

    =
:math:`a->3`



This is useful when the right side of a rule should not be evaluated immediately (before matching):

>>> {1, 2} /. x_Integer -> N[x]

    =
:math:`\left\{1,2\right\}`



Here, :code:`N`  is applied to :code:`x`  before the actual matching, simply yielding :code:`x` . With a delayed rule this can be avoided:

>>> {1, 2} /. x_Integer :> N[x]

    =
:math:`\left\{1.,2.\right\}`



:code:`ReplaceAll`  and :code:`ReplaceRepeated`  take the first possible match.
However :code:`ReplaceList`  returns a list of all possible matches.
This can be used to get all subsequences of a list, for instance:

>>> ReplaceList[{a, b, c}, {___, x__, ___} -> {x}]

    =
:math:`\left\{\left\{a\right\},\left\{a,b\right\},\left\{a,b,c\right\},\left\{b\right\},\left\{b,c\right\},\left\{c\right\}\right\}`



:code:`ReplaceAll`  would just return the first expression:

>>> ReplaceAll[{a, b, c}, {___, x__, ___} -> {x}]

    =
:math:`\left\{a\right\}`



In addition to defining functions as rules for certain patterns, there are `<pure>`_ functions that can be defined using the :code:`&`  postfix operator, where everything before it is treated as the function body, and :code:`#`  can be used as argument placeholder:

>>> h = # ^ 2 &;


>>> h[3]

    =
:math:`9`



Multiple arguments can simply be indexed:

>>> sum = #1 + #2 &;


>>> sum[4, 6]

    =
:math:`10`



It is also possible to name arguments using :code:`Function` :

>>> prod = Function[{x, y}, x * y];


>>> prod[4, 6]

    =
:math:`24`



Pure functions are very handy when functions are used only locally, e.g., when combined with operators like :code:`Map` :

>>> # ^ 2 & /@ Range[5]

    =
:math:`\left\{1,4,9,16,25\right\}`



Sort using the second element of a list as a key:

>>> Sort[{{x, 10}, {y, 2}, {z, 5}}, #1[[2]] < #2[[2]] &]

    =
:math:`\left\{\left\{y,2\right\},\left\{z,5\right\},\left\{x,10\right\}\right\}`



Functions can be applied using prefix or postfix notation, in addition to using :code:`[]` :

>>> h @ 3

    =
:math:`9`


>>> 3 // h

    =
:math:`9`


