Product
=======

`WMA link <https://reference.wolfram.com/language/ref/Product.html>`_


:code:`Product` [:math:`f`, {:math:`i`, :math:`i_{min}`, :math:`i_{max}`}]
    evaluates the discrete product of :math:`f` with :math:`i` ranging from :math:`i_{min}` to :math:`i_{max}`.

:code:`Product` [:math:`f`, {:math:`i`, :math:`i_{max}`}]
    same as :code:`Product` [:math:`f`, {:math:`i, 1, i_{max}`}].

:code:`Product` [:math:`f`, {:math:`i, i_{min}, i_{max}`, :math:`di`}]
    :math:`i` ranges from :math:`i_{min}` to :math:`i_{max}` in steps of :math:`di`.

:code:`Product` [:math:`f`, {:math:`i, i_{min}, i_{max}`}, {:math:`j, j_{min}, j_{max}`}, ...]
    evaluates :math:`f` as a multiple product, with {:math:`i`, ...}, {:math:`j`, ...}, ... being in       outermost-to-innermost order.





>>> Product[k, {k, 1, 10}]
    =

:math:`3628800`


>>> 10!
    =

:math:`3628800`


>>> Product[x^k, {k, 2, 20, 2}]
    =

:math:`x^{110}`


>>> Product[2 ^ i, {i, 1, n}]
    =

:math:`2^{{\frac{n}{2}+\frac{n^2}{2}}}`


>>> Product[f[i], {i, 1, 7}]
    =

:math:`f\left[1\right] f\left[2\right] f\left[3\right] f\left[4\right] f\left[5\right] f\left[6\right] f\left[7\right]`



Symbolic products involving the factorial are evaluated:

>>> Product[k, {k, 3, n}]
    =

:math:`\frac{n!}{2}`



Evaluate the :math:`n`-th primorial:

>>> primorial[0] = 1;


>>> primorial[n_Integer] := Product[Prime[k], {k, 1, n}];


>>> primorial[12]
    =

:math:`7420738134810`


