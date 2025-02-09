SetDelayed
==========

`WMA link <https://reference.wolfram.com/language/ref/SetDelayed.html>`_


:code:`SetDelayed` [:math:`expr`, :math:`value`]
    same as

:math:`expr` := :math:`value`
    assigns :math:`value` to :math:`expr`, without evaluating :math:`value`.





:code:`SetDelayed`  is like :code:`Set` , except it has attribute :code:`HoldAll` , thus it         does not evaluate the right-hand side immediately, but evaluates             it when needed.

>>> Attributes[SetDelayed]

    =
:math:`\left\{\text{HoldAll},\text{Protected},\text{SequenceHold}\right\}`


>>> a = 1

    =
:math:`1`


>>> x := a


>>> x

    =
:math:`1`



Changing the value of :math:`a` affects :math:`x`:

>>> a = 2

    =
:math:`2`


>>> x

    =
:math:`2`



:code:`Condition`  (:code:`/;` ) can be used with :code:`SetDelayed`  to make an
assignment that only holds if a condition is satisfied:

>>> f[x_] := p[x] /; x>0


>>> f[3]

    =
:math:`p\left[3\right]`


>>> f[-3]

    =
:math:`f\left[-3\right]`



It also works if the condition is set in the LHS:

>>> F[x_, y_] /; x < y /; x>0  := x / y;


>>> F[x_, y_] := y / x;


>>> F[2, 3]

    =
:math:`\frac{2}{3}`


>>> F[3, 2]

    =
:math:`\frac{2}{3}`


>>> F[-3, 2]

    =
:math:`-\frac{2}{3}`



We can use conditional delayed assignments to define     symbols with values conditioned to the context. For example,

>>> ClearAll[a,b]; a/; b>0:= 3



Set :math:`a` to have a value of :math:`3` if certain variable :math:`b` is positive.    So, if this variable is not set, :math:`a` stays unevaluated:

>>> a

    =
:math:`a`



If now we assign a positive value to :math:`b`, then :math:`a` is evaluated:

>>> b=2; a

    =
:math:`3`


