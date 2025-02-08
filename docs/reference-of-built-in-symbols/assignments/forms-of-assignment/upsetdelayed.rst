UpSetDelayed
============

`WMA link <https://reference.wolfram.com/language/ref/UpSetDelayed.html>`_


:code:`UpSetDelayed` [:math:`expression`, :math:`value`]
    same as

:math:`expression` :code:`^:=`  :math:`value`
    assigns :math:`expression` to the value of :math:`f`[:math:`x`]            (without evaluating :math:`expression`), associating the value with :math:`x`.





>>> a[b] ^:= x


>>> x = 2;


>>> a[b]
    =

:math:`2`


>>> UpValues[b]
    =

:math:`\left\{\text{HoldPattern}\left[a\left[b\right]\right]\text{:>}x\right\}`


