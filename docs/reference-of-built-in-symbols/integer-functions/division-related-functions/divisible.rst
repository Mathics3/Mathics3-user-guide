Divisible
=========

`WMA link <https://reference.wolfram.com/language/ref/Divisible.html>`_


:code:`Divisible` [:math:`n`, :math:`m`]
    returns :code:`True`  if :math:`n` is divisible by :math:`m`, and :code:`False`  otherwise.





<ul>
<li>:math:`n` is divisible by :math:`m` if :math:`n` is the product of :math:`m` by an integer.
<li>:code:`Divisible[:math:`n`,:math:`m`]`  is effectively equivalent to :code:`Mod[:math:`n`,:math:`m`]==0` .

Test whether the number 10 is divisible by 2

>>> Divisible[10, 2]
    =

:math:`\text{True}`



But the other way around is False: 2 is not divisible by 10:

>>> Divisible[2, 10]
    =

:math:`\text{False}`


