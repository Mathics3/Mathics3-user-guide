ToString
========

`WMA link <https://reference.wolfram.com/language/ref/ToString.html>`_

:code:`ToString` [:math:`expr`]
    returns a string representation of :math:`expr`.

:code:`ToString` [:math:`expr`, :math:`form`]
    returns a string representation of :math:`expr` in the form :math:`form`.





>>> ToString[2]
  = 2
>>> ToString[2] // InputForm
  = "2"
>>> ToString[a+b]
  = a + b
>>> "U" <> 2
  = U <> 2
>>> "U" <> ToString[2]
  = U2
>>> ToString[Integrate[f[x],x], TeXForm]
  = \int f\left[x\right] \, dx
