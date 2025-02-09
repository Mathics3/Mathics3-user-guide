SequenceHold
============

`WMA link <https://reference.wolfram.com/language/ref/SequenceHold.html>`_


:code:`SequenceHold`
    is an attribute that prevents :code:`Sequence`  objects from being         spliced into a function's arguments.





Normally, :code:`Sequence`  will be spliced into a function:

>>> f[Sequence[a, b]]

    =
:math:`f\left[a,b\right]`



It does not for :code:`SequenceHold`  functions:

>>> SetAttributes[f, SequenceHold]


>>> f[Sequence[a, b]]

    =
:math:`f\left[\text{Sequence}\left[a,b\right]\right]`



E.g., :code:`Set`  has attribute :code:`SequenceHold`  to allow assignment of sequences to variables:

>>> s = Sequence[a, b];


>>> s

    =
:math:`\text{Sequence}\left[a,b\right]`


>>> Plus[s]

    =
:math:`a+b`


