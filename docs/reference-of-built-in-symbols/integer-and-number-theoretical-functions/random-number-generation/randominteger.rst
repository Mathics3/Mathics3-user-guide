RandomInteger
=============

`WMA link <https://reference.wolfram.com/language/ref/RandomInteger.html>`_

:code:`RandomInteger` [{:math:`min`, :math:`max`}]
    yields a pseudorandom integer in the range from :math:`min` to :math:`max` inclusive.

:code:`RandomInteger` [:math:`max`]
    yields a pseudorandom integer in the range from 0 to :math:`max` inclusive.

:code:`RandomInteger[]`
    gives 0 or 1.

:code:`RandomInteger` [:math:`range`, :math:`n`]
    gives a list of :math:`n` pseudorandom integers.

:code:`RandomInteger` [:math:`range`, {:math:`n_1`, :math:`n_2`, ...}]
    gives a nested list of pseudorandom integers.





>>> RandomInteger[{1, 5}]
  = ...
>>> RandomInteger[100, {2, 3}] // TableForm
  = ...   ...   ...
    
    ...   ...   ...

Calling :code:`RandomInteger`  changes :code:`$RandomState` :

>>> previousState = $RandomState;

>>> RandomInteger[]
  = ...
>>> $RandomState != previousState
  = True
