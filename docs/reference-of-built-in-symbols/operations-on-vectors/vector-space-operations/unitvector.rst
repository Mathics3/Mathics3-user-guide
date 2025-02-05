UnitVector
==========

`Unit vector <https://en.wikipedia.org/wiki/Unit_vector>`_ (`WMA <https://reference.wolfram.com/language/ref/UnitVector.html>`_)


:code:`UnitVector` [:math:`n`, :math:`k`]
    returns the :math:`n`-dimensional unit vector with a 1 in position :math:`k`.

:code:`UnitVector` [:math:`k`]
    is equivalent to :code:`UnitVector[2, :math:`k`]` .





>>> UnitVector[2]
  = {0, 1}
>>> UnitVector[4, 3]
  = {0, 0, 1, 0}
