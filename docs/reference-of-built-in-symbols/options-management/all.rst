All
===

`WMA link <https://reference.wolfram.com/language/ref/All.html>`_


:code:`All`
    is an option value for a number of functions indicating to include everything.






In list functions, it indicates all levels of the list.

For example, in `Part </doc/reference-of-built-in-symbols/list-functions/elements-of-lists/part>`_,     :code:`All` , extracts into a first column vector the first element of each of the     list elements:

>>> {{1, 3}, {5, 7}}[[All, 1]]
  = {1, 5}

While in `Take </doc/reference-of-built-in-symbols/list-functions/elements-of-lists/part>`_,     :code:`All`  extracts as a column matrix the first element as a list for each of the list     elements:

>>> Take[{{1, 3}, {5, 7}}, All, {1}]
  = {{1}, {5}}

In `Plot </doc/reference-of-built-in-symbols/graphics-and-drawing/plotting-data/plot>`_,     setting the `Mesh </doc/reference-of-built-in-symbols/graphics-and-drawing/drawing-options-and-option-values/mesh>`_     option to :code:`All`  will show the specific plot points:

>>> Plot[x^2, {x, -1, 1}, MaxRecursion->5, Mesh->All]
  = -Graphics-
