SameQ
=====

`WMA link <https://reference.wolfram.com/language/ref/SameQ.html>`_


:code:`SameQ` [:math:`x`, :math:`y`]
    same as

:code:`:math:`x` === :math:`y``
    returns :code:`True`  if :math:`x` and :math:`y` are structurally identical. Commutative properties apply, so if :math:`x` === :math:`y` then :math:`y` === :math:`x`.







- :code:`SameQ`  requires exact correspondence between expressions, expect that it still considers :code:`Real`  numbers equal if they differ in their last binary digit.

- :math:`e_1` === :math:`e_2` === :math:`e_3` gives :code:`True`  if all the :math:`ei`'s are identical.

- :code:`SameQ[]`  and :code:`SameQ[:math:`expr`]`  always yield :code:`True` .





Any object is the same as itself:

>>> a === a
    =

:math:`\text{True}`



Degenerate cases of :code:`SameQ`  showing off how you can chain :code:`===` :

>>> SameQ[a] === SameQ[] === True
    =

:math:`\text{True}`



Unlike :code:`Equal` , :code:`SameQ`  only yields :code:`True`  if :math:`x` and :math:`y` have the same type:

>>> {1==1., 1===1.}
    =

:math:`\left\{\text{True},\text{False}\right\}`


>>> 2./9. === .2222222222222222`15.9546
    =

:math:`\text{True}`



The comparison consider just the lowest precision

>>> .2222222`6 === .2222`3
    =

:math:`\text{True}`



Notice the extra decimal in the rhs. Because the internal representation,
:math:`0.222`3` is not equivalent to :math:`0.2222`3`:

>>> .2222222`6 === .222`3
    =

:math:`\text{False}`



15.9546 is the value of :code:`$MaxPrecision` 