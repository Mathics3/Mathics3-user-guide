MathMLForm
==========

`WMA link <https://reference.wolfram.com/language/ref/MathMLForm.html>`_


:code:`MathMLForm` [:math:`expr`]
    displays :math:`expr` as a MathML expression.





>>> MathMLForm[HoldForm[Sqrt[a^3]]]

    =
:math:`\text{<math display="block"><msqrt> <msup><mi>a</mi> <mn>3</mn></msup> </msqrt></math>}`


>>> MathMLForm[\[Mu]]

    =
:math:`\text{<math display="block"><mi>μ</mi></math>}`



# This can causes the TeX to fail
# >> MathMLForm[Graphics[Text["μ"]]]
#  = ...

= ...