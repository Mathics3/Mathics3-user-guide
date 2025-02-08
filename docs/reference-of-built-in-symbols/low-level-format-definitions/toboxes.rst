ToBoxes
=======

`WMA link <https://reference.wolfram.com/language/ref/ToBoxes.html>`_


:code:`ToBoxes` [:math:`expr`]
    evaluates :math:`expr` and converts the result to box form.





Unlike :code:`MakeBoxes` , :code:`ToBoxes`  evaluates its argument:

>>> ToBoxes[a + a]
    =

:math:`\text{RowBox}\left[\left\{\text{2},\text{ },\text{a}\right\}\right]`


>>> ToBoxes[a + b]
    =

:math:`\text{RowBox}\left[\left\{\text{a},\text{+},\text{b}\right\}\right]`


>>> ToBoxes[a ^ b] // FullForm
    =

:math:`\text{SuperscriptBox}\left[\text{\`{}\`{}a''}, \text{\`{}\`{}b''}\right]`


