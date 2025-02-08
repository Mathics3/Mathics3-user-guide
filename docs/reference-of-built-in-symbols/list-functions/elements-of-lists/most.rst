Most
====

`WMA link <https://reference.wolfram.com/language/ref/Most.html>`_


:code:`Most` [:math:`expr`]
    returns :math:`expr` with the last element removed.





:code:`Most[:math:`expr`]`  is equivalent to :code:`:math:`expr`[[;;-2]]` .

>>> Most[{a, b, c}]
    =

:math:`\left\{a,b\right\}`


>>> Most[a + b + c]
    =

:math:`a+b`


>>> Most[x]

    Most::normal Nonatomic expression expected at position 1 in Most[x].
    =

:math:`\text{Most}\left[x\right]`


