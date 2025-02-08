Last
====

`WMA link <https://reference.wolfram.com/language/ref/Last.html>`_


:code:`Last` [:math:`expr`]
    returns the last element in :math:`expr`.

:code:`Last` [:math:`expr`, :math:`def`]
    returns the last element in :math:`expr` if it exists or :math:`def` otherwise.





:code:`Last[:math:`expr`]`  is equivalent to :code:`:math:`expr`[[-1]]` .

>>> Last[{a, b, c}]
    =

:math:`c`



The first argument need not be a list:

>>> Last[a + b + c]
    =

:math:`c`



However, the first argument must be Nonatomic when there is a single argument:

>>> Last[10]

    Last::normal Nonatomic expression expected at position 1 in Last[10].
    =

:math:`\text{Last}\left[10\right]`



Or if it is not, but a second default argument is provided, that is     evaluated and returned:

>>> Last[10, 1+2]
    =

:math:`3`


>>> Last[{}]

    Last::nolast {} has zero length and no last element.
    =

:math:`\text{Last}\left[\left\{\right\}\right]`



As before, the first argument is empty, but since default argument is given,     evaluate and return the second argument:

>>> Last[{}, 1+2]
    =

:math:`3`


