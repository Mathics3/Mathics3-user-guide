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

.. image:: tmpfv0fcv1b.png
    :align: center




Now crop to the include the lower half of that image:

>>> ImageTake[alice, -244]
    =

.. image:: tmpnqs8zi4h.png
    :align: center




Just the text around the hat:

>>> ImageTake[alice, {40, 150}, {500, 600}]
    =

.. image:: tmpg6g4i3u8.png
    :align: center



