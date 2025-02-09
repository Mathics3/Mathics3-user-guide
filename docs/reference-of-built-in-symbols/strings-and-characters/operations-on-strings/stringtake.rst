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

    =
:math:`\text{ab}`


>>> StringTake["abcde", 0]

    =
:math:`\text{}`


>>> StringTake["abcde", -2]

    =
:math:`\text{de}`


>>> StringTake["abcde", {2}]

    =
:math:`\text{b}`


>>> StringTake["abcd", {2,3}]

    =
:math:`\text{bc}`


>>> StringTake["abcdefgh", {1, 5, 2}]

    =
:math:`\text{ace}`



Take the last 2 characters from several strings:

>>> StringTake[{"abcdef", "stuv", "xyzw"}, -2]

    =
:math:`\left\{\text{ef},\text{uv},\text{zw}\right\}`



StringTake also supports standard sequence specifications

>>> StringTake["abcdef", All]

    =
:math:`\text{abcdef}`


