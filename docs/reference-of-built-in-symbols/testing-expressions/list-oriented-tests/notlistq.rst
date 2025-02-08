NotListQ
========


:code:`NotListQ` [:math:`expr`]
    returns :code:`True`  if :math:`expr` is not a list. This function is primarily           used in function patterns for specifying type of a parameter.





Consider this definition for taking the deriviate :code:`Sin`  of a function:

>>> MyD[Sin[f_],x_?NotListQ] := D[f,x]*Cos[f]



=

We use "MyD" above to distinguish it from the Builtin :code:`D` . Now let's try it:

>>> MyD[Sin[2 x], x]
    =

:math:`2 \text{Cos}\left[2 x\right]`



And compare it with the Builtin deriviative function :code:`D` :

>>> D[Sin[2 x], x]
    =

:math:`2 \text{Cos}\left[2 x\right]`



Note however the pattern only matches if the :math:`x` parameter is not a list:

>>> MyD[{Sin[2], Sin[4]}, {1, 2}]
    =

:math:`\text{MyD}\left[\left\{\text{Sin}\left[2\right],\text{Sin}\left[4\right]\right\},\left\{1,2\right\}\right]`


