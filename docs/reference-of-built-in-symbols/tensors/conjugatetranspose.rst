ConjugateTranspose
==================

`Conjugate transpose <https://en.wikipedia.org/wiki/Conjugate_transpose>`_ (`WMA <https://reference.wolfram.com/language/ref/ConjugateTranspose.html>`_)


:code:`ConjugateTranspose` [:math:`m`]
    gives the conjugate transpose of :math:`m`.





>>> ConjugateTranspose[{{0, I}, {0, 0}}]
  = {{0, 0}, {-I, 0}}
>>> ConjugateTranspose[{{1, 2 I, 3}, {3 + 4 I, 5, I}}]
  = {{1, 3 - 4 I}, {-2 I, 5}, {3, -I}}
