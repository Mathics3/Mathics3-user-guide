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
:math:`0.963306+0.661374 I`


>>> RandomComplex[{1+I, 5+5I}]

    =
:math:`1.79519+4.76645 I`


>>> RandomComplex[1+I, 5]

    =
:math:`\left\{0.456712+0.338604 I,0.469558+0.240354 I,0.534559+0.0992511 I,0.754572+0.515928 I,0.376028+0.652849 I\right\}`


>>> RandomComplex[{1+I, 2+2I}, {2, 2}]

    =
:math:`\left\{\left\{1.96874+1.77004 I,1.27274+1.71205 I\right\},\left\{1.81611+1.43458 I,1.54173+1.84551 I\right\}\right\}`


