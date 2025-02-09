SparseArray
===========

`WMA link <https://reference.wolfram.com/language/ref/SparseArray.html>`_


:code:`SparseArray` [:math:`rules`]
    Builds a sparse array according to the list of :math:`rules`.

:code:`SparseArray` [:math:`rules`, :math:`dims`]
    Builds a sparse array of dimensions :math:`dims` according to the :math:`rules`.

:code:`SparseArray` [:math:`list`]
    Builds a sparse representation of :math:`list`.





>>> SparseArray[{{1, 2} -> 1, {2, 1} -> 1}]

    =
:math:`\text{SparseArray}\left[\text{Automatic},\left\{2,2\right\},0,\left\{\left\{1,2\right\}->1,\left\{2,1\right\}->1\right\}\right]`


>>> SparseArray[{{1, 2} -> 1, {2, 1} -> 1}, {3, 3}]

    =
:math:`\text{SparseArray}\left[\text{Automatic},\left\{3,3\right\},0,\left\{\left\{1,2\right\}->1,\left\{2,1\right\}->1\right\}\right]`


>>> M=SparseArray[{{0, a}, {b, 0}}]

    =
:math:`\text{SparseArray}\left[\text{Automatic},\left\{2,2\right\},0,\left\{\left\{1,2\right\}->a,\left\{2,1\right\}->b\right\}\right]`


>>> M //Normal

    =
:math:`\left\{\left\{0,a\right\},\left\{b,0\right\}\right\}`


