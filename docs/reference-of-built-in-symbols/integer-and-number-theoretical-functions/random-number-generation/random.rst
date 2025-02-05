Random
======

`Randomness <https://en.wikipedia.org/wiki/Randomness>`_ (`WMA link <https://reference.wolfram.com/language/ref/Random.html>`_)

:code:`Random[]`
    gives a pseudorandom real number in the range 0 to 1.

:code:`Random` [:math:`type`, :math:`range`]
    gives a pseudorandom number of the type :math:`type`, in the specified interval :math:`range`.
    Possible types are :code:`Integer` , :code:`Real`  or :code:`Complex` .





Legacy function. Superseded by `RandomReal </doc/reference-of-built-in-symbols/integer-and-number-theoretical-functions/random-number-generation/randomreal>`_, `RandomInteger </doc/reference-of-built-in-symbols/integer-and-number-theoretical-functions/random-number-generation/randominteger>`_, and `RandomComplex </doc/reference-of-built-in-symbols/integer-and-number-theoretical-functions/random-number-generation/randomcomplex>`_.

Four random numbers in the range 0..1:

>>> Table[Random[], {4}]
  = ...

Eight random integers in the range 1..100:

>>> Table[Random[Integer, {1, 100}], {8}]
  = ...
