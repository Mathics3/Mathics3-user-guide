MakeBoxes
=========

`WMA link <https://reference.wolfram.com/language/ref/MakeBoxes.html>`_


:code:`MakeBoxes` [:math:`expr`]
    is a low-level formatting primitive that converts :math:`expr`
    to box form, without evaluating it.

:code:`\( ... \)`
    directly inputs box objects.





String representation of boxes

>>> \(x \^ 2\)
  = SuperscriptBox[x, 2]
>>> \(x \_ 2\)
  = SubscriptBox[x, 2]
>>> \( a \+ b \% c\)
  = UnderoverscriptBox[a, b, c]
>>> \( a \& b \% c\)
  = UnderoverscriptBox[a, c, b]
>>> \( \@ 5 \)
  = SqrtBox[5]
>>> \(x \& y \)
  = OverscriptBox[x, y]
>>> \(x \+ y \)
  = UnderscriptBox[x, y]
>>> \( x \^ 2 \_ 4 \)
  = SuperscriptBox[x, SubscriptBox[2, 4]]
>>> (a + b)[x]
  = (a + b)[x]
>>> (a b)[x]
  = (a b)[x]
>>> (a <> b)[x]
  = (a <> b)[x]
