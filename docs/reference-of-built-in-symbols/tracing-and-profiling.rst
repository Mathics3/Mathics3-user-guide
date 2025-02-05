Tracing and Profiling
=====================

The :code:`Trace`  builtins provide a Mathics3-oriented trace of what is getting evaluated and where the time is spent in evaluation.

With this, it may be possible for both users and implementers to follow how Mathics3 arrives at its results, or guide how to speed up expression evaluation.

Python `CProfile <https://docs.python.org/3/library/profile.html>`_ profiling is available via :code:`PythonCProfileEvaluation` .

.. toctree::
    :maxdepth: 2

    tracing-and-profiling/$tracebuiltins.rst
    tracing-and-profiling/$traceevaluation.rst
    tracing-and-profiling/cleartrace.rst
    tracing-and-profiling/printtrace.rst
    tracing-and-profiling/pythoncprofileevaluation.rst
    tracing-and-profiling/tracebuiltins.rst
    tracing-and-profiling/traceevaluation.rst

