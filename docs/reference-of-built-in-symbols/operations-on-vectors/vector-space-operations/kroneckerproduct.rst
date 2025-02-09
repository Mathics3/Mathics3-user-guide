KroneckerProduct
================

`Kronecker product <https://en.wikipedia.org/wiki/Kronecker_product>`_ (`SymPy <https://docs.sympy.org/latest/modules/physics/quantum/tensorproduct.html>`_, `WMA <https://reference.wolfram.com/language/ref/KroneckerProduct.html>`_)


:code:`KroneckerProduct` [:math:`m_1`, :math:`m_2`, ...]
    returns the Kronecker product of the arrays :math:`m_i`





Show symbolically how the Kronecker product works on two two-dimensional arrays:

>>> a = {{a11, a12}, {a21, a22}}; b = {{b11, b12}, {b21, b22}};


>>> KroneckerProduct[a, b]

    =
:math:`\left\{\left\{\text{a11} \text{b11},\text{a11} \text{b12},\text{a12} \text{b11},\text{a12} \text{b12}\right\},\left\{\text{a11} \text{b21},\text{a11} \text{b22},\text{a12} \text{b21},\text{a12} \text{b22}\right\},\left\{\text{a21} \text{b11},\text{a21} \text{b12},\text{a22} \text{b11},\text{a22} \text{b12}\right\},\left\{\text{a21} \text{b21},\text{a21} \text{b22},\text{a22} \text{b21},\text{a22} \text{b22}\right\}\right\}`



Now do the same with discrete values:

>>> a = {{0, 1}, {-1, 0}}; b = {{1, 2}, {3, 4}};


>>> KroneckerProduct[a, b] // MatrixForm

    =
:math:`\left(\begin{array}{cccc} 0 & 0 & 1 & 2\\ 0 & 0 & 3 & 4\\ -1 & -2 & 0 & 0\\ -3 & -4 & 0 & 0\end{array}\right)`


>>> Clear[a, b];
    = `

