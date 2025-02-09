$TraceBuiltins
==============


:code:`$TraceBuiltins`
    A Boolean Built-in variable when True collects function evaluation statistics.





Setting this variable True will enable statistics collection for Built-in functions that are evaluated.
In contrast to :code:`TraceBuiltins[]`  statistics are accumulated and over several inputs,and are not shown after each input is evaluated.

By default, this setting is False.

>>> $TraceBuiltins = True

    =
:math:`\text{True}`


>>> $TraceBuiltins = False
    = False`


Tracing is enabled, so the expressions entered and evaluated will have statistics collected for the evaluations.

>>> x

    =
:math:`x`



To print the statistics collected, use :code:`PrintTrace[]` :

>>> PrintTrace[]



To  clear statistics collected use :code:`ClearTrace[]` :

>>> ClearTrace[]



:code:`$TraceBuiltins`   cannot be set to a non-boolean value.

>>> $TraceBuiltins = x

    $TraceBuiltins::bool x should be True or False.

    =
:math:`x`


