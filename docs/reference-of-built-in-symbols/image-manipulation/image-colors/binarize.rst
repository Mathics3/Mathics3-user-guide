Binarize
========

`WMA link <https://reference.wolfram.com/language/ref/Binarize.html>`_


:code:`Binarize` [:math:`image`]
    gives a binarized version of :math:`image`, in which each pixel is either 0 or 1.

:code:`Binarize` [:math:`image`, :math:`t`]
    map values :math:`x` > :math:`t` to 1, and values :math:`x` <= :math:`t` to 0.

:code:`Binarize` [:math:`image`, {:math:`t_1`, :math:`t_2`}]
    map :math:`t_1` < :math:`x` < :math:`t_2` to 1, and all other values to 0.





>>> hedy = Import["ExampleData/hedy.tif"];


>>> Binarize[hedy]

    =
.. image:: tmpy8uxlor7.png
    :align: center



>>> Binarize[hedy, 0.7]

    =
.. image:: tmpb_stjkg1.png
    :align: center



>>> Binarize[hedy, {0.2, 0.6}]

    =
.. image:: tmphu5nc3oe.png
    :align: center



