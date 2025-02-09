HTML`SourceImport
=================


:code:`HTML`SourceImport["filename"]`
    imports source code from a HTML file.





>>> DeleteDuplicates[StringCases[Import["ExampleData/PrimeMeridian.html", "Source"], RegularExpression["<t[a-z]+>"]]]

    =
:math:`\left\{\text{<title>},\text{<tr>},\text{<th>},\text{<td>}\right\}`


