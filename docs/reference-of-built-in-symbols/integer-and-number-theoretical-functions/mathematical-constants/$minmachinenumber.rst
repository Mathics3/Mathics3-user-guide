$MinMachineNumber
=================

Smallest normalizable machine number (`WMA <https://reference.wolfram.com/language/ref/$MinMachineNumber.html>`_)


:code:`$MinMachineNumber`
    Represents the smallest positive number that can be represented as a normalized machine number in the system.





:code:`MachinePrecision`  minus the :code:`Log`  base 10 of this number is the :code:`Accuracy`  of 0`:

>>> MachinePrecision -Log[10., $MinMachineNumber]==Accuracy[0`]
  = True
