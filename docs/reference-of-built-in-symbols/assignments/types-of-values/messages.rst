Messages
========

`WMA link <https://reference.wolfram.com/language/ref/Messages.html>`_


:code:`Messages` [:math:`symbol`]
    gives the list of messages associated with :math:`symbol`.





>>> a::b = "foo"
  = foo
>>> Messages[a]
  = {HoldPattern[a::b] :> foo}
>>> Messages[a] = {a::c :> "bar"};

>>> a::c // InputForm
  = "bar"
>>> Message[a::c]

