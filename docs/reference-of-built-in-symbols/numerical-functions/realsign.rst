RealSign
========

`Sign function <https://en.wikipedia.org/wiki/Sign_function>`_ (`WMA link <https://reference.wolfram.com/language/ref/RealSign.html>`_)


:code:`RealSign` [:math:`x`]
    returns -1, 0 or 1 depending on whether :math:`x` is negative,
    zero or positive.





:code:`RealSign`  is also known as :math:`sgn` or :math:`signum` function.

>>> RealSign[-3.]

    =
:math:`-1`



:code:`RealSign[:math:`z`]`  is left unevaluated for complex :math:`z`:

>>> RealSign[2. + 3. I]

    =
:math:`\text{RealSign}\left[2.+3. I\right]`


>>> D[RealSign[x^2],x]

    =
:math:`2 x \text{Piecewise}\left[\left\{\left\{0,x^2\text{!=}0\right\}\right\},\text{Indeterminate}\right]`


>>> Integrate[RealSign[u],{u,0,x}]

    =
:math:`\text{RealAbs}\left[x\right]`


