FileDate
========

`WMA link <https://reference.wolfram.com/language/ref/FileDate.html>`_


:code:`FileDate` [:math:`file`, :math:`types`]
    returns the time and date at which the file was last modified.





>>> FileDate["ExampleData/sunflowers.jpg"]
  = ...
>>> FileDate["ExampleData/sunflowers.jpg", "Access"]
  = ...
>>> FileDate["ExampleData/sunflowers.jpg", "Creation"]
  = ...
>>> FileDate["ExampleData/sunflowers.jpg", "Change"]
  = ...
>>> FileDate["ExampleData/sunflowers.jpg", "Modification"]
  = ...
>>> FileDate["ExampleData/sunflowers.jpg", "Rules"]
  = ...
