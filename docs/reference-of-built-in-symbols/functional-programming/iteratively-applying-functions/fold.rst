Fold
====

`WMA link <https://reference.wolfram.com/language/ref/Fold.html>`_


:code:`Fold` [:math:`f`, :math:`x`, :math:`list`]
    returns the result of iteratively applying the binary
    operator :math:`f` to each element of :math:`list`, starting with :math:`x`.

:code:`Fold` [:math:`f`, :math:`list`]
    is equivalent to :code:`Fold[:math:`f`, First[:math:`list`], Rest[:math:`list`]]` .





>>> Fold[Plus, 5, {1, 1, 1}]
    =

:math:`8`


>>> Fold[f, 5, {1, 2, 3}]
    =

:math:`f\left[f\left[f\left[5,1\right],2\right],3\right]`


