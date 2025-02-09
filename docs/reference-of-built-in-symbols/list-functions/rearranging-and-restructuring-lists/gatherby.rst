GatherBy
========

`WMA link <https://reference.wolfram.com/language/ref/GatherBy.html>`_


:code:`GatherBy` [:math:`list`, :math:`f`]
    gathers elements of :math:`list` into sub lists of items whose image       under :math:`f` identical.

:code:`GatherBy` [:math:`list`, {:math:`f`, :math:`g`, ...}]
    gathers elements of :math:`list` into sub lists of items whose image       under :math:`f` identical. Then, gathers these sub lists again into sub       sub lists, that are identical under :math:`g`.





>>> GatherBy[{{1, 3}, {2, 2}, {1, 1}}, Total]

    =
:math:`\left\{\left\{\left\{1,3\right\},\left\{2,2\right\}\right\},\left\{\left\{1,1\right\}\right\}\right\}`


>>> GatherBy[{"xy", "abc", "ab"}, StringLength]

    =
:math:`\left\{\left\{\text{xy},\text{ab}\right\},\left\{\text{abc}\right\}\right\}`


>>> GatherBy[{{2, 0}, {1, 5}, {1, 0}}, Last]

    =
:math:`\left\{\left\{\left\{2,0\right\},\left\{1,0\right\}\right\},\left\{\left\{1,5\right\}\right\}\right\}`


>>> GatherBy[{{1, 2}, {2, 1}, {3, 5}, {5, 1}, {2, 2, 2}}, {Total, Length}]

    =
:math:`\left\{\left\{\left\{\left\{1,2\right\},\left\{2,1\right\}\right\}\right\},\left\{\left\{\left\{3,5\right\}\right\}\right\},\left\{\left\{\left\{5,1\right\}\right\},\left\{\left\{2,2,2\right\}\right\}\right\}\right\}`


