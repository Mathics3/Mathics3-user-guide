ToString
========

`WMA link <https://reference.wolfram.com/language/ref/ToString.html>`_

:code:`ToString` [:math:`expr`]
    returns a string representation of :math:`expr`.

:code:`ToString` [:math:`expr`, :math:`form`]
    returns a string representation of :math:`expr` in the form :math:`form`.





>>> ToString[2]

    =
:math:`\text{2}`


>>> ToString[2] // InputForm

    =
:math:`\text{\`{}\`{}2''}`


>>> ToString[a+b]

    =
:math:`\text{a + b}`


>>> "U" <> 2

    StringJoin::string String expected.

    =
:math:`\text{U}\text{<>}2`


>>> "U" <> ToString[2]

    =
:math:`\text{U2}`


>>> ToString[Integrate[f[x],x], TeXForm]

    =
:math:`\text{$\backslash$int f$\backslash$left[x$\backslash$right] $\backslash$, dx}`


