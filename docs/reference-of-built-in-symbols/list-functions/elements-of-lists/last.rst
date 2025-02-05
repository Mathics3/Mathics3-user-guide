Last
====

`WMA link <https://reference.wolfram.com/language/ref/Last.html>`_


:code:`Last` [:math:`expr`]
    returns the last element in :math:`expr`.

:code:`Last` [:math:`expr`, :math:`def`]
    returns the last element in :math:`expr` if it exists or :math:`def` otherwise.





:code:`Last[:math:`expr`]`  is equivalent to :code:`:math:`expr`[[-1]]` .

>>> Last[{a, b, c}]
  = c

The first argument need not be a list:

>>> Last[a + b + c]
  = c

However, the first argument must be Nonatomic when there is a single argument:

>>> Last[10]
  = Last[10]

Or if it is not, but a second default argument is provided, that is     evaluated and returned:

>>> Last[10, 1+2]
  = 3
>>> Last[{}]
  = Last[{}]

As before, the first argument is empty, but since default argument is given,     evaluate and return the second argument:

>>> Last[{}, 1+2]
  = 3
