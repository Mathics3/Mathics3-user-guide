Array
=====

`WMA link <https://reference.wolfram.com/language/ref/Array.html>`_


:code:`Array` [:math:`f`, :math:`n`]
    returns the :math:`n`-element list :code:`{:math:`f`[1], ..., :math:`f`[:math:`n`]}` .

:code:`Array` [:math:`f`, :math:`n`, :math:`a`]
    returns the :math:`n`-element list :code:`{:math:`f`[:math:`a`], ..., :math:`f`[:math:`a` + :math:`n`]}` .

:code:`Array` [:math:`f`, {:math:`n`, :math:`m`}, {:math:`a`, :math:`b`}]
    returns an :math:`n`-by-:math:`m` matrix created by applying :math:`f` to indices           ranging from :code:`(:math:`a`, :math:`b`)`  to :code:`(:math:`a` + :math:`n`, :math:`b` + :math:`m`)` .

:code:`Array` [:math:`f`, :math:`dims`, :math:`origins`, :math:`h`]
    returns an expression with the specified dimensions and index origins,           with head :math:`h` (instead of :code:`List` ).





>>> Array[f, 4]
  = {f[1], f[2], f[3], f[4]}
>>> Array[f, {2, 3}]
  = {{f[1, 1], f[1, 2], f[1, 3]}, {f[2, 1], f[2, 2], f[2, 3]}}
>>> Array[f, {2, 3}, 3]
  = {{f[3, 3], f[3, 4], f[3, 5]}, {f[4, 3], f[4, 4], f[4, 5]}}
>>> Array[f, {2, 3}, {4, 6}]
  = {{f[4, 6], f[4, 7], f[4, 8]}, {f[5, 6], f[5, 7], f[5, 8]}}
>>> Array[f, {2, 3}, 1, Plus]
  = f[1, 1] + f[1, 2] + f[1, 3] + f[2, 1] + f[2, 2] + f[2, 3]
