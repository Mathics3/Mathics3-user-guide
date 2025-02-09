Evaluate
========

`WMA link <https://reference.wolfram.com/language/ref/Evaluate.html>`_


:code:`Evaluate` [:math:`expr`]
    forces evaluation of :math:`expr`, even if it occurs inside a
    held argument or a :code:`Hold`  form.





Create a function :math:`f` with a held argument:

>>> SetAttributes[f, HoldAll]


>>> f[1 + 2]

    =
:math:`f\left[1+2\right]`



:code:`Evaluate`  forces evaluation of the argument, even though :math:`f` has
the :code:`HoldAll`  attribute:

>>> f[Evaluate[1 + 2]]

    =
:math:`f\left[3\right]`


>>> Hold[Evaluate[1 + 2]]

    =
:math:`\text{Hold}\left[3\right]`


>>> HoldComplete[Evaluate[1 + 2]]

    =
:math:`\text{HoldComplete}\left[\text{Evaluate}\left[1+2\right]\right]`


>>> Evaluate[Sequence[1, 2]]

    =
:math:`\text{Sequence}\left[1,2\right]`


