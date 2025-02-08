XML`Parser`XMLGetString
=======================


:code:`XML`Parser`XMLGetString["string"]`
    parses "string" as XML code, and returns an XMLObject.





>>> Head[XML`Parser`XMLGetString["<a></a>"]]
    =

:math:`\text{XMLObject}\left[\text{Document}\right]`


>>> XML`Parser`XMLGetString["<a></a>xyz"]
    = $Failed`

