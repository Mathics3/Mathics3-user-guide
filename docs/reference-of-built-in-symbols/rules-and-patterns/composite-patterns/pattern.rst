Pattern
=======

`WMA link <https://reference.wolfram.com/language/ref/Pattern.html>`_


:code:`Pattern` [:math:`symb`, :math:`pat`]
    same as

:math:`symb` :code:`:`  :math:`pat`
    assigns the name :math:`symb` to the pattern :math:`pat`.

:math:`symb`:code:`_` :math:`head`
    is equivalent to :math:`symb`:code:` : _` :math:`head` (accordingly with :code:`__`          and :code:`___` ).

:math:`symb`:code:` : ` :math:`pat`:code:` : ` :math:`default`
    is a pattern with name :math:`symb` and default value :math:`default`,         equivalent to :code:`Optional` [:math:`pat` : :math:`symb`, :math:`default`].





>>> FullForm[a_b]
  = Pattern[a, Blank[b]]
>>> FullForm[a:_:b]
  = Optional[Pattern[a, Blank[]], b]

:code:`Pattern`  has attribute :code:`HoldFirst` , so it does not evaluate its name:

>>> x = 2
  = 2
>>> x_
  = x_

Nested :code:`Pattern`  assigns multiple names to the same pattern. Still,     the last parameter is the default value.

>>> f[y] /. f[a:b,_:d] -> {a, b}
  = f[y]

This is equivalent to:

>>> f[a] /. f[a:_:b] -> {a, b}
  = {a, b}

:code:`FullForm` :

>>> FullForm[a:b:c:d:e]
  = Optional[Pattern[a, b], Optional[Pattern[c, d], e]]
>>> f[] /. f[a:_:b] -> {a, b}
  = {b, b}
