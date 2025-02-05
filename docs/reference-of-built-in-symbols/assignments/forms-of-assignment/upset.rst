UpSet
=====

`WMA link <https://reference.wolfram.com/language/ref/UpSet.html>`_


:math:`f`[:math:`x`] :code:`^=`  :math:`expression`
    evaluates :math:`expression` and assigns it to the value of :math:`f`[:math:`x`],           associating the value with :math:`x`.





:code:`UpSet`  creates an upvalue:

>>> a[b] ^= 3;

>>> DownValues[a]
  = {}
>>> UpValues[b]
  = {HoldPattern[a[b]] :> 3}

You can use :code:`UpSet`  to specify special values like format values.
However, these values will not be saved in :code:`UpValues` :

>>> Format[r] ^= "custom";

>>> r
  = custom
>>> UpValues[r]
  = {}
