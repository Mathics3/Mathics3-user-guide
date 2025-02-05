BitLength
=========

`WMA link <https://reference.wolfram.com/language/ref/BitLength.html>`_


:code:`BitLength` [:math:`x`]
    gives the number of bits needed to represent the integer :math:`x`. :math:`x`'s sign is ignored.





>>> BitLength[1023]
  = 10
>>> BitLength[100]
  = 7
>>> BitLength[-5]
  = 3
>>> BitLength[0]
  = 0
