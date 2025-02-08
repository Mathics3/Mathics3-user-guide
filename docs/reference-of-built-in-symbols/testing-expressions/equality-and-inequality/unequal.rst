Unequal
=======

`WMA link <https://reference.wolfram.com/language/ref/Unequal.html>`_


:code:`Unequal` [:math:`x`, :math:`y`] or :math:`x` != :math:`y` or :math:`x` ≠ :math:`y`
    is :code:`False`  if :math:`x` and :math:`y` are known to be equal, or :code:`True`  if :math:`x`           and :math:`y` are known to be unequal.
    
    Commutative properties apply so if :math:`x` != :math:`y` then :math:`y` != :math:`x`.
    
    For any expression :math:`x` and :math:`y`, :code:`Unequal[:math:`x`, :math:`y`]`  == :code:`Not[Equal[:math:`x`, :math:`y`]]` .





>>> 1 != 1.
    =

:math:`\text{False}`



Comparisons can be chained:

>>> 1 != 2 != 3
    =

:math:`\text{True}`


>>> 1 != 2 != x
    =

:math:`1\text{!=}2\text{!=}x`



Strings are allowed:

>>> Unequal["11", "11"]
    =

:math:`\text{False}`



Comparison to mismatched types is True:

>>> Unequal[11, "11"]
    =

:math:`\text{True}`



Lists are compared based on their elements:

>>> {1} != {2}
    =

:math:`\text{True}`


>>> {1, 2} != {1, 2}
    =

:math:`\text{False}`


>>> {a} != {a}
    =

:math:`\text{False}`


>>> "a" != "b"
    =

:math:`\text{True}`


>>> "a" != "a"
    =

:math:`\text{False}`



:code:`Unequal`  using an empty parameter or list, or a list with one element is True. This is the same as 'Equal".

>>> {Unequal[], Unequal[x], Unequal[1]}
    =

:math:`\left\{\text{True},\text{True},\text{True}\right\}`


