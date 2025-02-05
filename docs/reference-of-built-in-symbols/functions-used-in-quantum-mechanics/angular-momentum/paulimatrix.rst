PauliMatrix
===========

`Pauli matrices <https://en.wikipedia.org/wiki/Pauli_matrices>`_ (`SymPy <https://docs.sympy.org/latest/modules/physics/matrices.html#sympy.physics.matrices.msigma>`_, `WMA <https://reference.wolfram.com/language/ref/PauliMatrix.html>`_)


:code:`PauliMatrix` [:math:`k`]
    returns the :math:`k`-th Pauli spin matrix).





>>> Table[PauliMatrix[i], {i, 1, 3}]
  = {{{0, 1}, {1, 0}}, {{0, -I}, {I, 0}}, {{1, 0}, {0, -1}}}
>>> PauliMatrix[1] . PauliMatrix[2] == I PauliMatrix[3]
  = True
>>> MatrixExp[I \[Phi]/2 PauliMatrix[3]]
  = {{E ^ (I / 2 ϕ), 0}, {0, E ^ ((-I / 2) ϕ)}}
>>> % /. \[Phi] -> 2 Pi
  = {{-1, 0}, {0, -1}}
