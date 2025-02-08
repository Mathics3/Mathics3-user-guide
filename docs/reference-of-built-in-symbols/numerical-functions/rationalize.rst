Rationalize
===========

`WMA link <https://reference.wolfram.com/language/ref/Rationalize.html>`_


:code:`Rationalize` [:math:`x`]
    converts a real number :math:`x` to a nearby rational number with           small denominator.

:code:`Rationalize` [:math:`x`, :math:`d_x`]
    finds the rational number lies within :math:`d_x` of :math:`x`.





>>> Rationalize[2.2]
    =

:math:`\frac{11}{5}`



For negative :math:`x`, :code:`-Rationalize[-:math:`x`] == Rationalize[:math:`x`]`  which     gives symmetric results:

>>> Rationalize[-11.5, 1]
    =

:math:`-11`



Not all numbers can be well approximated.

>>> Rationalize[N[Pi]]
    =

:math:`3.14159`



Find the exact rational representation of :code:`N[Pi]` 

>>> Rationalize[N[Pi], 0]
    =

:math:`\frac{245850922}{78256779}`


