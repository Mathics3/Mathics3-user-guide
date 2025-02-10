RandomReal
==========

`WMA link <https://reference.wolfram.com/language/ref/RandomReal.html>`_


:code:`RandomReal` [{:math:`min`, :math:`max`}]
    yields a pseudorandom real number in the range from :math:`min` to :math:`max`.

:code:`RandomReal` [:math:`max`]
    yields a pseudorandom real number in the range from 0 to :math:`max`.

:code:`RandomReal[]`
    yields a pseudorandom real number in the range from 0 to 1.

:code:`RandomReal` [:math:`range`, :math:`n`]
    gives a list of :math:`n` pseudorandom real numbers.

:code:`RandomReal` [:math:`range`, {:math:`n_1`, :math:`n_2`, ...}]
    gives an :math:`n_1` x :math:`n_2` array of pseudorandom real numbers.





>>> RandomReal[]

    =
:math:`0.358557`


>>> RandomReal[{1, 5}]

    =
:math:`1.14078`


