Context
=======

`WMA link <https://reference.wolfram.com/language/ref/Context.html>`_

:code:`Context` [:math:`symbol`]
    yields the name of the context where :math:`symbol` is defined in.

:code:`Context[]`
    returns the value of :code:`$Context` .





>>> Context[a]
  = Global`
>>> Context[b`c]
  = b`
>>> InputForm[Context[]]
  = "Global`"
