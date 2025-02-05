Multinomial
===========

`Multinomial distribution <https://en.wikipedia.org/wiki/Multinomial_distribution>`_ (`WMA <https://reference.wolfram.com/language/ref/Multinomial.html>`_)

:code:`Multinomial` [:math:`n_1`, :math:`n_2`, ...]
    gives the multinomial coefficient :math:`(n_1+n_2+...)!/(n_1!n_2!...)`.





>>> Multinomial[2, 3, 4, 5]
  = 2522520
>>> Multinomial[]
  = 1

Multinomial is expressed in terms of :code:`Binomial` :

>>> Multinomial[a, b, c]
  = Binomial[a, a] Binomial[a + b, b] Binomial[a + b + c, c]

:code:`Multinomial` [:math:`n`-:math:`k`, :math:`k`] is equivalent to :code:`Binomial` [:math:`n`, :math:`k`]:

>>> Multinomial[2, 3]
  = 10

See also `:code:`Binomial`  </doc/reference-of-built-in-symbols/integer-functions/combinatorial-functions/binomial/>`_.