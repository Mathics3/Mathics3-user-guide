PauliMatrix
===========

`Pauli matrices <https://en.wikipedia.org/wiki/Pauli_matrices>`_ (`SymPy <https://docs.sympy.org/latest/modules/physics/matrices.html#sympy.physics.matrices.msigma>`_, `WMA <https://reference.wolfram.com/language/ref/PauliMatrix.html>`_)


:code:`PauliMatrix` [:math:`k`]
    returns the :math:`k`-th Pauli spin matrix).





>>> Table[PauliMatrix[i], {i, 1, 3}]

    =
:math:`\left\{\left\{\left\{0,1\right\},\left\{1,0\right\}\right\},\left\{\left\{0,-I\right\},\left\{I,0\right\}\right\},\left\{\left\{1,0\right\},\left\{0,-1\right\}\right\}\right\}`


>>> PauliMatrix[1] . PauliMatrix[2] == I PauliMatrix[3]

    =
:math:`\text{True}`


>>> MatrixExp[I \[Phi]/2 PauliMatrix[3]]

    =
:math:`\left\{\left\{E^{\frac{I}{2}  \phi },0\right\},\left\{0,E^{\left(-\frac{I}{2}\right)  \phi }\right\}\right\}`


>>> % /. \[Phi] -> 2 Pi

    =
:math:`\left\{\left\{-1,0\right\},\left\{0,-1\right\}\right\}`


