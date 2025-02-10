TableForm
=========

`WMA link <https://reference.wolfram.com/language/ref/TableForm.html>`_


:code:`TableForm` [:math:`expr`]
    displays :math:`expr` as a table.





>>> TableForm[Array[a, {3,2}],TableDepth->1]

    =
:math:`\begin{array}{c} \left\{a\left[1,1\right],a\left[1,2\right]\right\}\\ \left\{a\left[2,1\right],a\left[2,2\right]\right\}\\ \left\{a\left[3,1\right],a\left[3,2\right]\right\}\end{array}`



A table of Graphics:

>>> Table[Style[Graphics[{EdgeForm[{Black}], RGBColor[r,g,b], Rectangle[]}], ImageSizeMultipliers->{0.2, 1}], {r,0,1,1/2}, {g,0,1,1/2}, {b,0,1,1/2}] // TableForm

    =
.. image:: eq_Reference_of_Built-in_Symbols_Forms_of_Input_and_Output_TableForm_rpqyt37c.png
    :align: center



