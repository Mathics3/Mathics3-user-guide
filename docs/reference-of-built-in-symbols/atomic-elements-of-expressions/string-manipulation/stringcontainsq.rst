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
    =

:math:`\text{True}`


>>> StringContainsQ["mathics", "a" ~~ __ ~~ "m"]
    =

:math:`\text{False}`


>>> StringContainsQ[{"g", "a", "laxy", "universe", "sun"}, "u"]
    =

:math:`\left\{\text{False},\text{False},\text{False},\text{True},\text{True}\right\}`


>>> StringContainsQ["e" ~~ ___ ~~ "u"] /@ {"The Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    =

:math:`\left\{\text{True},\text{True},\text{True},\text{False},\text{False},\text{False},\text{False},\text{False},\text{True}\right\}`


