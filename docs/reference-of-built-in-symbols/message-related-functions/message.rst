Message
=======

`WMA link <https://reference.wolfram.com/language/ref/Message.html>`_


:code:`Message` [:math:`symbol`:::math:`msg`, :math:`expr_1`, :math:`expr_2`, ...]
    displays the specified message, replacing placeholders in
    the message text with the corresponding expressions.





>>> a::b = "Hello world!"
  = Hello world!
>>> Message[a::b]

>>> a::c := "Hello `1`, Mr 00`2`!"

>>> Message[a::c, "you", 3 + 4]

