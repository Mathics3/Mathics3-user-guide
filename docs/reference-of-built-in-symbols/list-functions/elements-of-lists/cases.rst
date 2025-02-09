Cases
=====

`WMA link <https://reference.wolfram.com/language/ref/Cases.html>`_


:code:`Cases` [:math:`list`, :math:`pattern`]
    returns the elements of :math:`list` that match :math:`pattern`.

:code:`Cases` [:math:`list`, :math:`pattern`, :math:`ls`]
    returns the elements matching at levelspec :math:`ls`.

:code:`Cases` [:math:`list`, :math:`pattern`, Heads->:math:`bool`]
    Match including the head of the expression in the search.





>>> Cases[{a, 1, 2.5, "string"}, _Integer|_Real]

    =
:math:`\left\{1,2.5\right\}`


>>> Cases[_Complex][{1, 2I, 3, 4-I, 5}]

    =
:math:`\left\{2 I,4-I\right\}`



Find symbols among the elements of an expression:

>>> Cases[{b, 6, \[Pi]}, _Symbol]

    =
:math:`\left\{b, \pi \right\}`



Also include the head of the expression in the previous search:

>>> Cases[{b, 6, \[Pi]}, _Symbol, Heads -> True]

    =
:math:`\left\{\text{List},b, \pi \right\}`


