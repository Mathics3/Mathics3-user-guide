Check
=====

`WMA link <https://reference.wolfram.com/language/ref/Check.html>`_


:code:`Check` [:math:`expr`, :math:`failexpr`]
    evaluates :math:`expr`, and returns the result, unless messages were           generated, in which case it evaluates and :math:`failexpr` will be returned.

:code:`Check` [:math:`expr`, :math:`failexpr`, {s1::t1,s2::t2,...}]
    checks only for the specified messages.





Return err when a message is generated:

>>> Check[1/0, err]
  = err

Check only for specific messages:

>>> Check[Sin[0^0], err, Sin::argx]
  = Indeterminate
>>> Check[1/0, err, Power::infy]
  = err
