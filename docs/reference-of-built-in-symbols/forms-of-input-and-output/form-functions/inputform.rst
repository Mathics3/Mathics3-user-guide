InputForm
=========

`WMA link <https://reference.wolfram.com/language/ref/InputForm.html>`_


:code:`InputForm` [:math:`expr`]
    displays :math:`expr` in an unambiguous form suitable for input.





>>> InputForm[a + b * c]
    =

:math:`a\text{ + }b*c`


>>> InputForm["A string"]
    =

:math:`\text{\`{}\`{}A string''}`


>>> InputForm[f'[x]]
    =

:math:`\text{Derivative}\left[1\right]\left[f\right]\left[x\right]`


>>> InputForm[Derivative[1, 0][f][x]]
    =

:math:`\text{Derivative}\left[1, 0\right]\left[f\right]\left[x\right]`


