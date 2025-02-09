ImageTake
=========

Extract Image parts `WMA link <https://reference.wolfram.com/language/ref/ImageTake.html>`_

:code:`ImageTake` [:math:`image`, :math:`n`]
    gives the first :math:`n` rows of :math:`image`.

:code:`ImageTake` [:math:`image`, -:math:`n`]
    gives the last :math:`n` rows of :math:`image`.

:code:`ImageTake` [:math:`image`, {:math:`r_1`, :math:`r_2`}]
    gives rows :math:`r_1`, ..., :math:`r_2` of :math:`image`.

:code:`ImageTake` [:math:`image`, {:math:`r_1`, :math:`r_2`}, {:math:`c_1`, :math:`c_2`}]
    gives a cropped version of :math:`image`.





Crop to the include only the upper half (244 rows) of an image:

>>> alice = Import["ExampleData/MadTeaParty.gif"]; ImageTake[alice, 244]

    =
.. image:: tmp7_f0t0ga.png
    :align: center




Now crop to the include the lower half of that image:

>>> ImageTake[alice, -244]

    =
.. image:: tmp2nzonprg.png
    :align: center




Just the text around the hat:

>>> ImageTake[alice, {40, 150}, {500, 600}]

    =
.. image:: tmpu1n922vm.png
    :align: center



