ModularInverse
==============

`Modular multiplicative inverse <https://en.wikipedia.org/wiki/Modular_multiplicative_inverse>`_ (`SymPy <https://docs.sympy.org/latest/modules/core.html#sympy.core.numbers.mod_inverse>`_, `WMA <https://reference.wolfram.com/language/ref/ModularInverse.html>`_)


:code:`ModularInverse` [:math:`k`, :math:`n`]
    returns the modular inverse :math:`k`^(-1) mod :math:`n`.





:code:`ModularInverse[:math:`k`,:math:`n`]`  gives the smallest positive integer :math:`r` where the remainder     of the division of :math:`r` x :math:`k` by :math:`n` is equal to 1.

>>> ModularInverse[2, 3]

    =
:math:`2`



The following is be True for all values :math:`n`, :math:`k` which have a modular inverse:

>>> k = 2; n = 3; Mod[ModularInverse[k, n] * k, n] == 1

    =
:math:`\text{True}`



Some modular inverses just do not exists. For example when :math:`k` is a multiple of :math:`n`:

>>> ModularInverse[k, k]

    =
:math:`\text{ModularInverse}\left[2,2\right]`


>>> Clear[k, n]
    = `

