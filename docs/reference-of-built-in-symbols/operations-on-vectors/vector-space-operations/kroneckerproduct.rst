KroneckerProduct
================

`Kronecker product <https://en.wikipedia.org/wiki/Kronecker_product>`_ (`SymPy <https://docs.sympy.org/latest/modules/physics/quantum/tensorproduct.html>`_, `WMA <https://reference.wolfram.com/language/ref/KroneckerProduct.html>`_)


:code:`KroneckerProduct` [:math:`m_1`, :math:`m_2`, ...]
    returns the Kronecker product of the arrays :math:`m_i`





Show symbolically how the Kronecker product works on two two-dimensional arrays:

>>> a = {{a11, a12}, {a21, a22}}; b = {{b11, b12}, {b21, b22}};

>>> KroneckerProduct[a, b]
  = {{a11 b11, a11 b12, a12 b11, a12 b12}, {a11 b21, a11 b22, a12 b21, a12 b22}, {a21 b11, a21 b12, a22 b11, a22 b12}, {a21 b21, a21 b22, a22 b21, a22 b22}}

Now do the same with discrete values:

>>> a = {{0, 1}, {-1, 0}}; b = {{1, 2}, {3, 4}};

>>> KroneckerProduct[a, b] // MatrixForm
  = 0    0    1   2
    
     0    0    3   4
    
    -1   -2   0   0
    
    -3   -4   0   0
>>> Clear[a, b];

