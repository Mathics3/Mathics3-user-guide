Length
======

`WMA link <https://reference.wolfram.com/language/ref/Length.html>`_


:code:`Length` [:math:`expr`]
    returns the number of elements in :math:`expr`.





Length of a list:

>>> Length[{1, 2, 3}]

    =
:math:`3`



:code:`Length`  operates on the :code:`FullForm`  of expressions:

>>> Length[Exp[x]]

    =
:math:`2`


>>> FullForm[Exp[x]]

    =
:math:`\text{Power}\left[E, x\right]`



The length of atoms is 0:

>>> Length[a]

    =
:math:`0`



Note that rational and complex numbers are atoms, although their
:code:`FullForm`  might suggest the opposite:

>>> Length[1/3]

    =
:math:`0`


>>> FullForm[1/3]

    =
:math:`\text{Rational}\left[1, 3\right]`


