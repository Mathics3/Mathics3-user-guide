Sum
===

`WMA link <https://reference.wolfram.com/language/ref/Sum.html>`_


:code:`Sum` [:math:`expr`, {:math:`i`, :math:`imin`, :math:`imax`}]
    evaluates the discrete sum of :math:`expr` with :math:`i` ranging from :math:`imin` to :math:`imax`.

:code:`Sum` [:math:`expr`, {:math:`i`, :math:`imax`}]
    same as :code:`Sum[:math:`expr`, {:math:`i`, 1, :math:`imax`}]` .

:code:`Sum` [:math:`expr`, {:math:`i`, :math:`imin`, :math:`imax`, :math:`di`}]
    :math:`i` ranges from :math:`imin` to :math:`imax` in steps of :math:`di`.

:code:`Sum` [:math:`expr`, {:math:`i`, :math:`imin`, :math:`imax`}, {:math:`j`, :math:`jmin`, :math:`jmax`}, ...]
    evaluates :math:`expr` as a multiple sum, with {:math:`i`, ...}, {:math:`j`, ...}, ... being           in outermost-to-innermost order.






A sum that Gauss in elementary school was asked to do to kill time:

>>> Sum[k, {k, 1, 10}]
  = 55

The symbolic form he used:

>>> Sum[k, {k, 1, n}]
  = n (1 + n) / 2

A Geometric series with a finite limit:

>>> Sum[1 / 2 ^ i, {i, 1, k}]
  = 1 - 2 ^ (-k)

A Geometric series using Infinity:

>>> Sum[1 / 2 ^ i, {i, 1, Infinity}]
  = 1

Leibniz formula used in computing Pi:

>>> Sum[1 / ((-1)^k (2k + 1)), {k, 0, Infinity}]
  = Pi / 4

A table of double sums to compute squares:

>>> Table[ Sum[i * j, {i, 0, n}, {j, 0, n}], {n, 0, 4} ]
  = {0, 1, 9, 36, 100}

Computing Harmonic using a sum

>>> Sum[1 / k ^ 2, {k, 1, n}]
  = HarmonicNumber[n, 2]

Other symbolic sums:

>>> Sum[k, {k, n, 2 n}]
  = 3 n (1 + n) / 2

A sum with Complex-number iteration values

>>> Sum[k, {k, I, I + 1}]
  = 1 + 2 I
>>> Sum[k, {k, Range[5]}]
  = 15
>>> Sum[f[i], {i, 1, 7}]
  = f[1] + f[2] + f[3] + f[4] + f[5] + f[6] + f[7]

Verify algebraic identities:

>>> Sum[x ^ 2, {x, 1, y}] - y * (y + 1) * (2 * y + 1) / 6
  = 0

Non-integer bounds:

>>> Sum[i, {i, 1, 2.5}]
  = 3
>>> Sum[i, {i, 1.1, 2.5}]
  = 3.2
>>> Sum[k, {k, I, I + 1.5}]
  = 1 + 2 I
