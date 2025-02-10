EdgeForm
========

`WMA link <https://reference.wolfram.com/language/ref/EdgeForm.html>`_


:code:`EdgeForm` [:math:`g`]
    is a graphics directive that specifies that edges of filled graphics objects are to be drawn using the graphics directive or list of directives :math:`g`.





>>> Graphics[{EdgeForm[{Thick, Green}], Disk[]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_EdgeForm_fxz28ooj.png
    :align: center



>>> Graphics[{Style[Disk[],EdgeForm[{Thick,Red}]], Circle[{1,1}]}]

    =
.. image:: asy_Reference_of_Built-in_Symbols_Drawing_Graphics_EdgeForm_v1caxljb.png
    :align: center



