RealAbs
=======

`Abs (Real) <https://en.wikipedia.org/wiki/Absolute_value>`_ (`WMA link <https://reference.wolfram.com/language/ref/RealAbs.html>`_)


:code:`RealAbs` [:math:`x`]
    returns the absolute value of a real number :math:`x`.





:code:`RealAbs`  is also known as modulus. It is evaluated if :math:`x` can be compared     with :math:`0`.

>>> RealAbs[-3.]
  = 3.

:code:`RealAbs[:math:`z`]`  is left unevaluated for complex :math:`z`:

>>> RealAbs[2. + 3. I]
  = RealAbs[2. + 3. I]
>>> D[RealAbs[x ^ 2], x]
  = 2 x ^ 3 / RealAbs[x ^ 2]
