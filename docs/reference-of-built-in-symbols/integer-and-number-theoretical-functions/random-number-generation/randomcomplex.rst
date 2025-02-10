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
:math:`0.32005+0.271281 I`


>>> RandomComplex[{1+I, 5+5I}]

    =
:math:`1.51468+2.60813 I`


>>> RandomComplex[1+I, 5]

    =
:math:`\left\{0.713293+0.301641 I,0.0600777+0.324175 I,0.78783+0.473928 I,0.297303+0.95123 I,0.900556+0.012783 I\right\}`


>>> RandomComplex[{1+I, 2+2I}, {2, 2}]

    =
:math:`\left\{\left\{1.70867+1.15504 I,1.49256+1.68666 I\right\},\left\{1.18981+1.63147 I,1.18195+1.83118 I\right\}\right\}`


