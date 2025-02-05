StringSplit
===========

`WMA link <https://reference.wolfram.com/language/ref/StringSplit.html>`_


:code:`StringSplit` [:math:`s`]
    splits the string :math:`s` at whitespace, discarding the whitespace and returning a list of strings.

:code:`StringSplit` [:math:`s`, :math:`pattern`]
    splits :math:`s` into substrings separated by delimiters matching the string expression :math:`pattern`.

:code:`StringSplit` [:math:`s`, {:math:`p_1`, :math:`p_2`, ...}]
    splits :math:`s` at any of the :math:`p_i` patterns.

:code:`StringSplit` [{:math:`s_1`, :math:`s_2`, ...}, {:math:`d_1`, :math:`d_2`, ...}]
    returns a list with the result of applying the function to each element.





>>> StringSplit["abc,123", ","]
  = {abc, 123}

By default any number of whitespace characters are used to at a delimiter:

>>> StringSplit["  abc    123  "]
  = {abc, 123}

However if you want instead to use only a *single* character for each delimiter, use :code:`WhiteSpaceCharacter` :

>>> StringSplit["  abc    123  ", WhitespaceCharacter]
  = {, , abc, , , , 123, , }
>>> StringSplit["abc,123.456", {",", "."}]
  = {abc, 123, 456}
>>> StringSplit["a  b    c", RegularExpression[" +"]]
  = {a, b, c}
>>> StringSplit[{"a  b", "c  d"}, RegularExpression[" +"]]
  = {{a, b}, {c, d}}
>>> StringSplit["x", "x"]
  = {}

Split using a delmiter that has nonzero list of 12's

>>> StringSplit["12312123", "12"..]
  = {3, 3}
