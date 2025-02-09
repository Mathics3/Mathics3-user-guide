BernoulliB
==========

`WMA link <https://reference.wolfram.com/language/ref/BernoulliB.html>`_


:code:`BernoulliB` [:math:`n`]
    represents the Bernoulli number :math:`B_n`.

:code:`BernouilliB` [:math:`n`, :math:`x`]
    represents the Bernoulli polynomial :math:`B_n(x)`.





>>> BernoulliB[42]

    =
:math:`\frac{1520097643918070802691}{1806}`



First five Bernoulli numbers:

>>> Table[BernoulliB[k], {k, 0, 5}]

    =
:math:`\left\{1,\frac{1}{2},\frac{1}{6},0,-\frac{1}{30},0\right\}`



First five Bernoulli polynomials:

>>> Table[BernoulliB[k, z], {k, 0, 3}]

    =
:math:`\left\{1,-\frac{1}{2}+z,\frac{1}{6}-z+z^2,\frac{z}{2}-\frac{3 z^2}{2}+z^3\right\}`


