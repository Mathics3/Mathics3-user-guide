ClusteringComponents
====================

`WMA link <https://reference.wolfram.com/language/ref/ClusteringComponents.html>`_


:code:`ClusteringComponents` [:math:`list`]
    forms clusters from :math:`list` and returns a list of cluster indices, in which each
    element shows the index of the cluster in which the corresponding element in :math:`list`
    ended up.

:code:`ClusteringComponents` [:math:`list`, :math:`k`]
    forms :math:`k` clusters from :math:`list` and returns a list of cluster indices, in which
    each element shows the index of the cluster in which the corresponding element in
    :math:`list` ended up.





For more detailed documentation regarding options and behavior, see FindClusters[].

>>> ClusteringComponents[{1, 2, 3, 1, 2, 10, 100}]
    =

:math:`\left\{1,1,1,1,1,1,2\right\}`


>>> ClusteringComponents[{10, 100, 20}, Method -> "KMeans"]
    =

:math:`\left\{1,0,1\right\}`


