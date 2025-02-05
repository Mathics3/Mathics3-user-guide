Keys
====

`WMA link <https://reference.wolfram.com/language/ref/Keys.html>`_


:code:`Keys` [:code:`<|`  :math:`key_1` :code:`->`  :math:`val_1`, :math:`key_2` :code:`->`  :math:`val_2`, ...:code:`|>` ]
    return a list of the keys :math:`keyi` in an association.

:code:`Keys` [{:math:`key_1` :code:`->`  :math:`val_1`, :math:`key_2` :code:`->`  :math:`val_2`, ...}]
    return a list of the :math:`key_i` in a list of rules.





>>> Keys[<|a -> x, b -> y|>]
  = {a, b}
>>> Keys[{a -> x, b -> y}]
  = {a, b}

Keys automatically threads over lists:

>>> Keys[{<|a -> x, b -> y|>, {w -> z, {}}}]
  = {{a, b}, {w, {}}}

Keys are listed in the order of their appearance:

>>> Keys[{c -> z, b -> y, a -> x}]
  = {c, b, a}
