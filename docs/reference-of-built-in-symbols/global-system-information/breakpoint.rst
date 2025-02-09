Breakpoint
==========

`Python breakpoint() <https://docs.python.org/3/library/functions.html#breakpoint>`_


:code:`Breakpoint[]`
    Invoke a Python breakpoint.
    
    This can be used for debugging the Mathics3 implementation, but       if you are familiar with Python, it might assist in debugging a Mathics3 programs       as well.
    
    By default, the Python debugger (:code:`pdb` ) is loaded. For loading other debuggers,       change the environment variable :code:`PYTHONBREAKPOINT` .






Mathics3 code includes a breakpoint handler function, :code:`mathics.disabled_breakpoint`  which     reports whether :code:`Breakpoint[]`  was encountered in Mathics3, or :code:`breakpoint()`  was encountered     in the Mathics3 source code. In contrast to :code:`pdb` , :code:`trepan3k`  and other handlers, this breakpoint     handler does not stop inside, it just reports.

Here is how to use :code:`mathics.disabled_breakpoint` :

>>> SetEnvironment["PYTHONBREAKPOINT" -> "mathics.disabled_breakpoint"];


>>> Breakpoint[]

    =
:math:`\text{Breakpoint}\left[\right]`



The environment variable :code:`PYTHONBREAKPOINT`  can be changed at runtime to switch     :code:`breakpoint()`  and :code:`Breakpoint[]`  behavior.