StringRepeat
============

`WMA link <https://reference.wolfram.com/language/ref/StringRepeat.html>`_

:code:`StringRepeat` [":math:`string`", :math:`n`]
    gives :math:`string` repeated :math:`n` times.

:code:`StringRepeat` [":math:`string`", :math:`n`, :math:`max`]
    gives :math:`string` repeated :math:`n` times, but not more than :math:`max` characters.





>>> StringRepeat["abc", 3]
  = abcabcabc
>>> StringRepeat["abc", 10, 7]
  = abcabca
