Range
=====

`WMA link <https://reference.wolfram.com/language/ref/Range.html>`_


:code:`Range` [:math:`n`]
    returns a list of integers from 1 to :math:`n`.

:code:`Range` [:math:`a`, :math:`b`]
    returns a list of (Integer, Rational, Real) numbers from :math:`a` to :math:`b`.

:code:`Range` [:math:`a`, :math:`b`, :math:`di`]
    returns a list of numbers from :math:`a` to :math:`b` using step :math:`di`.
    More specifically, :code:`Range`  starts from :math:`a` and successively adds         increments of :math:`di` until the result is greater (if :math:`di` > 0) or         less (if :math:`di` < 0) than :math:`b`.





>>> Range[5]
  = {1, 2, 3, 4, 5}
>>> Range[-3, 2]
  = {-3, -2, -1, 0, 1, 2}
>>> Range[5, 1, -2]
  = {5, 3, 1}
>>> Range[1.0, 2.3]
  = {1., 2.}
>>> Range[0, 2, 1/3]
  = {0, 1 / 3, 2 / 3, 1, 4 / 3, 5 / 3, 2}
>>> Range[1.0, 2.3, .5]
  = {1., 1.5, 2.}
