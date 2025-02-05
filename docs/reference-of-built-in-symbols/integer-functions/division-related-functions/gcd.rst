GCD
===

`WMA link <https://reference.wolfram.com/language/ref/GCD.html>`_


:code:`GCD` [:math:`n_1`, :math:`n_2`, ...]
    computes the greatest common divisor of the given integers.





>>> GCD[20, 30]
  = 10
>>> GCD[10, y]
  = GCD[10, y]

:code:`GCD`  is :code:`Listable` :

>>> GCD[4, {10, 11, 12, 13, 14}]
  = {2, 1, 4, 1, 2}

:code:`GCD`  does not work for rational numbers and Gaussian integers yet.