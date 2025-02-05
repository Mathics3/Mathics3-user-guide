StringContainsQ
===============

`WMA link <https://reference.wolfram.com/language/ref/StringContainsQ.html>`_

:code:`StringContainsQ` [":math:`string`", :math:`patt`]
    returns True if any part of :math:`string` matches :math:`patt`, and returns False otherwise.

:code:`StringContainsQ[{"s1", "s2", ...}, patt]`
    returns the list of results for each element of string list.

:code:`StringContainsQ[patt]`
    represents an operator form of StringContainsQ that can be applied to an expression.





>>> StringContainsQ["mathics", "m" ~~ __ ~~ "s"]
  = True
>>> StringContainsQ["mathics", "a" ~~ __ ~~ "m"]
  = False
>>> StringContainsQ[{"g", "a", "laxy", "universe", "sun"}, "u"]
  = {False, False, False, True, True}
>>> StringContainsQ["e" ~~ ___ ~~ "u"] /@ {"The Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
  = {True, True, True, False, False, False, False, False, True}
