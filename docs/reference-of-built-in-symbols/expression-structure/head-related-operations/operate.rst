Operate
=======

`WMA link <https://reference.wolfram.com/language/ref/Operate.html>`_


:code:`Operate` [:math:`p`, :math:`expr`]
    applies :math:`p` to the head of :math:`expr`.

:code:`Operate` [:math:`p`, :math:`expr`, :math:`n`]
    applies :math:`p` to the :math:`n`th head of :math:`expr`.





>>> Operate[p, f[a, b]]

    =
:math:`p\left[f\right]\left[a,b\right]`



The default value of :math:`n` is 1:

>>> Operate[p, f[a, b], 1]

    =
:math:`p\left[f\right]\left[a,b\right]`



With :math:`n`=0, :code:`Operate`  acts like :code:`Apply` :

>>> Operate[p, f[a][b][c], 0]

    =
:math:`p\left[f\left[a\right]\left[b\right]\left[c\right]\right]`


