Sequence
========

`WMA link <https://reference.wolfram.com/language/ref/Sequence.html>`_


:code:`Sequence` [:math:`x_1`, :math:`x_2`, ...]
    represents a sequence of arguments to a function.





:code:`Sequence`  is automatically spliced in, except when a function has attribute :code:`SequenceHold` 
(like assignment functions).

>>> f[x, Sequence[a, b], y]
  = f[x, a, b, y]
>>> Attributes[Set]
  = {HoldFirst, Protected, SequenceHold}
>>> a = Sequence[b, c];

>>> a
  = Sequence[b, c]

Apply :code:`Sequence`  to a list to splice in arguments:

>>> list = {1, 2, 3};

>>> f[Sequence @@ list]
  = f[1, 2, 3]

Inside :code:`Hold`  or a function with a held argument, :code:`Sequence`  is
spliced in at the first level of the argument:

>>> Hold[a, Sequence[b, c], d]
  = Hold[a, b, c, d]

If :code:`Sequence`  appears at a deeper level, it is left unevaluated:

>>> Hold[{a, Sequence[b, c], d}]
  = Hold[{a, Sequence[b, c], d}]
