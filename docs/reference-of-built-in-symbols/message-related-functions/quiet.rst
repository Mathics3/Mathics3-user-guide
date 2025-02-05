Quiet
=====

`WMA link <https://reference.wolfram.com/language/ref/Quiet.html>`_


:code:`Quiet` [:math:`expr`, {:math:`s_1`:::math:`t_1`, ...}]
    evaluates :math:`expr`, without messages :code:`{:math:`s_1`:::math:`t_1`, ...}`  being displayed.

:code:`Quiet` [:math:`expr`, All]
    evaluates :math:`expr`, without any messages being displayed.

:code:`Quiet` [:math:`expr`, None]
    evaluates :math:`expr`, without all messages being displayed.

:code:`Quiet` [:math:`expr`, :math:`off`, :math:`on`]
    evaluates :math:`expr`, with messages :math:`off` being suppressed, but messages :math:`on` being displayed.





Evaluate without generating messages:

>>> Quiet[1/0]
  = ComplexInfinity

Same as above:

>>> Quiet[1/0, All]
  = ComplexInfinity
>>> a::b = "Hello";

>>> Quiet[x+x, {a::b}]
  = 2 x
>>> Quiet[Message[a::b]; x+x, {a::b}]
  = 2 x
>>> Message[a::b]; y=Quiet[Message[a::b]; x+x, {a::b}]; Message[a::b]; y
  = 2 x
>>> Quiet[x + x, {a::b}, {a::b}]
  = Quiet[x + x, {a::b}, {a::b}]
