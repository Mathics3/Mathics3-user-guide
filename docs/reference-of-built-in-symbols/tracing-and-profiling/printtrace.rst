PrintTrace
==========


:code:`PrintTrace[]`
    Print statistics collected for Built-in Functions





Sort Options:



- count

- name

- time




Note that in a browser the information only appears in a console.


Note: before :code:`$TraceBuiltins`  is set to :code:`True` , :code:`PrintTrace[]`  will print an empty
list.

>>> PrintTrace[] (* See console log *)


>>> $TraceBuiltins = True

    =
:math:`\text{True}`


>>> PrintTrace[SortBy -> "time"]


>>> $TraceBuiltins = False
    = False`

