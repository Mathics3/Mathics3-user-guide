Multinomial
===========

`Multinomial distribution <https://en.wikipedia.org/wiki/Multinomial_distribution>`_ (`WMA <https://reference.wolfram.com/language/ref/Multinomial.html>`_)

:code:`Multinomial` [:math:`n_1`, :math:`n_2`, ...]
    gives the multinomial coefficient :math:`(n_1+n_2+...)!/(n_1!n_2!...)`.





>>> Multinomial[2, 3, 4, 5]

    =
:math:`2522520`


>>> Multinomial[]

    =
:math:`1`



Multinomial is expressed in terms of :code:`Binomial` :

>>> Multinomial[a, b, c]

    =
:math:`\text{Binomial}\left[a,a\right] \text{Binomial}\left[a+b,b\right] \text{Binomial}\left[a+b+c,c\right]`



:code:`Multinomial` [:math:`n`-:math:`k`, :math:`k`] is equivalent to :code:`Binomial` [:math:`n`, :math:`k`]:

>>> Multinomial[2, 3]

    =
:math:`10`



See also `:code:`Binomial`  </doc/reference-of-built-in-symbols/integer-functions/combinatorial-functions/binomial/>`_.