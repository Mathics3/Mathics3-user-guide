String
======

`WMA link <https://reference.wolfram.com/language/ref/String.html>`_

:code:`String`
    is the head of strings.





>>> Head["abc"]
  = String
>>> "abc"
  = abc

Use :code:`InputForm`  to display quotes around strings:

>>> InputForm["abc"]
  = "abc"

:code:`FullForm`  also displays quotes:

>>> FullForm["abc" + 2]
  = Plus[2, "abc"]
