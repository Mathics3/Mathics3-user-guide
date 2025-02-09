Values
======

`WMA link <https://reference.wolfram.com/language/ref/Values.html>`_


:code:`Values` [:code:`<|` :math:`key_1` :code:`->`  :math:`val_1`, :math:`key_2` -> :math:`val_2`, ...:code:`|>` ]
    return a list of the values :math:`val_i` in an association.

:code:`Values` [{:math:`key_1` :code:`->`  :math:`val_1`, :math:`key_2` :code:`->`  :math:`val_2`, ...}]
    return a list of the :math:`val_i` in a list of rules.





>>> Values[<|a -> x, b -> y|>]

    =
:math:`\left\{x,y\right\}`


>>> Values[{a -> x, b -> y}]

    =
:math:`\left\{x,y\right\}`



Values automatically threads over lists:

>>> Values[{<|a -> x, b -> y|>, {c -> z, {}}}]

    =
:math:`\left\{\left\{x,y\right\},\left\{z,\left\{\right\}\right\}\right\}`



Values are listed in the order of their appearance:

>>> Values[{c -> z, b -> y, a -> x}]

    =
:math:`\left\{z,y,x\right\}`


