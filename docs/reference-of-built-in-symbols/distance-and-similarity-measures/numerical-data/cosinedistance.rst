CosineDistance
==============

`Cosine similarity <https://en.wikipedia.org/wiki/Cosine_similarity>`_ (`WMA <https://reference.wolfram.com/language/ref/CosineDistance.html>`_)


:code:`CosineDistance` [:math:`u`, :math:`v`]
    returns the angular cosine distance between vectors :math:`u` and :math:`v`.





The cosine distance is equivalent to :math:`1 - (u.Conjugate[v]) / (Norm[u] Norm[v])`.

>>> N[CosineDistance[{7, 9}, {71, 89}]]

    =
:math:`0.0000759646`



When the length of either vector is 0, the result is 0:

>>> CosineDistance[{0.0, 0.0}, {x, y}]

    =
:math:`0`


>>> CosineDistance[{1, 0}, {x, y}]

    =
:math:`1-\frac{\text{Conjugate}\left[x\right]}{\sqrt{\text{Abs}\left[x\right]^2+\text{Abs}\left[y\right]^2}}`



The order of the vectors influences the result:

>>> CosineDistance[{x, y}, {1, 0}]

    =
:math:`1-\frac{x}{\sqrt{\text{Abs}\left[x\right]^2+\text{Abs}\left[y\right]^2}}`



Cosine distance includes a dot product scaled by norms:

>>> CosineDistance[{a, b, c}, {x, y, z}]

    =
:math:`1+\frac{-a \text{Conjugate}\left[x\right]-b \text{Conjugate}\left[y\right]-c \text{Conjugate}\left[z\right]}{\sqrt{\text{Abs}\left[a\right]^2+\text{Abs}\left[b\right]^2+\text{Abs}\left[c\right]^2} \sqrt{\text{Abs}\left[x\right]^2+\text{Abs}\left[y\right]^2+\text{Abs}\left[z\right]^2}}`



A Cosine distance applied to complex numbers, uses :code:`Abs[]`  for :code:`Norm[]`  and complex multiplication for dot product,
1 - :math:`u` * Conjugate[:math:`v`] / (:code:`Abs[:math:`u`] Abs[:math:`v`]` ):

>>> CosineDistance[1+2I, 5]

    =
:math:`1-\left(\frac{1}{5}+\frac{2 I}{5}\right) \sqrt{5}`


