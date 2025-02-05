Values
======

`WMA link <https://reference.wolfram.com/language/ref/Values.html>`_


:code:`Values` [:code:`<|` :math:`key_1` :code:`->`  :math:`val_1`, :math:`key_2` -> :math:`val_2`, ...:code:`|>` ]
    return a list of the values :math:`val_i` in an association.

:code:`Values` [{:math:`key_1` :code:`->`  :math:`val_1`, :math:`key_2` :code:`->`  :math:`val_2`, ...}]
    return a list of the :math:`val_i` in a list of rules.





>>> Values[<|a -> x, b -> y|>]
  = {x, y}
>>> Values[{a -> x, b -> y}]
  = {x, y}

Values automatically threads over lists:

>>> Values[{<|a -> x, b -> y|>, {c -> z, {}}}]
  = {{x, y}, {z, {}}}

Values are listed in the order of their appearance:

>>> Values[{c -> z, b -> y, a -> x}]
  = {z, y, x}
