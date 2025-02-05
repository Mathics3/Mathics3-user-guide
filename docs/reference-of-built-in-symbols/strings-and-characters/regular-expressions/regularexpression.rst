RegularExpression
=================

`WMA link <https://reference.wolfram.com/language/ref/RegularExpression.html>`_


:code:`RegularExpression["regex"]`
    represents the regex specified by the string ":math:`regex`".





>>> StringSplit["1.23, 4.56  7.89", RegularExpression["(\\s|,)+"]]
  = {1.23, 4.56, 7.89}

:code:`RegularExpression`  just wraps a string to be interpreted as a regular expression, but are not evaluated as stand alone expressions:

>>> RegularExpression["[abc]"]
  = RegularExpression[[abc]]
