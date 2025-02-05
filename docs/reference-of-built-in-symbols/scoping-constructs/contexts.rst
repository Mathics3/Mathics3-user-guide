Contexts
========

`WMA link <https://reference.wolfram.com/language/ref/Contexts.html>`_


:code:`Contexts[]`
    returns a list of contexts.

:code:`Contexts["string"]`
    returns a list of contexts that match the string.





:code:`Contexts`  allows the string patterns with the following metacharacters:


-  :code:`*`  zero or more characters

-  :code:`@`  one or more characters, excluding uppercase letters




Get a list of all contexts:

>>> Contexts[]
  = ...

Get a list of HTML contexts only:

>>> Contexts["HTML*"]
  = {HTML`, HTML`Parser`}
