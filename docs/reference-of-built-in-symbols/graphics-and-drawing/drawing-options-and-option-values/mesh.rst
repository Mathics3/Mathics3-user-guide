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
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Mesh_83hp8o7e.png
    :align: center



>>> Plot[Sin[x], {x,0,4 Pi}, Mesh->Full]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Mesh_3ecsm2e8.png
    :align: center



>>> DensityPlot[Sin[x y], {x, -2, 2}, {y, -2, 2}, Mesh->Full]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Mesh_r9ksr7ip.png
    :align: center



>>> Plot3D[Sin[x y], {x, -2, 2}, {y, -2, 2}, Mesh->Full]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Mesh_klvjnek4.png
    :align: center



