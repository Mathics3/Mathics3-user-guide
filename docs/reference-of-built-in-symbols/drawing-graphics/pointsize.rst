PointSize
=========

`WMA link <https://reference.wolfram.com/language/ref/PointSize.html>`_


:code:`PointSize` [:math:`t`]
    sets the diameter of points to :math:`t`, which is relative to the overall width.





:code:`PointSize`  can be used for both two- and three-dimensional graphics.     The initial default pointsize is 0.008 for two-dimensional graphics and 0.01 for three-dimensional graphics.

>>> Table[Graphics[{PointSize[r], Point[{0, 0}]}], {r, {0.02, 0.05, 0.1, 0.3}}]
    =


.. math::
    \left\{
    \includegraphics[]{/tmp/tmpyj3olfge.png}
    ,
    \includegraphics[]{/tmp/tmpw7kfqn3z.png}
    ,
    \includegraphics[]{/tmp/tmpegao2kob.png}
    ,
    \includegraphics[]{/tmp/tmpp_o14eec.png}
    \right\}



>>> Table[Graphics3D[{PointSize[r], Point[{0, 0, 0}]}], {r, {0.05, 0.1, 0.8}}]
    =


.. math::
    \left\{
    \includegraphics[]{/tmp/tmp3pql69wi.png}
    ,
    \includegraphics[]{/tmp/tmpx8ni1l3o.png}
    ,
    \includegraphics[]{/tmp/tmpq_prc3ak.png}
    \right\}



