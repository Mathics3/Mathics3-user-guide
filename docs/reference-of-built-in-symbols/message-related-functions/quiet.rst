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

    =
:math:`\text{ComplexInfinity}`



Same as above:

>>> Quiet[1/0, All]

    =
:math:`\text{ComplexInfinity}`


>>> a::b = "Hello";


>>> Quiet[x+x, {a::b}]

    =
:math:`2 x`


>>> Quiet[Message[a::b]; x+x, {a::b}]

    =
:math:`2 x`


>>> Message[a::b]; y=Quiet[Message[a::b]; x+x, {a::b}]; Message[a::b]; y

    a::b Hello

    a::b Hello

    =
:math:`2 x`


>>> Quiet[x + x, {a::b}, {a::b}]

    Quiet::conflict In Quiet[x + x, {a::b}, {a::b}] the message name(s) {a::b} appear in both the list of messages to switch off and the list of messages to switch on.

    =
:math:`\text{Quiet}\left[x+x,\left\{a\text{::}\text{b}\right\},\left\{a\text{::}\text{b}\right\}\right]`


