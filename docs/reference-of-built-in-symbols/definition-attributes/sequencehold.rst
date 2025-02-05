SequenceHold
============

`WMA link <https://reference.wolfram.com/language/ref/SequenceHold.html>`_


:code:`SequenceHold`
    is an attribute that prevents :code:`Sequence`  objects from being         spliced into a function's arguments.





Normally, :code:`Sequence`  will be spliced into a function:

>>> f[Sequence[a, b]]
  = f[a, b]

It does not for :code:`SequenceHold`  functions:

>>> SetAttributes[f, SequenceHold]

>>> f[Sequence[a, b]]
  = f[Sequence[a, b]]

E.g., :code:`Set`  has attribute :code:`SequenceHold`  to allow assignment of sequences to variables:

>>> s = Sequence[a, b];

>>> s
  = Sequence[a, b]
>>> Plus[s]
  = a + b
