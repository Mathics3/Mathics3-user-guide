ReleaseHold
===========

`WMA link <https://reference.wolfram.com/language/ref/ReleaseHold.html>`_


:code:`ReleaseHold` [:math:`expr`]
    removes any :code:`Hold` , :code:`HoldForm` , :code:`HoldPattern`  or
    :code:`HoldComplete`  head from :math:`expr`.





>>> x = 3;


>>> Hold[x]
    =

:math:`\text{Hold}\left[x\right]`


>>> ReleaseHold[Hold[x]]
    =

:math:`3`


>>> ReleaseHold[y]
    =

:math:`y`


