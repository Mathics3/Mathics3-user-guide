FindClusters
============

`WMA link <https://reference.wolfram.com/language/ref/FindClusters.html>`_


:code:`FindClusters` [:math:`list`]
    returns a list of clusters formed from the elements of :math:`list`. The number of cluster is determined
    automatically.

:code:`FindClusters` [:math:`list`, :math:`k`]
    returns a list of :math:`k` clusters formed from the elements of :math:`list`.





>>> FindClusters[{1, 2, 20, 10, 11, 40, 19, 42}]
  = {{1, 2, 20, 10, 11, 19}, {40, 42}}
>>> FindClusters[{25, 100, 17, 20}]
  = {{25, 17, 20}, {100}}
>>> FindClusters[{3, 6, 1, 100, 20, 5, 25, 17, -10, 2}]
  = {{3, 6, 1, 5, -10, 2}, {100}, {20, 25, 17}}
>>> FindClusters[{1, 2, 10, 11, 20, 21}]
  = {{1, 2}, {10, 11}, {20, 21}}
>>> FindClusters[{1, 2, 10, 11, 20, 21}, 2]
  = {{1, 2, 10, 11}, {20, 21}}
>>> FindClusters[{1 -> a, 2 -> b, 10 -> c}]
  = {{a, b}, {c}}
>>> FindClusters[{1, 2, 5} -> {a, b, c}]
  = {{a, b}, {c}}
>>> FindClusters[{1, 2, 3, 1, 2, 10, 100}, Method -> "Agglomerate"]
  = {{1, 2, 3, 1, 2, 10}, {100}}
>>> FindClusters[{1, 2, 3, 10, 17, 18}, Method -> "Agglomerate"]
  = {{1, 2, 3}, {10}, {17, 18}}
>>> FindClusters[{{1}, {5, 6}, {7}, {2, 4}}, DistanceFunction -> (Abs[Length[#1] - Length[#2]]&)]
  = {{{1}, {7}}, {{5, 6}, {2, 4}}}
>>> FindClusters[{"meep", "heap", "deep", "weep", "sheep", "leap", "keep"}, 3]
  = {{meep, deep, weep, keep}, {heap, leap}, {sheep}}

FindClusters' automatic distance function detection supports scalars, numeric tensors, boolean vectors and
strings.

The Method option must be either "Agglomerate" or "Optimize". If not specified, it defaults to "Optimize".
Note that the Agglomerate and Optimize methods usually produce different clusterings.

The runtime of the Agglomerate method is quadratic in the number of clustered points n, builds the clustering
from the bottom up, and is exact (no element of randomness). The Optimize method's runtime is linear in n,
Optimize builds the clustering from top down, and uses random sampling.