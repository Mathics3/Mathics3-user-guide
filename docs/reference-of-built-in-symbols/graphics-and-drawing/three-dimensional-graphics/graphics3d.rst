Graphics3D
==========

`WMA link <https://reference.wolfram.com/language/ref/Graphics3D.html>`_


:code:`Graphics3D` [:math:`primitives`, :math:`options`]
    represents a three-dimensional graphic.
    
    See `Drawing Option and Option Values </doc/reference-of-built-in-symbols/graphics-and-drawing/drawing-options-and-option-values>`_ for a list of Plot options.





>>> Graphics3D[Polygon[{{0,0,0}, {0,1,1}, {1,0,0}}]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Graphics3D_t_kf_ati.png
    :align: center




The :code:`Background`  option allows to set the color of the background:

>>> Graphics3D[Sphere[], Background->RGBColor[.6, .7, 1.]]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Graphics_and_Drawing_Graphics3D_gle08z7a.png
    :align: center




In :code:`TeXForm` , :code:`Graphics3D`  creates Asymptote figures:

>>> Graphics3D[Sphere[]] // TeXForm

    =

.. math::
    \text{\newline
    $\backslash$begin\{asy\}\newline
    import three;\newline
    import solids;\newline
    import tube;\newline
    size(6.6667cm, 6.6667cm);\newline
    currentprojection=perspective(2.6,-4.8,4.0);\newline
    currentlight=light(rgb(0.5,0.5,0.5), specular=red, (2,0,2), (2,2,2), (0,2,2));\newline
    // Sphere3DBox\newline
    draw(surface(sphere((0, 0, 0), 1)), rgb(1,1,1)+opacity(1));\newline
    draw(((-1,-1,-1)--(1,-1,-1)), rgb(0.4, 0.4, 0.4)+linewidth(1));\newline
    draw(((-1,1,-1)--(1,1,-1)), rgb(0.4, 0.4, 0.4)+linewidth(1));\newline
    draw(((-1,-1,1)--(1,-1,1)), rgb(0.4, 0.4, 0.4)+linewidth(1));\newline
    draw(((-1,1,1)--(1,1,1)), rgb(0.4, 0.4, 0.4)+linewidth(1));\newline
    draw(((-1,-1,-1)--(-1,1,-1)), rgb(0.4, 0.4, 0.4)+linewidth(1));\newline
    draw(((1,-1,-1)--(1,1,-1)), rgb(0.4, 0.4, 0.4)+linewidth(1));\newline
    draw(((-1,-1,1)--(-1,1,1)), rgb(0.4, 0.4, 0.4)+linewidth(1));\newline
    draw(((1,-1,1)--(1,1,1)), rgb(0.4, 0.4, 0.4)+linewidth(1));\newline
    draw(((-1,-1,-1)--(-1,-1,1)), rgb(0.4, 0.4, 0.4)+linewidth(1));\newline
    draw(((1,-1,-1)--(1,-1,1)), rgb(0.4, 0.4, 0.4)+linewidth(1));\newline
    draw(((-1,1,-1)--(-1,1,1)), rgb(0.4, 0.4, 0.4)+linewidth(1));\newline
    draw(((1,1,-1)--(1,1,1)), rgb(0.4, 0.4, 0.4)+linewidth(1));\newline
    $\backslash$end\{asy\}\newline
    }



