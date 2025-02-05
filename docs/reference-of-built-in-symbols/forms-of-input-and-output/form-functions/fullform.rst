FullForm
========

`WMA link <https://reference.wolfram.com/language/ref/FullForm.html>`_


:code:`FullForm` [:math:`expr`]
    displays the underlying form of :math:`expr`.





>>> FullForm[a + b * c]
  = Plus[a, Times[b, c]]
>>> FullForm[2/3]
  = Rational[2, 3]
>>> FullForm["A string"]
  = "A string"
