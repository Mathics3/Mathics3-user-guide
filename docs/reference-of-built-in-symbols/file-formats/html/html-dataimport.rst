HTML`DataImport
===============


:code:`HTML`DataImport["filename"]`
    imports data from a HTML file.





>>> Import["ExampleData/PrimeMeridian.html", "Data"][[1, 1, 2, 3]]

    =
:math:`\left\{\text{Washington, D.C.},\text{77°03′56.07″ W (1897) or 77°04′02.24″ W (NAD 27) or 77°04′01.16″ W (NAD 83)},\text{New Naval Observatory meridian}\right\}`


>>> Length[Import["ExampleData/PrimeMeridian.html", "Data"]]
    = 3`

