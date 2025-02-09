MessageName
===========

`WMA link <https://reference.wolfram.com/language/ref/MessageName.html>`_


:code:`MessageName` [:math:`symbol`, :math:`tag`]
    same as

:code:`:math:`symbol`:::math:`tag``
    identifies a message.





:code:`MessageName`  is the head of message IDs of the form :code:`symbol::tag` .

>>> FullForm[a::b]

    =
:math:`\text{MessageName}\left[a, \text{\`{}\`{}b''}\right]`



The second parameter :code:`tag`  is interpreted as a string.

>>> FullForm[a::"b"]

    =
:math:`\text{MessageName}\left[a, \text{\`{}\`{}b''}\right]`


