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
    =

:math:`\left\{\text{HTML\`{}},\text{HTML\`{}Parser\`{}},\text{ImportExport\`{}},\text{Internal\`{}},\text{Pymathics\`{}},\text{Settings\`{}},\text{System\`{}},\text{System\`{}Convert\`{}Asy\`{}},\text{System\`{}Convert\`{}B64Dump\`{}},\text{System\`{}Convert\`{}Image\`{}},\text{System\`{}Convert\`{}JSONDump\`{}},\text{System\`{}Convert\`{}TableDump\`{}},\text{System\`{}Convert\`{}TextDump\`{}},\text{System\`{}ConvertersDump\`{}},\text{System\`{}Limit\`{}private\`{}},\text{System\`{}Private\`{}},\text{XML\`{}},\text{XML\`{}Parser\`{}},\text{internals\`{}bessel\`{}},\text{internals\`{}elements\`{}}\right\}`



Get a list of HTML contexts only:

>>> Contexts["HTML*"]
    =

:math:`\left\{\text{HTML\`{}},\text{HTML\`{}Parser\`{}}\right\}`


