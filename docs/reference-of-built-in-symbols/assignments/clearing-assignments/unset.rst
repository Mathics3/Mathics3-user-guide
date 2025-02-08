Unset
=====

`WMA link <https://reference.wolfram.com/language/ref/Unset.html>`_


:code:`Unset` [:math:`x`]
    same as

:code:`:math:`x`=.`
    removes any value belonging to :math:`x`.





>>> a = 2
    =

:math:`2`


>>> a =.


>>> a
    =

:math:`a`



Unsetting an already unset or never defined variable will not change anything:

>>> a =.


>>> b =.



:code:`Unset`  can unset particular function values. It will print a message if no corresponding rule is found.

>>> f[x_] =.

    Unset::norep Assignment on f for f[x_] not found.
    =

:math:`\text{\$Failed}`


>>> f[x_] := x ^ 2


>>> f[3]
    =

:math:`9`


>>> f[x_] =.


>>> f[3]
    =

:math:`f\left[3\right]`



You can also unset :code:`OwnValues` , :code:`DownValues` , :code:`SubValues` , and :code:`UpValues`  directly. This is equivalent to setting them to :code:`{}` .

>>> f[x_] = x; f[0] = 1;


>>> DownValues[f] =.


>>> f[2]
    =

:math:`f\left[2\right]`



:code:`Unset`  threads over lists:

>>> a = b = 3;


>>> {a, {b}} =.
    =

:math:`\left\{\text{Null},\left\{\text{Null}\right\}\right\}`


