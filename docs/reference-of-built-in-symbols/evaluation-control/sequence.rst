Sequence
========

`WMA link <https://reference.wolfram.com/language/ref/Sequence.html>`_


:code:`Sequence` [:math:`x_1`, :math:`x_2`, ...]
    represents a sequence of arguments to a function.





:code:`Sequence`  is automatically spliced in, except when a function has attribute :code:`SequenceHold` 
(like assignment functions).

>>> f[x, Sequence[a, b], y]

    =
:math:`f\left[x,a,b,y\right]`


>>> Attributes[Set]

    =
:math:`\left\{\text{HoldFirst},\text{Protected},\text{SequenceHold}\right\}`


>>> a = Sequence[b, c];


>>> a

    =
:math:`\text{Sequence}\left[b,c\right]`



Apply :code:`Sequence`  to a list to splice in arguments:

>>> list = {1, 2, 3};


>>> f[Sequence @@ list]

    =
:math:`f\left[1,2,3\right]`



Inside :code:`Hold`  or a function with a held argument, :code:`Sequence`  is
spliced in at the first level of the argument:

>>> Hold[a, Sequence[b, c], d]

    =
:math:`\text{Hold}\left[a,b,c,d\right]`



If :code:`Sequence`  appears at a deeper level, it is left unevaluated:

>>> Hold[{a, Sequence[b, c], d}]

    =
:math:`\text{Hold}\left[\left\{a,\text{Sequence}\left[b,c\right],d\right\}\right]`


