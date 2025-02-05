OptionValue
===========

`WMA link <https://reference.wolfram.com/language/ref/OptionValue.html>`_


:code:`OptionValue` [:math:`name`]
    gives the value of the option :math:`name` as specified in a call to a function with :code:`OptionsPattern` .

:code:`OptionValue` [:math:`f`, :math:`name`]
    recover the value of the option :math:`name` associated to the symbol :math:`f`.

:code:`OptionValue` [:math:`f`, :math:`optvals`, :math:`name`]
    recover the value of the option :math:`name` associated to the symbol :math:`f`, extracting the values from :math:`optvals` if available.

:code:`OptionValue` [..., :math:`list`]
    recover the value of the options in :math:`list` .





>>> f[a->3] /. f[OptionsPattern[{}]] -> {OptionValue[a]}
  = {3}

Unavailable options generate a message:

>>> f[a->3] /. f[OptionsPattern[{}]] -> {OptionValue[b]}
  = {b}

The argument of :code:`OptionValue`  must be a symbol:

>>> f[a->3] /. f[OptionsPattern[{}]] -> {OptionValue[a+b]}
  = {OptionValue[a + b]}

However, it can be evaluated dynamically:

>>> f[a->5] /. f[OptionsPattern[{}]] -> {OptionValue[Symbol["a"]]}
  = {5}
