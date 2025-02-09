Arrow
=====

`WMA link <https://reference.wolfram.com/language/ref/Arrow.html>`_


:code:`Arrow` [{:math:`p_1`, :math:`p_2`}]
    represents a line from :math:`p_1` to :math:`p_2` that ends with an arrow at :math:`p_2`.

:code:`Arrow` [{:math:`p_1`, :math:`p_2`}, :math:`s`]
    represents a line with arrow that keeps a distance of :math:`s` from :math:`p_1` and :math:`p_2`.

:code:`Arrow` [{:math:`point_1`, :math:`point_2`}, {:math:`s_1`, :math:`s_2`}]
    represents a line with arrow that keeps a distance of :math:`s_1` from :math:`p_1` and a           distance of :math:`s_2` from :math:`p_2`.

:code:`Arrow` [{:math:`point_1`, :math:`point_2`}, {:math:`s_1`, :math:`s_2`}]
    represents a line with arrow that keeps a distance of :math:`s_1` from :math:`p_1` and a           distance of :math:`s_2` from :math:`p_2`.





>>> Graphics[Arrow[{{0,0}, {1,1}}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Arrow_l6s3m7f2.png
    :align: center



>>> Graphics[{Circle[], Arrow[{{2, 1}, {0, 0}}, 1]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Arrow_qg8_jqsh.png
    :align: center




Arrows can also be drawn in 3D by giving point in three dimensions:

>>> Graphics3D[Arrow[{{1, 1, -1}, {2, 2, 0}, {3, 3, -1}, {4, 4, 0}}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_Arrow_paj0jv08.png
    :align: center




Keeping distances may happen across multiple segments:

>>> Table[Graphics[{Circle[], Arrow[Table[{Cos[phi],Sin[phi]},{phi,0,2*Pi,Pi/2}],{d, d}]}],{d,0,2,0.5}]

    =
.. image:: eq_Reference of Built-in Symbols_Drawing Graphics_Arrow_q4fm4_ss.png
    :align: center



