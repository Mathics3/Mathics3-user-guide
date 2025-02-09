XML`PlaintextImport
===================

`WMA link <https://reference.wolfram.com/language/ref/PlaintextImport.html>`_


:code:`XML`PlaintextImport["string"]`
    parses "string" as XML code, and returns it as plain text.





>>> StringReplace[StringTake[Import["ExampleData/InventionNo1.xml", "Plaintext"],31],FromCharacterCode[10]->"/"]

    =
:math:`\text{MuseScore 1.2/2012-09-12/5.7/40}`


