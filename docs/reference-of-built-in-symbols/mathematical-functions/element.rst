Element
=======

`Element of <https://en.wikipedia.org/wiki/Element_(mathematics)>`_     `WMA link <https://reference.wolfram.com/language/ref/Element.html>`_


:code:`Element` [:math:`expr`, :math:`domain`]
    returns :math:`True` if :math:`expr` is an element of :math:`domain`

:code:`Element` [:math:`expr_1`|:math:`expr_2`|..., :math:`domain`]
    returns :math:`True` if all the :math:`expr_i` belongs to :math:`domain`, and     :math:`False` if one of the items doesn't.






Check if :math:`3` and :math:`a` are both integers. If :math:`a` is not defined, then :code:`Element`  reduces the condition:

>>> Element[3 | a, Integers]
  = Element[a, Integers]

Notice that standard domain names (:code:`Primes` , :code:`Integers` , :code:`Rationals` , :code:`Algebraics` , :code:`Reals` , :code:`Complexes` , and :code:`Booleans` )    are in plural form. If a singular form is used, a warning is shown:

>>> Element[a, Real]
  = Element[a, Real]
