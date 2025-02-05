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
  = -Graphics-
>>> Plot[Sin[x], {x,0,4 Pi}, Mesh->Full]
  = -Graphics-
>>> DensityPlot[Sin[x y], {x, -2, 2}, {y, -2, 2}, Mesh->Full]
  = -Graphics-
>>> Plot3D[Sin[x y], {x, -2, 2}, {y, -2, 2}, Mesh->Full]
  = -Graphics3D-
