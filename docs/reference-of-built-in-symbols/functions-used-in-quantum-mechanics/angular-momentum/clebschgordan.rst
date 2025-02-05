ClebschGordan
=============

`Clebsch-Gordan coefficients matrices <https://en.wikipedia.org/wiki/Clebsch%E2%80%93Gordan_coefficients>`_ (`SymPy <https://docs.sympy.org/latest/modules/physics/quantum/cg.html>`_, `WMA <https://reference.wolfram.com/language/ref/ClebschGordan>`_)


:code:`ClebschGordan` [{:math:`j_1`, :math:`m_1`}, {:math:`j_2`, :math:`m_2`}, {:math:`j` :math:`m`}]
    returns the Clebsch-Gordan coefficient for the decomposition of :math:`|j, m\rangle`       in terms of :math:`|j_1, m\rangle`, :math:`|j_2, m2\rangle`.





>>> ClebschGordan[{3 / 2, 3 / 2}, {1 / 2, -1 / 2}, {1, 1}]
  = Sqrt[3] / 2

:code:`ClebschGordan`  works with integer and half‐integer arguments:

>>> ClebschGordan[{1/2, -1/2}, {1/2, -1/2}, {1, -1}]
  = 1
>>> ClebschGordan[{1/2, -1/2}, {1, 0}, {1/2, -1/2}]
  = -Sqrt[3] / 3

Compare with WMA example:

>>> ClebschGordan[{5, 0}, {4, 0}, {1, 0}] == Sqrt[5 / 33]
  = True
