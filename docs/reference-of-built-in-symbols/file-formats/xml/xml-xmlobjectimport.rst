XML`XMLObjectImport
===================


:code:`XML`XMLObjectImport["string"]`
    parses "string" as XML code, and returns a list of XMLObjects found.





>>> Part[Import["ExampleData/InventionNo1.xml", "XMLObject"], 2, 3, 1]

    =
:math:`\text{XMLElement}\left[\text{identification},\left\{\right\},\left\{\text{XMLElement}\left[\text{encoding},\left\{\right\},\left\{\text{XMLElement}\left[\text{software},\left\{\right\},\left\{\text{MuseScore 1.2}\right\}\right],\text{XMLElement}\left[\text{encoding-date},\left\{\right\},\left\{\text{2012-09-12}\right\}\right]\right\}\right]\right\}\right]`


>>> Part[Import["ExampleData/Namespaces.xml"], 2]

    =
:math:`\text{XMLElement}\left[\text{book},\left\{\left\{\text{http://www.w3.org/2000/xmlns/},\text{xmlns}\right\}->\text{urn:loc.gov:books}\right\},\left\{\text{XMLElement}\left[\text{title},\left\{\right\},\left\{\text{Cheaper by the Dozen}\right\}\right],\text{XMLElement}\left[\left\{\text{urn:ISBN:0-395-36341-6},\text{number}\right\},\left\{\right\},\left\{\text{1568491379}\right\}\right],\text{XMLElement}\left[\text{notes},\left\{\right\},\left\{\text{XMLElement}\left[\text{p},\left\{\left\{\text{http://www.w3.org/2000/xmlns/},\text{xmlns}\right\}->\text{http://www.w3.org/1999/xhtml}\right\},\left\{\text{This is a},\text{XMLElement}\left[\text{i},\left\{\right\},\left\{\text{funny},\text{book!}\right\}\right]\right\}\right]\right\}\right]\right\}\right]`


