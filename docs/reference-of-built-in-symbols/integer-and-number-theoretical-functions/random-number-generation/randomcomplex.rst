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
:math:`0.785178+0.340514 I`


>>> RandomComplex[{1+I, 5+5I}]

    =
:math:`1.41135+1.62804 I`


>>> RandomComplex[1+I, 5]

    =
:math:`\left\{0.867427+0.298953 I,0.627428+0.996598 I,0.0919917+0.896386 I,0.386171+0.206905 I,0.366675+0.419415 I\right\}`


>>> RandomComplex[{1+I, 2+2I}, {2, 2}]

    =
:math:`\left\{\left\{1.1394+1.09267 I,1.88136+1.73885 I\right\},\left\{1.98749+1.8717 I,1.01962+1.97388 I\right\}\right\}`


