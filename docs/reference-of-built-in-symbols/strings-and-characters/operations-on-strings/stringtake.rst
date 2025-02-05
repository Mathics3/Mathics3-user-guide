StringTake
==========

`WMA link <https://reference.wolfram.com/language/ref/StringTake.html>`_


:code:`StringTake` [":math:`string`", :math:`n`]
    gives the first :math:`n` characters in :math:`string`.

:code:`StringTake` [":math:`string`", -:math:`n`]
    gives the last :math:`n` characters in :math:`string`.

:code:`StringTake` [":math:`string`", {:math:`n`}]
    gives the :math:`n`th character in :math:`string`.

:code:`StringTake` [":math:`string`", {:math:`m`, :math:`n`}]
    gives characters :math:`m` through :math:`n` in :math:`string`.

:code:`StringTake` [":math:`string`", {:math:`m`, :math:`n`, :math:`s`}]
    gives characters :math:`m` through :math:`n` in steps of :math:`s`.

:code:`StringTake` [{:math:`s_1`, :math:`s_2`, ...} :math:`spec`}]
    gives the list of results for each of the :math:`si`.





>>> StringTake["abcde", 2]
  = ab
>>> StringTake["abcde", 0]

>>> StringTake["abcde", -2]
  = de
>>> StringTake["abcde", {2}]
  = b
>>> StringTake["abcd", {2,3}]
  = bc
>>> StringTake["abcdefgh", {1, 5, 2}]
  = ace

Take the last 2 characters from several strings:

>>> StringTake[{"abcdef", "stuv", "xyzw"}, -2]
  = {ef, uv, zw}

StringTake also supports standard sequence specifications

>>> StringTake["abcdef", All]
  = abcdef
