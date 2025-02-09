SyntaxQ
=======

`WMA link <https://reference.wolfram.com/language/ref/SyntaxQ.html>`_

:code:`SyntaxQ["string"]`
    returns :code:`True`  if "string" corresponds to a syntactically correct input for a Mathics3 expression, or :code:`False`  otherwise.





>>> SyntaxQ["a[b"]

    =
:math:`\text{False}`


>>> SyntaxQ["a[b]"]

    =
:math:`\text{True}`


