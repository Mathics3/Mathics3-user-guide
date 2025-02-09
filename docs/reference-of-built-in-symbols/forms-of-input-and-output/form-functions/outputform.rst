OutputForm
==========

`WMA link <https://reference.wolfram.com/language/ref/OutputForm.html>`_


:code:`OutputForm` [:math:`expr`]
    displays :math:`expr` in a plain-text form.





>>> OutputForm[f'[x]]

    =
:math:`f'\left[x\right]`


>>> OutputForm[Derivative[1, 0][f][x]]

    =
:math:`\text{Derivative}\left[1, 0\right]\left[f\right]\left[x\right]`



:code:`OutputForm`  is used by default:

>>> OutputForm[{"A string", a + b}]

    =
:math:`\left\{\text{A string}, a\text{ + }b\right\}`


>>> {"A string", a + b}

    =
:math:`\left\{\text{A string},a+b\right\}`


>>> OutputForm[Graphics[Rectangle[]]]

    =
.. image:: tmpkxjrl95x.png
    :align: center



