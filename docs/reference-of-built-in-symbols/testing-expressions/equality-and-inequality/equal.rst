Equal
=====

`WMA link <https://reference.wolfram.com/language/ref/Equal.html>`_


:code:`Equal` [:math:`x`, :math:`y`]
    same as

:code:`:math:`x` == :math:`y``
    is :code:`True`  if :math:`x` and :math:`y` are known to be equal, or
    :code:`False`  if :math:`x` and :math:`y` are known to be unequal, in which case
    case, :code:`Not[:math:`x` == :math:`y`]`  will be :code:`True` .
    
    Commutative properties apply, so if :math:`x` == :math:`y` then :math:`y` == :math:`x`.
    
    For any expression :math:`x` and :math:`y`, Equal[:math:`x`, :math:`y`] == Not[Unequal[:math:`x`, :math:`y`]].
    
    For any expression :code:`SameQ[:math:`x`, :math:`y`]`  implies Equal[:math:`x`, :math:`y`].

:code:`:math:`x` == :math:`y` == :math:`z` == ...`
    express a chain of equalities.





Numerical Equalities:

>>> 1 == 1.
  = True
>>> 5/3 == 3/2
  = False

Comparisons are done using the lower precision:

>>> N[E, 100] == N[E, 150]
  = True

Compare an exact numeric expression and its corresponding approximate number:

>>> Pi == N[Pi, 20]
  = True

Symbolic constants are compared numerically:

>>> Pi == 3.14
  = False

Compare two exact numeric expressions; a numeric test may suffice to disprove equality:

>>> Pi ^ E == E ^ Pi
  = False

Compare an exact expression against an approximate real number:

>>> Pi == 3.1415``4
  = True

Real values are considered equal if they only differ in their last digits:

>>> 0.739085133215160642 == 0.739085133215160641
  = True
>>> 0.73908513321516064200000000 == 0.73908513321516064100000000
  = False

Numeric evaluation using Equal:

>>> {Mod[6, 2] == 0, Mod[6, 4] == 0}
  = {True, False}

String equalities:

>>> Equal["11", "11"]
  = True
>>> Equal["121", "11"]
  = False

When we have symbols without values, the values are equal
only if the symbols are equal:

>>> Clear[a, b]; a == b
  = a == b
>>> a == a
  = True
>>> a = b; a == b
  = True

Comparison to mismatched types is False:

>>> Equal[11, "11"]
  = False

Lists are compared based on their elements:

>>> {{1}, {2}} == {{1}, {2}}
  = True
>>> {1, 2} == {1, 2, 3}
  = False

For chains of equalities, the comparison is done amongst all the pairs.     The evaluation is successful only if the equality is satisfied over all the pairs:

>>> g[1] == g[1] == g[1]
  = True
>>> g[1] == g[1] == g[r]
  = g[1] == g[1] == g[r]

Equality can also be combined with other inequality expressions, like:

>>> g[1] == g[2] != g[3]
  = g[1] == g[2] && g[2] != g[3]
>>> g[1] == g[2] <= g[3]
  = g[1] == g[2] && g[2] <= g[3]

:code:`Equal`  with no parameter or an empty list is :code:`True` :

>>> Equal[] == True
  = True

:code:`Equal`  on one parameter or list element is also :code:`True` 

>>> {Equal[x], Equal[1], Equal["a"]}
  = {True, True, True}

This degenerate behavior is the same for :code:`Unequal` ;
empty or single-element lists are both :code:`Equal`  and :code:`Unequal` .