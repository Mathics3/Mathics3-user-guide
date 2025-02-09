MapThread
=========

`WMA link <https://reference.wolfram.com/language/ref/MapThread.html>`_


'MapThread[:math:`f`, {{:math:`a_1`, :math:`a_2`, ...}, {:math:`b_1`, :math:`b_2`, ...}, ...}]
    returns :code:`{:math:`f`[:math:`a_1`, :math:`b_1`, ...], :math:`f`[:math:`a_2`, :math:`b_2`, ...], ...}` .

:code:`MapThread` [:math:`f`, {:math:`expr_1`, :math:`expr_2`, ...}, :math:`n`]
    applies :math:`f` at level :math:`n`.





>>> MapThread[f, {{a, b, c}, {1, 2, 3}}]

    =
:math:`\left\{f\left[a,1\right],f\left[b,2\right],f\left[c,3\right]\right\}`


>>> MapThread[f, {{{a, b}, {c, d}}, {{e, f}, {g, h}}}, 2]

    =
:math:`\left\{\left\{f\left[a,e\right],f\left[b,f\right]\right\},\left\{f\left[c,g\right],f\left[d,h\right]\right\}\right\}`


