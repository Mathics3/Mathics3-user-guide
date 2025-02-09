$MachineEpsilon
===============

`WMA link <https://reference.wolfram.com/language/ref/$MachineEpsilon.html>`_


:code:`$MachineEpsilon`
    is the distance between :code:`1.0`  and the next nearest representable machine-precision number.





>>> $MachineEpsilon

    =
:math:`2.22045\text{*${}^{\wedge}$}-16`


>>> x = 1.0 + {0.4, 0.5, 0.6} $MachineEpsilon;


>>> x - 1

    =
:math:`\left\{0.,0.,2.22045\text{*${}^{\wedge}$}-16\right\}`


