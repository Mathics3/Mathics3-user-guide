ClearTrace
==========


:code:`ClearTrace[]`
    Clear the statistics collected for Built-in Functions





First, set up Builtin-function tracing:

>>> $TraceBuiltins = True
  = True

Dump Builtin-Function statistics gathered in running that assignment:

>>> PrintTrace[]

>>> ClearTrace[]

>>> $TraceBuiltins = False
  = False
