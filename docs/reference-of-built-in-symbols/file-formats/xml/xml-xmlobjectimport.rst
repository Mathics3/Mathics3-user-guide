XML`XMLObjectImport
===================


:code:`XML`XMLObjectImport["string"]`
    parses "string" as XML code, and returns a list of XMLObjects found.





>>> Part[Import["ExampleData/InventionNo1.xml", "XMLObject"], 2, 3, 1]
  = XMLElement[identification, {}, {XMLElement[encoding, {}, {XMLElement[software, {}, {MuseScore 1.2}], XMLElement[encoding-date, {}, {2012-09-12}]}]}]
>>> Part[Import["ExampleData/Namespaces.xml"], 2]
  = XMLElement[book, {{http://www.w3.org/2000/xmlns/, xmlns} -> urn:loc.gov:books}, {XMLElement[title, {}, {Cheaper by the Dozen}], XMLElement[{urn:ISBN:0-395-36341-6, number}, {}, {1568491379}], XMLElement[notes, {}, {XMLElement[p, {{http://www.w3.org/2000/xmlns/, xmlns} -> http://www.w3.org/1999/xhtml}, {This is a, XMLElement[i, {}, {funny, book!}]}]}]}]
