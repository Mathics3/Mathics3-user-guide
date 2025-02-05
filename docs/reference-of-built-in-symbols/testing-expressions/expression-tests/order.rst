Order
=====

`WMA link <https://reference.wolfram.com/language/ref/Order.html>`_


:code:`Order` [:math:`x`, :math:`y`]
    returns a number indicating the canonical ordering of :math:`x` and :math:`y`.          1 indicates that :math:`x` is before :math:`y`, and -1 that :math:`y` is before :math:`x`.          0 indicates that there is no specific ordering. Uses the same order          as :code:`Sort` .





>>> Order[7, 11]
  = 1
>>> Order[100, 10]
  = -1
>>> Order[x, z]
  = 1
>>> Order[x, x]
  = 0
