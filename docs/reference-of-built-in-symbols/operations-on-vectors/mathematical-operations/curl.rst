Curl
====

`Curl <https://en.wikipedia.org/wiki/Curl_(mathematics)>`_ (`SymPy <https://docs.sympy.org/latest/modules/vector/api/vectorfunctions.html#sympy.vector.curl>`_, `WMA <https://reference.wolfram.com/language/ref/Curl.html>`_)


:code:`Curl` [{:math:`f_1`, :math:`f_2`}, {:math:`x_1`, :math:`x_2`}]
    returns the curl :math:`df_2`/:math:`dx_1` - :math:`df_1`/:math:`dx_2`

:code:`Curl` [{:math:`f_1`, :math:`f_2`, :math:`f_3`} {:math:`x_1`, :math:`x_2`, :math:`x_3`}]
    returns the curl (:math:`df_3`/:math:`dx_2` - :math:`df_2`/:math:`dx_3`, :math:`dx_3`/:math:`df_3` - :math:`df_3`/:math:`dx_1`, :math:`df_2`/:math:`df_1` - :math:`df_1`/:math:`dx_2`)





Two-dimensional :code:`Curl` :

>>> Curl[{y, -x}, {x, y}]
  = -2
>>> v[x_, y_] := {Cos[x] Sin[y], Cos[y] Sin[x]}

>>> Curl[v[x, y], {x, y}]
  = 0

Three-dimensional :code:`Curl` :

>>> Curl[{y, -x, 2 z}, {x, y, z}]
  = {0, 0, -2}
>>> Clear[v];

