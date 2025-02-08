ImageSubtract
=============

`WMA link <https://reference.wolfram.com/language/ref/ImageSubtract.html>`_


:code:`ImageSubtract` [:math:`image`, :math:`expr_1`, :math:`expr_2`, ...]
    subtracts all :math:`expr_i` from :math:`image` where each :math:`expr_i` must be an           image or a real number.





>>> i = Image[{{0, 0.5, 0.2, 0.1, 0.9}, {1.0, 0.1, 0.3, 0.8, 0.6}}];


>>> ImageSubtract[i, 0.2]
    =

.. image:: tmpzaphahr4.png
    :align: center



>>> ImageSubtract[i, i]
    =

.. image:: tmpj671at_9.png
    :align: center



