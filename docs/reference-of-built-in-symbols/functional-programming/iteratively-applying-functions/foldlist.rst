FoldList
========

`WMA link <https://reference.wolfram.com/language/ref/FoldList.html>`_


:code:`FoldList` [:math:`f`, :math:`x`, :math:`list`]
    returns a list starting with :math:`x`, where each element is
    the result of applying the binary operator :math:`f` to the previous
    result and the next element of :math:`list`.

:code:`FoldList` [:math:`f`, :math:`list`]
    is equivalent to :code:`FoldList[:math:`f`, First[:math:`list`], Rest[:math:`list`]]` .





>>> FoldList[f, x, {1, 2, 3}]

    =
:math:`\left\{x,f\left[x,1\right],f\left[f\left[x,1\right],2\right],f\left[f\left[f\left[x,1\right],2\right],3\right]\right\}`


>>> FoldList[Times, {1, 2, 3}]

    =
:math:`\left\{1,2,6\right\}`


