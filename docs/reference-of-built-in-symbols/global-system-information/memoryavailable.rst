MemoryAvailable
===============

`WMA link <https://reference.wolfram.com/language/ref/MemoryAvailable.html>`_


:code:`MemoryAvailable`
    Returns the amount of the available physical memory.





>>> MemoryAvailable[]

    =
:math:`5189345280`



The relationship between $SystemMemory, MemoryAvailable, and MemoryInUse:

>>> $SystemMemory > MemoryAvailable[] > MemoryInUse[]

    =
:math:`\text{True}`


