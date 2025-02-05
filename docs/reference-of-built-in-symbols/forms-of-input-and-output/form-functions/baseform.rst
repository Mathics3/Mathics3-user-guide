BaseForm
========

`WMA link <https://reference.wolfram.com/language/ref/BaseForm.html>`_


:code:`BaseForm` [:math:`expr`, :math:`n`]
    prints numbers in :math:`expr` in base :math:`n`.





A binary integer:

>>> BaseForm[33, 2]
  = 100001_2

A hexadecimal number:

>>> BaseForm[234, 16]
  = ea_16

A binary real number:

>>> BaseForm[12.3, 2]
  = 1100.01001100110011001_2
>>> BaseForm[-42, 16]
  = -2a_16
>>> BaseForm[x, 2]
  = x
>>> BaseForm[12, 3] // FullForm
  = BaseForm[12, 3]

Bases must be between 2 and 36:

>>> BaseForm[12, -3]
  = BaseForm[12, -3]
>>> BaseForm[12, 100]
  = BaseForm[12, 100]
