ProductLog
==========

`WMA link <https://reference.wolfram.com/language/ref/ProductLog.html>`_


:code:`ProductLog` [:math:`z`]
    returns the principle solution for :math:`w` in :math:`z == wE^w`.

:code:`ProductLog` [:math:`k`, :math:`z`]
    gives the :math:`k`-th solution.





The defining equation:

>>> z == ProductLog[z] * E ^ ProductLog[z]
    =

:math:`\text{True}`



Some special values:

>>> ProductLog[0]
    =

:math:`0`


>>> ProductLog[E]
    =

:math:`1`


>>> ProductLog[-1.5]
    =

:math:`-0.0327837+1.54964 I`



The graph of :code:`ProductLog` :

>>> Plot[ProductLog[x], {x, -1/E, E}]
    =

.. image:: tmpnfffvemz.png
    :align: center



