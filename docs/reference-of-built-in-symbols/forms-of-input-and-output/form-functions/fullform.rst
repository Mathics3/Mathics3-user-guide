FullForm
========

`WMA link <https://reference.wolfram.com/language/ref/FullForm.html>`_


:code:`FullForm` [:math:`expr`]
    displays the underlying form of :math:`expr`.





>>> FullForm[a + b * c]

    =
:math:`\text{Plus}\left[a, \text{Times}\left[b, c\right]\right]`


>>> FullForm[2/3]

    =
:math:`\text{Rational}\left[2, 3\right]`


>>> FullForm["A string"]

    =
:math:`\text{\`{}\`{}A string''}`


