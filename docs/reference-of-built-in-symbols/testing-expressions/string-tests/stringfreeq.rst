StringFreeQ
===========

`WMA link <https://reference.wolfram.com/language/ref/StringFreeQ.html>`_


:code:`StringFreeQ` [":math:`string`", :math:`patt`]
    returns True if no substring in :math:`string` matches the string       expression :math:`patt`, and returns False otherwise.

:code:`StringFreeQ[{"s1", "s2", ...}, patt]`
    returns the list of results for each element of string list.

:code:`StringFreeQ["string", {p1, p2, ...}]`
    returns True if no substring matches any of the :math:`pi`.

:code:`StringFreeQ[patt]`
    represents an operator form of StringFreeQ that can be applied         to an expression.





>>> StringFreeQ["mathics", "m" ~~ __ ~~ "s"]

    =
:math:`\text{False}`


>>> StringFreeQ["mathics", "a" ~~ __ ~~ "m"]

    =
:math:`\text{True}`


>>> StringFreeQ["Mathics", "MA" , IgnoreCase -> True]

    =
:math:`\text{False}`


>>> StringFreeQ[{"g", "a", "laxy", "universe", "sun"}, "u"]

    =
:math:`\left\{\text{True},\text{True},\text{True},\text{False},\text{False}\right\}`


>>> StringFreeQ["e" ~~ ___ ~~ "u"] /@ {"The Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

    =
:math:`\left\{\text{False},\text{False},\text{False},\text{True},\text{True},\text{True},\text{True},\text{True},\text{False}\right\}`


>>> StringFreeQ[{"A", "Galaxy", "Far", "Far", "Away"}, {"F" ~~ __ ~~ "r", "aw" ~~ ___}, IgnoreCase -> True]

    =
:math:`\left\{\text{True},\text{True},\text{False},\text{False},\text{False}\right\}`


