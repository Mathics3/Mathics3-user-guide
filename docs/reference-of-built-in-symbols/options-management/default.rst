Default
=======

`WMA link <https://reference.wolfram.com/language/ref/Default.html>`_


:code:`Default` [:math:`f`]
    gives the default value for an omitted parameter of :math:`f`.

:code:`Default` [:math:`f`, :math:`k`]
    gives the default value for a parameter on the :math:`k`-th position.

:code:`Default` [:math:`f`, :math:`k`, :math:`n`]
    gives the default value for the :math:`k`-th parameter out of :math:`n`.





Assign values to :code:`Default`  to specify default values.

>>> Default[f] = 1
  = 1
>>> f[x_.] := x ^ 2

>>> f[]
  = 1

Default values are stored in :code:`DefaultValues` :

>>> DefaultValues[f]
  = {HoldPattern[Default[f]] :> 1}

You can use patterns for :math:`k` and :math:`n`:

>>> Default[h, k_, n_] := {k, n}


Note that the position of a parameter is relative to the pattern, not the matching expression:

>>> h[] /. h[___, ___, x_., y_., ___] -> {x, y}
  = {{3, 5}, {4, 5}}
