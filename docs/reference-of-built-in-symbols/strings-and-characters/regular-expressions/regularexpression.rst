RegularExpression
=================

`WMA link <https://reference.wolfram.com/language/ref/RegularExpression.html>`_


:code:`RegularExpression["regex"]`
    represents the regex specified by the string ":math:`regex`".





>>> StringSplit["1.23, 4.56  7.89", RegularExpression["(\\s|,)+"]]
    =

:math:`\left\{\text{1.23},\text{4.56},\text{7.89}\right\}`



:code:`RegularExpression`  just wraps a string to be interpreted as a regular expression, but are not evaluated as stand alone expressions:

>>> RegularExpression["[abc]"]
    =

:math:`\text{RegularExpression}\left[\text{[abc]}\right]`


