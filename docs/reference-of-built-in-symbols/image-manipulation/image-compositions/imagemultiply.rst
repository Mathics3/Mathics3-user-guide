ImageMultiply
=============

`WMA link <https://reference.wolfram.com/language/ref/ImageMultiply.html>`_


:code:`ImageMultiply` [:math:`image`, :math:`expr_1`, :math:`expr_2`, ...]
    multiplies all :math:`expr_i` with :math:`image` where each :math:`expr_i` must be an image or a real number.





>>> i = Image[{{0, 0.5, 0.2, 0.1, 0.9}, {1.0, 0.1, 0.3, 0.8, 0.6}}];


>>> ImageMultiply[i, 0.2]

    =
.. image:: tmpmr3nugjt.png
    :align: center



>>> ImageMultiply[i, i]

    =
.. image:: tmpym481rth.png
    :align: center



