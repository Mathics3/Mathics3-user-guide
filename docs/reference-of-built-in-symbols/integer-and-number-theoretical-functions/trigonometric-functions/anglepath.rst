AnglePath
=========

`WMA link <https://reference.wolfram.com/language/ref/AnglePath.html>`_


:code:`AnglePath` [{:math:`\phi_1`, :math:`\phi_2`, ...}]
    returns the points formed by a turtle starting at {0, 0} and angled at 0 degrees going through
    the turns given by angles :math:`\phi_1`, :math:`\phi_2`, ... and using distance 1 for each step.

:code:`AnglePath` [{{:math:`r_1`, :math:`\phi_1`}, {:math:`r_2`, :math:`\phi_2`}, ...}]
    instead of using 1 as distance, use :math:`r_1`, :math:`r_2`, ... as distances for the respective steps.

:code:`AnglePath` [:math:`\phi_0`, {:math:`\phi_1`, :math:`\phi_2`, ...}]
    starts with direction :math:`\phi_0` instead of 0.

:code:`AnglePath` [{:math:`x`, :math:`y`}, {:math:`\phi_1`, :math:`\phi_2`, ...}]
    starts at {:math:`x`, :math:`y`} instead of {0, 0}.

:code:`AnglePath` [{{:math:`x`, :math:`y`}, :math:`\phi_0`}, {:math:`\phi_1`, :math:`\phi_2`, ...}]
    specifies initial position {:math:`x`, :math:`y`} and initial direction :math:`\phi_0`.

:code:`AnglePath` [{{:math:`x`, :math:`y`}, {:math:`d_x`, :math:`d_y`}}, {:math:`\phi_1`, :math:`\phi_2`, ...}]
    specifies initial position {:math:`x`, :math:`y`} and a slope {:math:`d_x`, :math:`d_y`} that is understood to be the initial direction of the turtle.





>>> AnglePath[{90 Degree, 90 Degree, 90 Degree, 90 Degree}]
  = {{0, 0}, {0, 1}, {-1, 1}, {-1, 0}, {0, 0}}
>>> AnglePath[{{1, 1}, 90 Degree}, {{1, 90 Degree}, {2, 90 Degree}, {1, 90 Degree}, {2, 90 Degree}}]
  = {{1, 1}, {0, 1}, {0, -1}, {1, -1}, {1, 1}}
>>> AnglePath[{a, b}]
  = {{0, 0}, {Cos[a], Sin[a]}, {Cos[a] + Cos[a + b], Sin[a] + Sin[a + b]}}
>>> Precision[Part[AnglePath[{N[1/3, 100], N[2/3, 100]}], 2, 1]]
  = 100.
>>> Graphics[Line[AnglePath[Table[1.7, {50}]]]]
  = -Graphics-
>>> Graphics[Line[AnglePath[RandomReal[{-1, 1}, {100}]]]]
  = -Graphics-
