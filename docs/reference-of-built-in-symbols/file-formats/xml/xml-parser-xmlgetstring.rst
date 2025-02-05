XML`Parser`XMLGetString
=======================


:code:`XML`Parser`XMLGetString["string"]`
    parses "string" as XML code, and returns an XMLObject.





>>> Head[XML`Parser`XMLGetString["<a></a>"]]
  = XMLObject[Document]
>>> XML`Parser`XMLGetString["<a></a>xyz"]
  = $Failed
