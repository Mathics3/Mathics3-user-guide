ImportExport`RegisterImport
===========================


:code:`RegisterImport` [":math:`format`", :math:`defaultFunction`]
    register :code:`:math:`defaultFunction``  as the default function used when           importing from a file of type :code:`":math:`format`"` .

:code:`RegisterImport[":math:`format`", {":math:`elem_1`" :> :math:`conditionalFunction_1`,           ":math:`elem_2`" :> :math:`conditionalFunction_2`, ..., :math:`defaultFunction`}]`
    registers multiple elements (:math:`elem_1`, ...) and their corresponding           converter functions (:math:`conditionalFunction_1`, ...) in addition to the :math:`defaultFunction`.

:code:`RegisterImport[":math:`format`", {":math:`conditionalFunctions`, :math:`defaultFunction`,            ":math:`elem_3`" :> :math:`postFunction_3`, ":math:`elem_4`" :> :math:`postFunction_4`, ...}]`
    also registers additional elements (:math:`elem_3`, ...) whose converters           (:math:`postFunction_3`, ...) act on output from the low-level functions.





First, define the default function used to import the data.

>>> ExampleFormat1Import[filename_String] := Module[{stream, head, data}, stream = OpenRead[filename]; head = ReadList[stream, String, 2]; data = Partition[ReadList[stream, Number], 2]; Close[stream]; {"Header" -> head, "Data" -> data}]



:code:`RegisterImport`  is then used to register the above function to a new data format.

>>> ImportExport`RegisterImport["ExampleFormat1", ExampleFormat1Import]


>>> FilePrint["ExampleData/ExampleData.txt"]

    Example File Format

    Created by Angus

    0.629452	0.586355

    0.711009	0.687453

    0.246540	0.433973

    0.926871	0.887255

    0.825141	0.940900

    0.847035	0.127464

    0.054348	0.296494

    0.838545	0.247025

    0.838697	0.436220

    0.309496	0.833591


>>> Import["ExampleData/ExampleData.txt", {"ExampleFormat1", "Elements"}]
    =

:math:`\left\{\text{Data},\text{Header}\right\}`


>>> Import["ExampleData/ExampleData.txt", {"ExampleFormat1", "Header"}]
    =

:math:`\left\{\text{Example File Format},\text{Created by Angus}\right\}`



Conditional Importer:

>>> ExampleFormat2DefaultImport[filename_String] := Module[{stream, head}, stream = OpenRead[filename]; head = ReadList[stream, String, 2]; Close[stream]; {"Header" -> head}]


>>> ExampleFormat2DataImport[filename_String] := Module[{stream, data}, stream = OpenRead[filename]; Skip[stream, String, 2]; data = Partition[ReadList[stream, Number], 2]; Close[stream]; {"Data" -> data}]


>>> ImportExport`RegisterImport["ExampleFormat2", {"Data" :> ExampleFormat2DataImport, ExampleFormat2DefaultImport}]


>>> Import["ExampleData/ExampleData.txt", {"ExampleFormat2", "Elements"}]
    =

:math:`\left\{\text{Data},\text{Header}\right\}`


>>> Import["ExampleData/ExampleData.txt", {"ExampleFormat2", "Header"}]
    =

:math:`\left\{\text{Example File Format},\text{Created by Angus}\right\}`


>>> Import["ExampleData/ExampleData.txt", {"ExampleFormat2", "Data"}] // Grid
    =

:math:`\begin{array}{cc} 0.629452 & 0.586355\\ 0.711009 & 0.687453\\ 0.24654 & 0.433973\\ 0.926871 & 0.887255\\ 0.825141 & 0.9409\\ 0.847035 & 0.127464\\ 0.054348 & 0.296494\\ 0.838545 & 0.247025\\ 0.838697 & 0.43622\\ 0.309496 & 0.833591\end{array}`


