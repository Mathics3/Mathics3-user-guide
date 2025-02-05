CosineDistance
==============

`Cosine similarity <https://en.wikipedia.org/wiki/Cosine_similarity>`_ (`WMA <https://reference.wolfram.com/language/ref/CosineDistance.html>`_)


:code:`CosineDistance` [:math:`u`, :math:`v`]
    returns the angular cosine distance between vectors :math:`u` and :math:`v`.





The cosine distance is equivalent to :math:`1 - (u.Conjugate[v]) / (Norm[u] Norm[v])`.

>>> N[CosineDistance[{7, 9}, {71, 89}]]
  = 0.0000759646

When the length of either vector is 0, the result is 0:

>>> CosineDistance[{0.0, 0.0}, {x, y}]
  = 0
>>> CosineDistance[{1, 0}, {x, y}]
  = 1 - Conjugate[x] / Sqrt[Abs[x] ^ 2 + Abs[y] ^ 2]

The order of the vectors influences the result:

>>> CosineDistance[{x, y}, {1, 0}]
  = 1 - x / Sqrt[Abs[x] ^ 2 + Abs[y] ^ 2]

Cosine distance includes a dot product scaled by norms:

>>> CosineDistance[{a, b, c}, {x, y, z}]
  = 1 + (-a Conjugate[x] - b Conjugate[y] - c Conjugate[z]) / (Sqrt[Abs[a] ^ 2 + Abs[b] ^ 2 + Abs[c] ^ 2] Sqrt[Abs[x] ^ 2 + Abs[y] ^ 2 + Abs[z] ^ 2])

A Cosine distance applied to complex numbers, uses :code:`Abs[]`  for :code:`Norm[]`  and complex multiplication for dot product,
1 - :math:`u` * Conjugate[:math:`v`] / (:code:`Abs[:math:`u`] Abs[:math:`v`]` ):

>>> CosineDistance[1+2I, 5]
  = 1 - (1 / 5 + 2 I / 5) Sqrt[5]
