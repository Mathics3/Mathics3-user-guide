$CharacterEncoding
==================

`WMA link <https://reference.wolfram.com/language/ref/$CharacterEncoding.html>`_


:code:`$CharacterEncoding`
    specifies the default raw character encoding to use for input and       output when no encoding is explicitly specified.       Initially this is set to :code:`$SystemCharacterEncoding` .





See the character encoding current is in effect and used in input and     output functions functions like :code:`OpenRead[]` :

>>> $CharacterEncoding
    =

:math:`\text{ASCII}`



By setting its value to one of the values in :code:`$CharacterEncodings` ,     operators are formatted differently. For example,

>>> $CharacterEncoding = "ASCII"; a -> b
    =

:math:`a->b`


>>> $CharacterEncoding = "UTF-8"; a -> b
    =

:math:`a \rightarrow b`



Setting its value to :code:`None`  restore the value to     :code:`$SystemCharacterEncoding` :

>>> $CharacterEncoding = None;


>>> $SystemCharacterEncoding == $CharacterEncoding
    =

:math:`\text{True}`



See also `$SystemCharacterEncoding </doc/reference-of-built-in-symbols/atomic-elements-of-expressions/string-manipulation/$systemcharacterencoding/>`_.