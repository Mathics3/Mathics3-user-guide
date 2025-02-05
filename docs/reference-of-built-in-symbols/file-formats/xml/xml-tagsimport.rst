XML`TagsImport
==============


:code:`XML`TagsImport["string"]`
    parses "string" as XML code, and returns a list with the tags found.





>>> Take[Import["ExampleData/InventionNo1.xml", "Tags"], 10]
  = {accidental, alter, arpeggiate, articulations, attributes, backup, bar-style, barline, beam, beat-type}
