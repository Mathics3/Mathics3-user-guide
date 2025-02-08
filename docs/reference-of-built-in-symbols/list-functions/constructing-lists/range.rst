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
    =

:math:`\left\{1,2,3,4,5\right\}`


>>> Range[-3, 2]
    =

:math:`\left\{-3,-2,-1,0,1,2\right\}`


>>> Range[5, 1, -2]
    =

:math:`\left\{5,3,1\right\}`


>>> Range[1.0, 2.3]
    =

:math:`\left\{1.,2.\right\}`


>>> Range[0, 2, 1/3]
    =

:math:`\left\{0,\frac{1}{3},\frac{2}{3},1,\frac{4}{3},\frac{5}{3},2\right\}`


>>> Range[1.0, 2.3, .5]
    =

:math:`\left\{1.,1.5,2.\right\}`


