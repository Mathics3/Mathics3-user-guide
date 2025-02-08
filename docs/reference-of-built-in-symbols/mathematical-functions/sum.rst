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
    =

:math:`55`



The symbolic form he used:

>>> Sum[k, {k, 1, n}]
    =

:math:`\frac{n \left(1+n\right)}{2}`



A Geometric series with a finite limit:

>>> Sum[1 / 2 ^ i, {i, 1, k}]
    =

:math:`1-2^{-k}`



A Geometric series using Infinity:

>>> Sum[1 / 2 ^ i, {i, 1, Infinity}]
    =

:math:`1`



Leibniz formula used in computing Pi:

>>> Sum[1 / ((-1)^k (2k + 1)), {k, 0, Infinity}]
    =

:math:`\frac{ \pi }{4}`



A table of double sums to compute squares:

>>> Table[ Sum[i * j, {i, 0, n}, {j, 0, n}], {n, 0, 4} ]
    =

:math:`\left\{0,1,9,36,100\right\}`



Computing Harmonic using a sum

>>> Sum[1 / k ^ 2, {k, 1, n}]
    =

:math:`\text{HarmonicNumber}\left[n,2\right]`



Other symbolic sums:

>>> Sum[k, {k, n, 2 n}]
    =

:math:`\frac{3 n \left(1+n\right)}{2}`



A sum with Complex-number iteration values

>>> Sum[k, {k, I, I + 1}]
    =

:math:`1+2 I`


>>> Sum[k, {k, Range[5]}]
    =

:math:`15`


>>> Sum[f[i], {i, 1, 7}]
    =

:math:`f\left[1\right]+f\left[2\right]+f\left[3\right]+f\left[4\right]+f\left[5\right]+f\left[6\right]+f\left[7\right]`



Verify algebraic identities:

>>> Sum[x ^ 2, {x, 1, y}] - y * (y + 1) * (2 * y + 1) / 6
    =

:math:`0`



Non-integer bounds:

>>> Sum[i, {i, 1, 2.5}]
    =

:math:`3`


>>> Sum[i, {i, 1.1, 2.5}]
    =

:math:`3.2`


>>> Sum[k, {k, I, I + 1.5}]
    =

:math:`1+2 I`


