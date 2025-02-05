Unequal
=======

`WMA link <https://reference.wolfram.com/language/ref/Unequal.html>`_


:code:`Unequal` [:math:`x`, :math:`y`] or :math:`x` != :math:`y` or :math:`x` ≠ :math:`y`
    is :code:`False`  if :math:`x` and :math:`y` are known to be equal, or :code:`True`  if :math:`x`           and :math:`y` are known to be unequal.
    
    Commutative properties apply so if :math:`x` != :math:`y` then :math:`y` != :math:`x`.
    
    For any expression :math:`x` and :math:`y`, :code:`Unequal[:math:`x`, :math:`y`]`  == :code:`Not[Equal[:math:`x`, :math:`y`]]` .





>>> 1 != 1.
  = False

Comparisons can be chained:

>>> 1 != 2 != 3
  = True
>>> 1 != 2 != x
  = 1 != 2 != x

Strings are allowed:

>>> Unequal["11", "11"]
  = False

Comparison to mismatched types is True:

>>> Unequal[11, "11"]
  = True

Lists are compared based on their elements:

>>> {1} != {2}
  = True
>>> {1, 2} != {1, 2}
  = False
>>> {a} != {a}
  = False
>>> "a" != "b"
  = True
>>> "a" != "a"
  = False

:code:`Unequal`  using an empty parameter or list, or a list with one element is True. This is the same as 'Equal".

>>> {Unequal[], Unequal[x], Unequal[1]}
  = {True, True, True}
