FindFile
========

`WMA link <https://reference.wolfram.com/language/ref/FileFind.html>`_


:code:`FindFile` [:math:`name`]
    searches :code:`$Path`  for the given filename.





>>> FindFile["ExampleData/sunflowers.jpg"]

    =
:math:`\text{/home/mauricio/Projects/mathics-core/mathics/data/ExampleData/sunflowers.jpg}`


>>> FindFile["VectorAnalysis`"]

    =
:math:`\text{/home/mauricio/Projects/mathics-core/mathics/Packages/VectorAnalysis/Kernel/init.m}`


>>> FindFile["VectorAnalysis`VectorAnalysis`"]

    =
:math:`\text{/home/mauricio/Projects/mathics-core/mathics/Packages/VectorAnalysis/VectorAnalysis.m}`


