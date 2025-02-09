LevelQ
======


:code:`LevelQ` [:math:`expr`]
    tests whether :math:`expr` is a valid level specification. This function           is primarily used in function patterns for specifying type of a           parameter.





>>> LevelQ[2]

    =
:math:`\text{True}`


>>> LevelQ[{2, 4}]

    =
:math:`\text{True}`


>>> LevelQ[Infinity]

    =
:math:`\text{True}`


>>> LevelQ[a + b]

    =
:math:`\text{False}`



We will define MyMap with the "level" parameter as a synonym for the     Builtin Map equivalent:

>>> MyMap[f_, expr_, Pattern[levelspec, _?LevelQ]] := Map[f, expr, levelspec]


>>> MyMap[f, {{a, b}, {c, d}}, {2}]

    =
:math:`\left\{\left\{f\left[a\right],f\left[b\right]\right\},\left\{f\left[c\right],f\left[d\right]\right\}\right\}`


>>> Map[f, {{a, b}, {c, d}}, {2}]

    =
:math:`\left\{\left\{f\left[a\right],f\left[b\right]\right\},\left\{f\left[c\right],f\left[d\right]\right\}\right\}`



But notice that when we pass an invalid level specification, MyMap     does not match and therefore does not pass the arguments through to :code:`Map` .     So we do not see the error message that :code:`Map`  would normally produce

>>> Map[f, {{a, b}, {c, d}}, x]

    Map::level Level specification x is not of the form n, {n}, or {m, n}.

    =
:math:`\text{Map}\left[f,\left\{\left\{a,b\right\},\left\{c,d\right\}\right\},x\right]`


>>> MyMap[f, {{a, b}, {c, d}}, {1, 2, 3}]

    =
:math:`\text{MyMap}\left[f,\left\{\left\{a,b\right\},\left\{c,d\right\}\right\},\left\{1,2,3\right\}\right]`


