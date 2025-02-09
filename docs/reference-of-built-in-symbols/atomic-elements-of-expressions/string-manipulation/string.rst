String
======

`WMA link <https://reference.wolfram.com/language/ref/String.html>`_

:code:`String`
    is the head of strings.





>>> Head["abc"]

    =
:math:`\text{String}`


>>> "abc"

    =
:math:`\text{abc}`



Use :code:`InputForm`  to display quotes around strings:

>>> InputForm["abc"]

    =
:math:`\text{\`{}\`{}abc''}`



:code:`FullForm`  also displays quotes:

>>> FullForm["abc" + 2]

    =
:math:`\text{Plus}\left[2, \text{\`{}\`{}abc''}\right]`


