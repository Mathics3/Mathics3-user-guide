Mesh
====

`WMA link <https://reference.wolfram.com/language/ref/Mesh.html>`_


:code:`Mesh`
    is a charting option, such as for :code:`Plot` , :code:`BarChart` , :code:`PieChart` , etc. that           specifies the mesh to be drawn. The default is :code:`Mesh->None` .





Options include:



- None: No mesh is drawn

- All: mesh divisions between elements

- Full: mesh divisions between regular datapoints




>>> Plot[Sin[Cos[x^2]],{x,-4,4},Mesh->All]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Mesh_z_ivucko.png
    :align: center



>>> Plot[Sin[x], {x,0,4 Pi}, Mesh->Full]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Mesh_tpaly5d5.png
    :align: center



>>> DensityPlot[Sin[x y], {x, -2, 2}, {y, -2, 2}, Mesh->Full]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Mesh_opkhbzfc.png
    :align: center



>>> Plot3D[Sin[x y], {x, -2, 2}, {y, -2, 2}, Mesh->Full]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Mesh_nhkyipka.png
    :align: center



