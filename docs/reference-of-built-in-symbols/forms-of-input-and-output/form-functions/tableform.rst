TableForm
=========

`WMA link <https://reference.wolfram.com/language/ref/TableForm.html>`_


:code:`TableForm` [:math:`expr`]
    displays :math:`expr` as a table.





>>> TableForm[Array[a, {3,2}],TableDepth->1]
  = {a[1, 1], a[1, 2]}
    
    {a[2, 1], a[2, 2]}
    
    {a[3, 1], a[3, 2]}

A table of Graphics:

>>> Table[Style[Graphics[{EdgeForm[{Black}], RGBColor[r,g,b], Rectangle[]}], ImageSizeMultipliers->{0.2, 1}], {r,0,1,1/2}, {g,0,1,1/2}, {b,0,1,1/2}] // TableForm
  = -Graphics-   -Graphics-   -Graphics-
    
    -Graphics-   -Graphics-   -Graphics-
    
    -Graphics-   -Graphics-   -Graphics-
    
    -Graphics-   -Graphics-   -Graphics-
    
    -Graphics-   -Graphics-   -Graphics-
    
    -Graphics-   -Graphics-   -Graphics-
    
    -Graphics-   -Graphics-   -Graphics-
    
    -Graphics-   -Graphics-   -Graphics-
    
    -Graphics-   -Graphics-   -Graphics-
