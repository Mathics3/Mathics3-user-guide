DirectedInfinity
================

`WMA link <https://reference.wolfram.com/language/ref/DirectedInfinity.html>`_


:code:`DirectedInfinity` [:math:`z`]
    represents an infinite multiple of the complex number :math:`z`.

:code:`DirectedInfinity[]`
    is the same as :code:`ComplexInfinity` .





>>> DirectedInfinity[1]

    =
:math:`\infty`


>>> DirectedInfinity[]

    =
:math:`\text{ComplexInfinity}`


>>> DirectedInfinity[1 + I]

    =
:math:`\left(\frac{1}{2}+\frac{I}{2}\right) \sqrt{2} \infty`


>>> 1 / DirectedInfinity[1 + I]

    =
:math:`0`


>>> DirectedInfinity[1] + DirectedInfinity[-1]

    Infinity::indet Indeterminate expression -Infinity + Infinity encountered.

    =
:math:`\text{Indeterminate}`


>>> DirectedInfinity[0]

    =
:math:`\text{ComplexInfinity}`


