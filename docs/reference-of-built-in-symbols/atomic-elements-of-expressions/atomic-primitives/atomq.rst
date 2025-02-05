AtomQ
=====

`WMA link <https://reference.wolfram.com/language/ref/AtomQ.html>`_


:code:`AtomQ` [:math:`expr`]
    returns :code:`True`  if :math:`expr` is an expression which cannot be divided into       subexpressions, or :code:`False`  otherwise.
    
    An expression that cannot be divided into subparts is called called an "atom".





Strings and expressions that produce strings are atoms:

>>> Map[AtomQ, {"x", "x" <> "y", StringReverse["live"]}]
  = {True, True, True}

Numeric literals are atoms:

>>> Map[AtomQ, {2, 2.1, 1/2, 2 + I, 2^^101}]
  = {True, True, True, True, True}

So are Mathematical Constants:

>>> Map[AtomQ, {Pi, E, I, Degree}]
  = {True, True, True, True}

A :code:`Symbol`  not bound to a value is an atom too:

>>> AtomQ[x]
  = True

On the other hand, expressions with more than one :code:`Part`  after evaluation, even those resulting in numeric values, aren't atoms:

>>> AtomQ[2 + Pi]
  = False

Similarly any compound :code:`Expression` , even lists of literals, aren't atoms:

>>> Map[AtomQ, {{}, {1}, {2, 3, 4}}]
  = {False, False, False}

Note that evaluation or the binding of "x" to an expression is taken into account:

>>> x = 2 + Pi; AtomQ[x]
  = False

Again, note that the expression evaluation to a number occurs before :code:`AtomQ`  evaluated:

>>> AtomQ[2 + 3.1415]
  = True
>>> Clear[x]

