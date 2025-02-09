MachineNumberQ
==============

`WMA link <https://reference.wolfram.com/language/ref/MachineNumberQ.html>`_


:code:`MachineNumberQ` [:math:`expr`]
    returns :code:`True`  if :math:`expr` is a machine-precision real or complex number.





= True

>>> MachineNumberQ[3.14159265358979324]

    =
:math:`\text{False}`


>>> MachineNumberQ[1.5 + 2.3 I]

    =
:math:`\text{True}`


>>> MachineNumberQ[2.71828182845904524 + 3.14159265358979324 I]

    =
:math:`\text{False}`


