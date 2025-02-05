ImportExport`RegisterExport
===========================


:code:`RegisterExport` [":math:`format`", :math:`func`]
    register :code:`:math:`func``  as the default function used when exporting from a file of           type :code:`":math:`format`"` .





Simple text exporter

>>> ExampleExporter1[filename_, data_, opts___] := Module[{strm = OpenWrite[filename], char = data}, WriteString[strm, char]; Close[strm]]

>>> ImportExport`RegisterExport["ExampleFormat1", ExampleExporter1]

>>> Export["sample.txt", "Encode this string!", "ExampleFormat1"];

>>> FilePrint["sample.txt"]

>>> DeleteFile["sample.txt"]


Very basic encrypted text exporter:

>>> ExampleExporter2[filename_, data_, opts___] := Module[{strm = OpenWrite[filename], char}, (* TODO: Check data *) char = FromCharacterCode[Mod[ToCharacterCode[data] - 84, 26] + 97]; WriteString[strm, char]; Close[strm]]

>>> ImportExport`RegisterExport["ExampleFormat2", ExampleExporter2]

>>> Export["sample.txt", "encodethisstring", "ExampleFormat2"];

>>> FilePrint["sample.txt"]

>>> DeleteFile["sample.txt"]

