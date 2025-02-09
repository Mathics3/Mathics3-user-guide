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
.. image:: tmpm36wcvsz.png
    :align: center



>>> Plot[Sin[x], {x,0,4 Pi}, Mesh->Full]

    =
.. image:: tmpwqdqbk_m.png
    :align: center



>>> DensityPlot[Sin[x y], {x, -2, 2}, {y, -2, 2}, Mesh->Full]

    =
.. image:: tmpm2rj23d8.png
    :align: center



>>> Plot3D[Sin[x y], {x, -2, 2}, {y, -2, 2}, Mesh->Full]

    =
.. image:: tmpp_rz4w_0.png
    :align: center



