Rest
====

`WMA link <https://reference.wolfram.com/language/ref/Rest.html>`_


:code:`Rest` [:math:`expr`]
    returns :math:`expr` with the first element removed.





:code:`Rest[:math:`expr`]`  is equivalent to :code:`:math:`expr`[[2;;]]` .

>>> Rest[{a, b, c}]
    =

:math:`\left\{b,c\right\}`


>>> Rest[a + b + c]
    =

:math:`b+c`


>>> Rest[x]

    Rest::normal Nonatomic expression expected at position 1 in Rest[x].
    =

:math:`\text{Rest}\left[x\right]`


>>> Rest[{}]

    Rest::norest Cannot take Rest of expression {} with length zero.
    =

:math:`\text{Rest}\left[\left\{\right\}\right]`


