Blank
=====

`WMA link <https://reference.wolfram.com/language/ref/Blank.html>`_


:code:`Blank[]`
    same as

:code:`_`
    represents any single expression in a pattern.

:code:`Blank` [:math:`h`]
    same as

:code:`_:math:`h``
    represents any expression with head :math:`h`.





>>> MatchQ[a + b, _]
  = True

Patterns of the form :code:`_` :math:`h` can be used to test the types of     objects:

>>> MatchQ[42, _Integer]
  = True
>>> MatchQ[1.0, _Integer]
  = False
>>> {42, 1.0, x} /. {_Integer -> "integer", _Real -> "real"} // InputForm
  = {"integer", "real", x}

:code:`Blank`  only matches a single expression:

>>> MatchQ[f[1, 2], f[_]]
  = False
