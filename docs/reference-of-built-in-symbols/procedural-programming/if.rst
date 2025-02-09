If
==

`WMA link <https://reference.wolfram.com/language/ref/If.html>`_


:code:`If` [:math:`cond`, :math:`pos`, :math:`neg`]
    returns :math:`pos` if :math:`cond` evaluates to :code:`True` , and :math:`neg` if it evaluates to
    :code:`False` .

:code:`If` [:math:`cond`, :math:`pos`, :math:`neg`, :math:`other`]
    returns :math:`other` if :math:`cond` evaluates to neither :code:`True`  nor :code:`False` .

:code:`If` [:math:`cond`, :math:`pos`]
    returns :code:`Null`  if :math:`cond` evaluates to :code:`False` .





>>> If[1<2, a, b]

    =
:math:`a`



If the second branch is not specified, :code:`Null`  is taken:

>>> If[1<2, a]

    =
:math:`a`


>>> If[False, a] //FullForm

    =
:math:`\text{Null}`



You might use comments (inside :code:`(*`  and :code:`*)` ) to make the branches of :code:`If` 
more readable:

>>> If[a, (*then*) b, (*else*) c];


