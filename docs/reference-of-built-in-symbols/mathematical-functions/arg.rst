Arg
===

`Argument (complex analysis) <https://en.wikipedia.org/wiki/Argument_(complex_analysis)>`_ (`WMA link <https://reference.wolfram.com/language/ref/Arg.html>`_)


:code:`Arg` [:math:`z`, :code:`Method ->`  ":math:`option`"]
    returns the argument of a complex value :math:`z`.







- :code:`Arg` [:math:`z`] is left unevaluated if :math:`z` is not a numeric quantity.

- :code:`Arg` [:math:`z`] gives the phase angle of :math:`z` in radians.

- The result from :code:`Arg` [:math:`z`] is always between -Pi and +Pi.

- :code:`Arg` [:math:`z`] has a branch cut discontinuity in the complex :math:`z` plane running              from -Infinity to 0.

- :code:`Arg` [0] is 0.




>>> Arg[-3]
  = Pi

Same as above, but using SymPy's method:

>>> Arg[-3, Method->"sympy"]
  = Pi
>>> Arg[1-I]
  = -Pi / 4

:code:`Arg`  evaluates the direction of :code:`DirectedInfinity`  quantities by     the :code:`Arg`  of its arguments:

>>> Arg[DirectedInfinity[1+I]]
  = Pi / 4
>>> Arg[DirectedInfinity[]]
  = 1

Arg for 0 is assumed to be 0:

>>> Arg[0]
  = 0
