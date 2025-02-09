Share
=====

`WMA link <https://reference.wolfram.com/language/ref/Share.html>`_


:code:`Share[]`
    release memory forcing Python to do garbage collection. If Python package           :code:`psutil`  installed is the amount of released memoryis returned. Otherwise           returns :math:`0`. This function differs from WMA which tries to reduce the amount           of memory required to store definitions, by reducing duplicated definitions.

:code:`Share[Symbol]`
    Does the same thing as :code:`Share[]` ; Note: this function differs from WMA which           tries to reduce the amount of memory required to store definitions associated           to :math:`Symbol`.





>>> Share[]

    =
:math:`258048`


