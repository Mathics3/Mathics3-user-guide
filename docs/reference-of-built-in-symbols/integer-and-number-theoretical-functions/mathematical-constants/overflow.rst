Overflow
========

Numeric Overflow (`WMA <https://reference.wolfram.com/language/ref/Overflow.html>`_)

See also `Integer Overflow <https://en.wikipedia.org/wiki/Integer_overflow>`_.


:code:`Overflow[]`
    represents a number too large to be represented by Mathics.





>>> Exp[10.*^20]
  = Overflow[]
>>> Table[Exp[10.^k],{k, 3}]
  = {22026.5, 2.68812×10^43, Overflow[]}
>>> 1 / Underflow[]
  = Overflow[]
