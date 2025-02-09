Prepend
=======

`WMA link <https://reference.wolfram.com/language/ref/Prepend.html>`_


:code:`Prepend` [:math:`expr`, :math:`item`]
    returns :math:`expr` with :math:`item` prepended to its elements.

:code:`Prepend` [:math:`expr`]
    :code:`Prepend[:math:`elem`][:math:`expr`]`  is equivalent to :code:`Prepend[:math:`expr`,:math:`elem`]` .





:code:`Prepend`  is similar to :code:`Append` , but adds :math:`item` to the beginning
of :math:`expr`:

>>> Prepend[{2, 3, 4}, 1]

    =
:math:`\left\{1,2,3,4\right\}`



:code:`Prepend`  works on expressions with heads other than :code:`List` :

>>> Prepend[f[b, c], a]

    =
:math:`f\left[a,b,c\right]`



Unlike :code:`Join` , :code:`Prepend`  does not flatten lists in :math:`item`:

>>> Prepend[{c, d}, {a, b}]

    =
:math:`\left\{\left\{a,b\right\},c,d\right\}`


