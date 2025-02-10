Arrowheads
==========

`WMA link <https://reference.wolfram.com/language/ref/Arrowheads.html>`_


:code:`Arrowheads` [:math:`s`]
    specifies that Arrow[] draws one arrow of size :math:`s` (relative to width of           image, defaults to 0.04).

:code:`Arrowheads` [{:math:`spec_1`, :math:`spec_2`, ..., :math:`spec_n`}]
    specifies that Arrow[] draws n arrows as defined by :math:`spec_1`, :math:`spec_2`,           ... :math:`spec_n`.

:code:`Arrowheads` [{{:math:`s`}}]
    specifies that one arrow of size :math:`s` should be drawn.

:code:`Arrowheads` [{{:math:`s`, :math:`pos`}}]
    specifies that one arrow of size :math:`s` should be drawn at position :math:`pos` (for           the arrow to be on the line, :math:`pos` has to be between 0, i.e. the start for           the line, and 1, i.e. the end of the line).

:code:`Arrowheads` [{{:math:`s`, :math:`pos`, :math:`g`}}]
    specifies that one arrow of size :math:`s` should be drawn at position :math:`pos`           using Graphics :math:`g`.





Arrows on both ends can be achieved using negative sizes:

>>> Graphics[{Circle[],Arrowheads[{-0.04, 0.04}], Arrow[{{0, 0}, {2, 2}}, {1,1}]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Arrowheads_d20r4jnb.png
    :align: center




You may also specify our own arrow shapes:

>>> Graphics[{Circle[], Arrowheads[{{0.04, 1, Graphics[{Red, Disk[]}]}}], Arrow[{{0, 0}, {Cos[Pi/3],Sin[Pi/3]}}]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Arrowheads_cay269np.png
    :align: center



>>> Graphics[{Arrowheads[Table[{0.04, i/10, Graphics[Disk[]]},{i,1,10}]], Arrow[{{0, 0}, {6, 5}, {1, -3}, {-2, 2}}]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Arrowheads_ky8s_yeb.png
    :align: center



