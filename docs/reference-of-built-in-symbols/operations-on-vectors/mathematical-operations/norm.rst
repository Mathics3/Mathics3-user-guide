Norm
====

`Matrix norms induced by vector p-norms <https://en.wikipedia.org/wiki/Matrix_norm#Matrix_norms_induced_by_vector_p-norms>`_ (`SymPy <https://docs.sympy.org/latest/modules/matrices/matrices.html#sympy.matrices.matrices.MatrixBase.norm>`_, `WMA <https://reference.wolfram.com/language/ref/Norm.html>`_)


:code:`Norm` [:math:`m`, :math:`p`]
    computes the p-norm of matrix m.

:code:`Norm` [:math:`m`]
    computes the 2-norm of matrix m.





The :code:`Norm`  of of a vector is its Euclidean distance:

>>> Norm[{x, y, z}]
  = Sqrt[Abs[x] ^ 2 + Abs[y] ^ 2 + Abs[z] ^ 2]

By default, 2-norm is used for vectors, but you can be explicit:

>>> Norm[{3, 4}, 2]
  = 5

The 1-norm is the sum of the values:

>>> Norm[{10, 100, 200}, 1]
  = 310
>>> Norm[{x, y, z}, Infinity]
  = Max[{Abs[x], Abs[y], Abs[z]}]
>>> Norm[{-100, 2, 3, 4}, Infinity]
  = 100

For complex numbers, :code:`Norm[:math:`z`]`  is :code:`Abs[:math:`z`]` :

>>> Norm[1 + I]
  = Sqrt[2]

So the norm is always real, even when the input is complex.


:code:`Norm` [:math:`m`,"Frobenius"] gives the Frobenius norm of :math:`m`:

>>> Norm[Array[Subscript[a, ##] &, {2, 2}], "Frobenius"]
  = Sqrt[Abs[Subscript[a, 1, 1]] ^ 2 + Abs[Subscript[a, 1, 2]] ^ 2 + Abs[Subscript[a, 2, 1]] ^ 2 + Abs[Subscript[a, 2, 2]] ^ 2]
