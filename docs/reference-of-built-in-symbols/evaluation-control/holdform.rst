HoldForm
========

`WMA link <https://reference.wolfram.com/language/ref/HoldForm.html>`_


:code:`HoldForm` [:math:`expr`]
    is equivalent to :code:`Hold[:math:`expr`]` , but prints as :math:`expr`.





>>> HoldForm[1 + 2 + 3]
  = 1 + 2 + 3

:code:`HoldForm`  has attribute :code:`HoldAll` :

>>> Attributes[HoldForm]
  = {HoldAll, Protected}
