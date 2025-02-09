Hue
===

`WMA link <https://reference.wolfram.com/language/ref/Hue.html>`_


:code:`Hue` [:math:`h`, :math:`s`, :math:`l`, :math:`a`]
    represents the color with hue :math:`h`, saturation :math:`s`, lightness :math:`l` and opacity :math:`a`.

:code:`Hue` [:math:`h`, :math:`s`, :math:`l`]
    is equivalent to :code:`Hue[:math:`h`, :math:`s`, :math:`l`, 1]` .

:code:`Hue` [:math:`h`, :math:`s`]
    is equivalent to :code:`Hue[:math:`h`, :math:`s`, 1, 1]` .

:code:`Hue` [:math:`h`]
    is equivalent to :code:`Hue[:math:`h`, 1, 1, 1]` .





>>> Graphics[Table[{EdgeForm[Gray], Hue[h, s], Disk[{12h, 8s}]}, {h, 0, 1, 1/6}, {s, 0, 1, 1/4}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Colors_Hue_5ikd427p.png
    :align: center



>>> Graphics[Table[{EdgeForm[{GrayLevel[0, 0.5]}], Hue[(-11+q+10r)/72, 1, 1, 0.6], Disk[(8-r) {Cos[2Pi q/12], Sin[2Pi q/12]}, (8-r)/3]}, {r, 6}, {q, 12}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Colors_Hue_st0oj6bn.png
    :align: center



