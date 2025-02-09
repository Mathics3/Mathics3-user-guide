DeleteCases
===========

`WMA link <https://reference.wolfram.com/language/ref/DeleteCases.html>`_


:code:`DeleteCases` [:math:`list`, :math:`pattern`]
    returns the elements of :math:`list` that do not match :math:`pattern`.

:code:`DeleteCases` [:math:`list`, :math:`pattern`, :math:`levelspec`]
    removes all parts of :math:`list` on levels specified by :math:`levelspec` that match pattern (not fully implemented).

:code:`DeleteCases` [:math:`list`, :math:`pattern`, :math:`levelspec`, :math:`n`]
    removes the first :math:`n` parts of :math:`list` that match :math:`pattern`.





>>> DeleteCases[{a, 1, 2.5, "string"}, _Integer|_Real]

    =
:math:`\left\{a,\text{string}\right\}`


>>> DeleteCases[{a, b, 1, c, 2, 3}, _Symbol]

    =
:math:`\left\{1,2,3\right\}`


