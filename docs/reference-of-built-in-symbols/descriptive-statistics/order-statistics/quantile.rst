Quantile
========

`Quantile <https://en.wikipedia.org/wiki/Quantile>`_ (`WMA link <https://reference.wolfram.com/language/ref/Quantile.html>`_)

In statistics and probability, quantiles are cut points dividing the     range of a probability distribution into continuous intervals with     equal probabilities, or dividing the observations in a sample in the same way.

Quantile is also known as value at risk (VaR) or fractile.

:code:`Quantile` [:math:`list`, :math:`q`]
    returns the :math:`q`th quantile of :math:`list`.

:code:`Quantile` [:math:`list`, :math:`q`, {{:math:`a,b`}, {:math:`c,d`}}]
    uses the quantile definition specified by parameters :math:`a`, :math:`b`, :math:`c`, :math:`d`.
    
    For a list of length :math:`n`, :code:`Quantile` [:math:`list`, :math:`q`, {{:math:`a ,b`}, {:math:`c, d`}}] depends       on :math:`x=a+(n+b)q`.
    
    If :math:`x` is an integer, the result is :math:`s[[x]]`, where :math:`s`=:code:`Sort[list,Less]` .
    
    Otherwise, the result is:
    :code:`s[[Floor[x]]] + (s[[Ceiling[x]]] - s[[Floor[x]]])(c + d FractionalPart[x])` ,
    with the indices taken to be 1 or n if they are out of range.
    
    The default choice of parameters is :code:`{{0,0},{1,0}}` .





Common choices of parameters include:


- :code:`{{0, 0}, {1, 0}}`  inverse empirical CDF (default)

- :code:`{{0, 0}, {0, 1}}`  linear interpolation (California method)




:code:`Quantile[list,q]`  always gives a result equal to an element of list.

>>> Quantile[Range[11], 1/3]
  = 4
>>> Quantile[Range[16], 1/4]
  = 4
>>> Quantile[{1, 2, 3, 4, 5, 6, 7}, {1/4, 3/4}]
  = {2, 6}
