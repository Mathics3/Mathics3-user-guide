ToBoxes
=======

`WMA link <https://reference.wolfram.com/language/ref/ToBoxes.html>`_


:code:`ToBoxes` [:math:`expr`]
    evaluates :math:`expr` and converts the result to box form.





Unlike :code:`MakeBoxes` , :code:`ToBoxes`  evaluates its argument:

>>> ToBoxes[a + a]
  = RowBox[{2,  , a}]
>>> ToBoxes[a + b]
  = RowBox[{a, +, b}]
>>> ToBoxes[a ^ b] // FullForm
  = SuperscriptBox["a", "b"]
