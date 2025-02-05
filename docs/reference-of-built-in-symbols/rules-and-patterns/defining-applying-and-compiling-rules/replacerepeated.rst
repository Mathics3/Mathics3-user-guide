ReplaceRepeated
===============

`WMA link <https://reference.wolfram.com/language/ref/ReplaceRepeated.html>`_


:code:`ReplaceRepeated` [:math:`expr`, :math:`x` -> :math:`y`]
    same as

:code:`:math:`expr` //. :math:`x` -> :math:`y``
    repeatedly applies the rule :code:`:math:`x` -> :math:`y``  to :math:`expr` until
    the result no longer changes.





>>> a+b+c //. c->d
  = a + b + d
>>> f = ReplaceRepeated[c->d];

>>> f[a+b+c]
  = a + b + d
>>> Clear[f];


Simplification of logarithms:

>>> logrules = {Log[x_ * y_] :> Log[x] + Log[y], Log[x_ ^ y_] :> y * Log[x]};

>>> Log[a * (b * c) ^ d ^ e * f] //. logrules
  = Log[a] + Log[f] + (Log[b] + Log[c]) d ^ e

:code:`ReplaceAll`  just performs a single replacement:

>>> Log[a * (b * c) ^ d ^ e * f] /. logrules
  = Log[a] + Log[f (b c) ^ d ^ e]
