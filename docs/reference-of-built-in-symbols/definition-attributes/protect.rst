Protect
=======

`WMA link <https://reference.wolfram.com/language/ref/Protect.html>`_


:code:`Protect` [:math:`s_1`, :math:`s_2`, ...]
    sets the attribute :code:`Protected`  for the symbols :math:`si`.

:code:`Protect` [:math:`str_1`, :math:`str_2`, ...]
    protects all symbols whose names textually match :math:`stri`.





>>> A = {1, 2, 3};

>>> Protect[A]

>>> A[[2]] = 4;

>>> A
  = {1, 2, 3}
