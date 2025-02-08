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

:math:`0.272646+0.453084 I`


>>> RandomComplex[{1+I, 5+5I}]
    =

:math:`4.37826+1.36769 I`


>>> RandomComplex[1+I, 5]
    =

:math:`\left\{0.397522+0.630283 I,0.822376+0.703573 I,0.252261+0.0697195 I,0.0902746+0.0714251 I,0.0708285+0.384019 I\right\}`


>>> RandomComplex[{1+I, 2+2I}, {2, 2}]
    =

:math:`\left\{\left\{1.91992+1.39588 I,1.82145+1.46203 I\right\},\left\{1.71328+1.67062 I,1.89635+1.47271 I\right\}\right\}`


