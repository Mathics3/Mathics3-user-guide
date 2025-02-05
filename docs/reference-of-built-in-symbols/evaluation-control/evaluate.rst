Evaluate
========

`WMA link <https://reference.wolfram.com/language/ref/Evaluate.html>`_


:code:`Evaluate` [:math:`expr`]
    forces evaluation of :math:`expr`, even if it occurs inside a
    held argument or a :code:`Hold`  form.





Create a function :math:`f` with a held argument:

>>> SetAttributes[f, HoldAll]

>>> f[1 + 2]
  = f[1 + 2]

:code:`Evaluate`  forces evaluation of the argument, even though :math:`f` has
the :code:`HoldAll`  attribute:

>>> f[Evaluate[1 + 2]]
  = f[3]
>>> Hold[Evaluate[1 + 2]]
  = Hold[3]
>>> HoldComplete[Evaluate[1 + 2]]
  = HoldComplete[Evaluate[1 + 2]]
>>> Evaluate[Sequence[1, 2]]
  = Sequence[1, 2]
