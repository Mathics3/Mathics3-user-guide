ImageAdd
========

`WMA link <https://reference.wolfram.com/language/ref/ImageAdd.html>`_


:code:`ImageAdd` [:math:`image`, :math:`expr_1`, :math:`expr_2`, ...]
    adds all :math:`expr_i` to :math:`image` where each :math:`expr_i` must be an image           or a real number.





>>> i = Image[{{0, 0.5, 0.2, 0.1, 0.9}, {1.0, 0.1, 0.3, 0.8, 0.6}}];


>>> ImageAdd[i, 0.5]

    =
.. image:: tmpxdzq0zpe.png
    :align: center



>>> ImageAdd[i, i]

    =
.. image:: tmpmarp96r4.png
    :align: center



>>> ein = Import["ExampleData/Einstein.jpg"];


>>> noise = RandomImage[{-0.1, 0.1}, ImageDimensions[ein]];


>>> ImageAdd[noise, ein]

    =
.. image:: tmpouq18_fv.png
    :align: center



>>> hedy = Import["ExampleData/hedy.tif"];


>>> noise = RandomImage[{-0.2, 0.2}, ImageDimensions[hedy], ColorSpace -> "RGB"];


>>> ImageAdd[noise, hedy]

    =
.. image:: tmpf58kcuyp.png
    :align: center



