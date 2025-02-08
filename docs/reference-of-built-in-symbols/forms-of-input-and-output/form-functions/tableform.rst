TableForm
=========

`WMA link <https://reference.wolfram.com/language/ref/TableForm.html>`_


:code:`TableForm` [:math:`expr`]
    displays :math:`expr` as a table.





>>> TableForm[Array[a, {3,2}],TableDepth->1]
    =

:math:`\begin{array}{c} \left\{a\left[1,1\right],a\left[1,2\right]\right\}\\ \left\{a\left[2,1\right],a\left[2,2\right]\right\}\\ \left\{a\left[3,1\right],a\left[3,2\right]\right\}\end{array}`



A table of Graphics:

>>> Table[Style[Graphics[{EdgeForm[{Black}], RGBColor[r,g,b], Rectangle[]}], ImageSizeMultipliers->{0.2, 1}], {r,0,1,1/2}, {g,0,1,1/2}, {b,0,1,1/2}] // TableForm
    =


.. math::
    \begin{array}{ccc} \begin{array}{c} 
    \includegraphics[]{/tmp/tmpogz1wr5l.png}
    \\ 
    \includegraphics[]{/tmp/tmpe071vhrt.png}
    \\ 
    \includegraphics[]{/tmp/tmp8gmjalyi.png}
    \end{array} & \begin{array}{c} 
    \includegraphics[]{/tmp/tmpg3is9__z.png}
    \\ 
    \includegraphics[]{/tmp/tmpdnpkmsp2.png}
    \\ 
    \includegraphics[]{/tmp/tmpi_7g3nwf.png}
    \end{array} & \begin{array}{c} 
    \includegraphics[]{/tmp/tmp27s_58py.png}
    \\ 
    \includegraphics[]{/tmp/tmpu2x0num9.png}
    \\ 
    \includegraphics[]{/tmp/tmp8oivawpl.png}
    \end{array}\\ \begin{array}{c} 
    \includegraphics[]{/tmp/tmprvtrmq_2.png}
    \\ 
    \includegraphics[]{/tmp/tmpkxu5b66h.png}
    \\ 
    \includegraphics[]{/tmp/tmphaq7ku8p.png}
    \end{array} & \begin{array}{c} 
    \includegraphics[]{/tmp/tmp24n86yps.png}
    \\ 
    \includegraphics[]{/tmp/tmp2_x3dvk5.png}
    \\ 
    \includegraphics[]{/tmp/tmprne0gnz4.png}
    \end{array} & \begin{array}{c} 
    \includegraphics[]{/tmp/tmppw2vi5fh.png}
    \\ 
    \includegraphics[]{/tmp/tmp7mfz0oi0.png}
    \\ 
    \includegraphics[]{/tmp/tmpmlbamuor.png}
    \end{array}\\ \begin{array}{c} 
    \includegraphics[]{/tmp/tmp3zxk8qmh.png}
    \\ 
    \includegraphics[]{/tmp/tmp878izgy1.png}
    \\ 
    \includegraphics[]{/tmp/tmpocxdbfav.png}
    \end{array} & \begin{array}{c} 
    \includegraphics[]{/tmp/tmprbayg6we.png}
    \\ 
    \includegraphics[]{/tmp/tmpalurbnc9.png}
    \\ 
    \includegraphics[]{/tmp/tmpxaak67m6.png}
    \end{array} & \begin{array}{c} 
    \includegraphics[]{/tmp/tmpo3ur42cl.png}
    \\ 
    \includegraphics[]{/tmp/tmp70ud1818.png}
    \\ 
    \includegraphics[]{/tmp/tmpa1zy5_hb.png}
    \end{array}\end{array}



