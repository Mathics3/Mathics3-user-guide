Context
=======

`WMA link <https://reference.wolfram.com/language/ref/Context.html>`_

:code:`Context` [:math:`symbol`]
    yields the name of the context where :math:`symbol` is defined in.

:code:`Context[]`
    returns the value of :code:`$Context` .





>>> Context[a]

    =
:math:`\text{Global\`{}}`


>>> Context[b`c]

    =
:math:`\text{b\`{}}`


>>> InputForm[Context[]]

    =
:math:`\text{\`{}\`{}Global\`{}''}`


