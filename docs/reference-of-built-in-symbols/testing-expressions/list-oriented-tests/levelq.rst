LevelQ
======


:code:`LevelQ` [:math:`expr`]
    tests whether :math:`expr` is a valid level specification. This function           is primarily used in function patterns for specifying type of a           parameter.





>>> LevelQ[2]
  = True
>>> LevelQ[{2, 4}]
  = True
>>> LevelQ[Infinity]
  = True
>>> LevelQ[a + b]
  = False

We will define MyMap with the "level" parameter as a synonym for the     Builtin Map equivalent:

>>> MyMap[f_, expr_, Pattern[levelspec, _?LevelQ]] := Map[f, expr, levelspec]

>>> MyMap[f, {{a, b}, {c, d}}, {2}]
  = {{f[a], f[b]}, {f[c], f[d]}}
>>> Map[f, {{a, b}, {c, d}}, {2}]
  = {{f[a], f[b]}, {f[c], f[d]}}

But notice that when we pass an invalid level specification, MyMap     does not match and therefore does not pass the arguments through to :code:`Map` .     So we do not see the error message that :code:`Map`  would normally produce

>>> Map[f, {{a, b}, {c, d}}, x]
  = Map[f, {{a, b}, {c, d}}, x]
>>> MyMap[f, {{a, b}, {c, d}}, {1, 2, 3}]
  = MyMap[f, {{a, b}, {c, d}}, {1, 2, 3}]
