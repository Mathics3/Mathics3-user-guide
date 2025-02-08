First
=====

`WMA link <https://reference.wolfram.com/language/ref/First.html>`_


:code:`First` [:math:`expr`]
    returns the first element in :math:`expr`.

:code:`First` [:math:`expr`, :math:`def`]
    returns the first element in :math:`expr` if it exists or :math:`def` otherwise.





:code:`First[:math:`expr`]`  is equivalent to :code:`:math:`expr`[[1]]` .

>>> First[{a, b, c}]
    =

:math:`a`



The first argument need not be a list:

>>> First[a + b + c]
    =

:math:`a`



However, the first argument must be Nonatomic when there is a single argument:

>>> First[x]

    First::normal Nonatomic expression expected at position 1 in First[x].
    =

:math:`\text{First}\left[x\right]`



Or if it is not, but a second default argument is provided, that is     evaluated and returned:

>>> First[10, 1+2]
    =

:math:`3`


>>> First[{}]

    First::nofirst {} has zero length and no first element.
    =

:math:`\text{First}\left[\left\{\right\}\right]`



As before, the first argument is empty, but a default argument is given,     evaluate and return the second argument:

>>> First[{}, 1+2]
    =

:math:`3`


