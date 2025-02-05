EndPackage
==========

`WMA link <https://reference.wolfram.com/language/ref/EndPackage.html>`_


:code:`EndPackage[]`
    marks the end of a package, undoing a previous :code:`BeginPackage` .





After :code:`EndPackage` , the values of :code:`$Context`  and :code:`$ContextPath`  at the time of the :code:`BeginPackage`  call are restored, with the new package's context prepended to :code:`$ContextPath` .