Messages
========

`WMA link <https://reference.wolfram.com/language/ref/Messages.html>`_


:code:`Messages` [:math:`symbol`]
    gives the list of messages associated with :math:`symbol`.





>>> a::b = "foo"

    =
:math:`\text{foo}`


>>> Messages[a]

    =
:math:`\left\{\text{HoldPattern}\left[a\text{::}\text{b}\right]\text{:>}\text{foo}\right\}`


>>> Messages[a] = {a::c :> "bar"};


>>> a::c // InputForm

    =
:math:`\text{\`{}\`{}bar''}`


>>> Message[a::c]

    a::c bar


