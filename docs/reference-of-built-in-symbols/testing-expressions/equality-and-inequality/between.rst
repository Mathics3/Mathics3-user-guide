Between
=======

`WMA link <https://reference.wolfram.com/language/ref/Between.html>`_


:code:`Between` [:math:`x`, {:math:`min`, :math:`max`}]
    equivalent to :math:`min` <= :math:`x` <= :math:`max`.

:code:`Between` [:math:`x`, { {:math:`min_1`, :math:`max_1`}, {:math:`min_2`, :math:`max_2`}, ...]
    equivalent to :math:`min_1` <= :math:`x` <= :math:`max_1` || :math:`min_2` <= :math:`x` <= :math:`max_2` ...

:code:`Between` [:math:`range`]
    operator form that yields :code:`Between` [:math:`x`, :math:`range`] when applied to expression :math:`x`.





Check that 6 is in range 4..10:

>>> Between[6, {4, 10}]
    =

:math:`\text{True}`



Same as above in operator form:

>>> Between[{4, 10}][6]
    =

:math:`\text{True}`



:code:`Between`  works with irrational numbers:

>>> Between[2, {E, Pi}]
    =

:math:`\text{False}`



If more than an interval is given, :code:`Between`  returns :code:`True`  if :math:`x` belongs to one of them:

>>> {Between[3, {1, 2}, {4, 6}], Between[5, {1, 2}, {4, 6}]}
    =

:math:`\left\{\text{False},\text{True}\right\}`


