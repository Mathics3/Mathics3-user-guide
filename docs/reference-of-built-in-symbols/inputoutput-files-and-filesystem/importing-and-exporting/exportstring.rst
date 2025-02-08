ExportString
============

`WMA link <https://reference.wolfram.com/language/ref/ExportString.html>`_


:code:`ExportString` [:math:`expr`, :math:`form`]
    exports :math:`expr` to a string, in the format :math:`form`.

:code:`Export` [":math:`file`", :math:`exprs`, :math:`elems`]
    exports :math:`exprs` to a string as elements specified by :math:`elems`.





>>> ExportString[{{1,2,3,4},{3},{2},{4}}, "CSV"]
    =


.. math::
    \text{1,2,3,4\newline
    3,\newline
    2,\newline
    4,}



>>> ExportString[{1,2,3,4}, "CSV"]
    =


.. math::
    \text{1,\newline
    2,\newline
    3,\newline
    4,}



>>> ExportString[Integrate[f[x],{x,0,2}], "SVG"]//Head
    =

:math:`\text{String}`


