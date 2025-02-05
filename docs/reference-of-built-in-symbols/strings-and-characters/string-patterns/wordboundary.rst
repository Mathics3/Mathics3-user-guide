WordBoundary
============

`WMA link <https://reference.wolfram.com/language/ref/WordBoundary.html>`_


:code:`WordBoundary`
    represents the boundary between words.





>>> StringReplace["apple banana orange artichoke", "e" ~~ WordBoundary -> "E"]
  = applE banana orangE artichokE
