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

.. image:: tmpz5n4zzau.png
    :align: center



>>> Plot[Sin[x], {x,0,4 Pi}, Mesh->Full]
    =

.. image:: tmp4htwhd3p.png
    :align: center



>>> DensityPlot[Sin[x y], {x, -2, 2}, {y, -2, 2}, Mesh->Full]
    =

.. image:: tmp9jk8kcxm.png
    :align: center



>>> Plot3D[Sin[x y], {x, -2, 2}, {y, -2, 2}, Mesh->Full]
    =

.. image:: tmp3mb4v7e1.png
    :align: center



