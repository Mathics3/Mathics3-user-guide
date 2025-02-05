FromContinuedFraction
=====================

`WMA link <https://reference.wolfram.com/language/ref/FromContinuedFraction.html>`_


:code:`FromContinuedFraction` [:math:`list`]
    reconstructs a number from the list of its continued fraction terms.





>>> FromContinuedFraction[{3, 7, 15, 1, 292, 1, 1, 1, 2, 1}]
  = 1146408 / 364913
>>> FromContinuedFraction[Range[5]]
  = 225 / 157
