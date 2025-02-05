HTML`Parser`HTMLGetString
=========================


:code:`HTML`Parser`HTMLGetString["string"]`
    parses HTML code contained in "string".





>>> Head[HTML`Parser`HTMLGetString["<a></a>"]]
  = XMLObject[Document]
>>> Head[HTML`Parser`HTMLGetString["<a><b></a>"]]
  = XMLObject[Document]
