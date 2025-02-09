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

    =
:math:`\left\{\text{abc},\text{123}\right\}`



By default any number of whitespace characters are used to at a delimiter:

>>> StringSplit["  abc    123  "]

    =
:math:`\left\{\text{abc},\text{123}\right\}`



However if you want instead to use only a *single* character for each delimiter, use :code:`WhiteSpaceCharacter` :

>>> StringSplit["  abc    123  ", WhitespaceCharacter]

    =
:math:`\left\{\text{},\text{},\text{abc},\text{},\text{},\text{},\text{123},\text{},\text{}\right\}`


>>> StringSplit["abc,123.456", {",", "."}]

    =
:math:`\left\{\text{abc},\text{123},\text{456}\right\}`


>>> StringSplit["a  b    c", RegularExpression[" +"]]

    =
:math:`\left\{\text{a},\text{b},\text{c}\right\}`


>>> StringSplit[{"a  b", "c  d"}, RegularExpression[" +"]]

    =
:math:`\left\{\left\{\text{a},\text{b}\right\},\left\{\text{c},\text{d}\right\}\right\}`


>>> StringSplit["x", "x"]

    =
:math:`\left\{\right\}`



Split using a delmiter that has nonzero list of 12's

>>> StringSplit["12312123", "12"..]

    =
:math:`\left\{\text{3},\text{3}\right\}`


