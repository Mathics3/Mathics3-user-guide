Strings
=======

Strings can be entered with :code:`"`  as delimiters:

>>> "Hello world!"
  = Hello world!

As you can see, quotation marks are not printed in the output by default. This can be changed by using :code:`InputForm` :

>>> InputForm["Hello world!"]
  = "Hello world!"

Strings can be joined using :code:`<>` :

>>> "Hello" <> " " <> "world!"
  = Hello world!

Numbers cannot be joined to strings:

>>> "Debian" <> 6
  = Debian <> 6

They have to be converted to strings using :code:`ToString`  first:

>>> "Debian" <> ToString[6]
  = Debian6
