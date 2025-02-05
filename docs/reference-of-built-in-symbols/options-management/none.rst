None
====

`WMA link <https://reference.wolfram.com/language/ref/None.html>`_


:code:`None`
    is a setting value for many options.





Plot3D shows the mesh grid between computed points by default. This the `Mesh </doc/reference-of-built-in-symbols/graphics-and-drawing/drawing-options-and-option-values/mesh>`_
However, you hide the mesh by setting the :code:`Mesh`  option value to :code:`None` :

>>> Plot3D[{x^2 + y^2, -x^2 - y^2}, {x, -2, 2}, {y, -2, 2}, BoxRatios-> Automatic, Mesh->None]
  = -Graphics3D-
