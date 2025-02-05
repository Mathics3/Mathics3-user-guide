$RandomState
============

`WMA link <https://reference.wolfram.com/language/ref/RandomState.html>`_

:code:`$RandomState`
    is a long number representing the internal state of the pseudo-random number generator.





>>> Mod[$RandomState, 10^100]
  = ...
>>> IntegerLength[$RandomState]
  = ...

So far, it is not possible to assign values to :code:`$RandomState` .

>>> $RandomState = 42
  = 42

Not even to its own value:

>>> $RandomState = $RandomState;

