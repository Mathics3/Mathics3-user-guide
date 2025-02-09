RandomComplex
=============

`WMA link <https://reference.wolfram.com/language/ref/RandomComplex.html>`_


:code:`RandomComplex` [{:math:`z_{min}`, :math:`z_{max}`}]
    yields a pseudorandom complex number in the rectangle with complex corners           :math:`z_{min}` and :math:`z_{max}`.

:code:`RandomComplex` [:math:`z_{max}`]
    yields a pseudorandom complex number in the rectangle with corners at the           origin and at :math:`z_{max}`.

:code:`RandomComplex[]`
    yields a pseudorandom complex number with real and imaginary parts from 0           to 1.

:code:`RandomComplex` [:math:`range`, :math:`n`]
    gives a list of :math:`n` pseudorandom complex numbers.

:code:`RandomComplex` [:math:`range`, {:math:`n_1`, :math:`n_2`, ...}]
    gives a nested list of pseudorandom complex numbers.





>>> RandomComplex[]

    =
:math:`0.464692+0.610076 I`


>>> RandomComplex[{1+I, 5+5I}]

    =
:math:`2.41639+2.93584 I`


>>> RandomComplex[1+I, 5]

    =
:math:`\left\{0.69589+0.214739 I,0.465918+0.412887 I,0.240696+0.815011 I,0.494593+0.860968 I,0.907028+0.449173 I\right\}`


>>> RandomComplex[{1+I, 2+2I}, {2, 2}]

    =
:math:`\left\{\left\{1.62109+1.43988 I,1.19893+1.4323 I\right\},\left\{1.24256+1.01371 I,1.93493+1.75559 I\right\}\right\}`


