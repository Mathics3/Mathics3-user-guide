First
=====

`WMA link <https://reference.wolfram.com/language/ref/First.html>`_


:code:`First` [:math:`expr`]
    returns the first element in :math:`expr`.

:code:`First` [:math:`expr`, :math:`def`]
    returns the first element in :math:`expr` if it exists or :math:`def` otherwise.





:code:`First[:math:`expr`]`  is equivalent to :code:`:math:`expr`[[1]]` .

>>> First[{a, b, c}]
  = a

The first argument need not be a list:

>>> First[a + b + c]
  = a

However, the first argument must be Nonatomic when there is a single argument:

>>> First[x]
  = First[x]

Or if it is not, but a second default argument is provided, that is     evaluated and returned:

>>> First[10, 1+2]
  = 3
>>> First[{}]
  = First[{}]

As before, the first argument is empty, but a default argument is given,     evaluate and return the second argument:

>>> First[{}, 1+2]
  = 3
