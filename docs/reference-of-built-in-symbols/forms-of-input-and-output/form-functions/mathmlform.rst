MathMLForm
==========

`WMA link <https://reference.wolfram.com/language/ref/MathMLForm.html>`_


:code:`MathMLForm` [:math:`expr`]
    displays :math:`expr` as a MathML expression.





>>> MathMLForm[HoldForm[Sqrt[a^3]]]
  = ...
>>> MathMLForm[\[Mu]]
  = ...

# This can causes the TeX to fail
# >> MathMLForm[Graphics[Text["μ"]]]
#  = ...

= ...