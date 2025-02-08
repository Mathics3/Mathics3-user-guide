TraceBuiltins
=============


:code:`TraceBuiltins` [:math:`expr`]
    Evaluate :math:`expr` and then print a list of the Built-in Functions called           in evaluating :math:`expr` along with the number of times is each called,           and combined elapsed time in milliseconds spent in each.





Sort Options:



- count

- name

- time




>>> TraceBuiltins[Graphics3D[Tetrahedron[]]] (* See console log *)
    =

.. image:: tmpojkw6p41.png
    :align: center




By default, the output is sorted by the name:

>>> TraceBuiltins[Times[x, x]] (* See console log *)
    =

:math:`x^2`



By default, the output is sorted by the number of calls of the builtin from     highest to lowest:

>>> TraceBuiltins[Times[x, x], SortBy->"count"] (* See console log *)
    =

:math:`x^2`



You can have results ordered by name, or time.

Trace an expression and list the result by time from highest to lowest.

>>> TraceBuiltins[Times[x, x], SortBy->"time"] (* See console log *)
    =

:math:`x^2`


