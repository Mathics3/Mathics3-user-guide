LeviCivitaTensor
================

`Levi-Civita tensor <https://en.wikipedia.org/wiki/Levi-Civita_symbol>`_     (`WMA link <https://reference.wolfram.com/language/ref/LeviCivitaTensor.html>`_)


:code:`LeviCivitaTensor` [:math:`d`]
    gives the :math:`d`-dimensional Levi-Civita totally antisymmetric tensor.





>>> LeviCivitaTensor[3]

    =
:math:`\text{SparseArray}\left[\text{Automatic},\left\{3,3,3\right\},0,\left\{\left\{1,2,3\right\}->1,\left\{1,3,2\right\}->-1,\left\{2,1,3\right\}->-1,\left\{2,3,1\right\}->1,\left\{3,1,2\right\}->1,\left\{3,2,1\right\}->-1\right\}\right]`


>>> LeviCivitaTensor[3, List]

    =
:math:`\left\{\left\{\left\{0,0,0\right\},\left\{0,0,1\right\},\left\{0,-1,0\right\}\right\},\left\{\left\{0,0,-1\right\},\left\{0,0,0\right\},\left\{1,0,0\right\}\right\},\left\{\left\{0,1,0\right\},\left\{-1,0,0\right\},\left\{0,0,0\right\}\right\}\right\}`


