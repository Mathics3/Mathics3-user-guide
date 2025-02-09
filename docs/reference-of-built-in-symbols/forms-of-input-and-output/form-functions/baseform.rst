BaseForm
========

`WMA link <https://reference.wolfram.com/language/ref/BaseForm.html>`_


:code:`BaseForm` [:math:`expr`, :math:`n`]
    prints numbers in :math:`expr` in base :math:`n`.





A binary integer:

>>> BaseForm[33, 2]

    =
:math:`\text{SubscriptBox}\left[\text{100001},\text{2}\right]`



A hexadecimal number:

>>> BaseForm[234, 16]

    =
:math:`\text{SubscriptBox}\left[\text{ea},\text{16}\right]`



A binary real number:

>>> BaseForm[12.3, 2]

    =
:math:`\text{SubscriptBox}\left[\text{1100.01001100110011001},\text{2}\right]`


>>> BaseForm[-42, 16]

    =
:math:`\text{SubscriptBox}\left[\text{-2a},\text{16}\right]`


>>> BaseForm[x, 2]

    =
:math:`x`


>>> BaseForm[12, 3] // FullForm

    =
:math:`\text{BaseForm}\left[12, 3\right]`



Bases must be between 2 and 36:

>>> BaseForm[12, -3]

>>> BaseForm[12, 100]

