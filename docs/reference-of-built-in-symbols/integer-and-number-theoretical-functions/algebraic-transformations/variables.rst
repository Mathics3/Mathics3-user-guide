Variables
=========

`WMA link <https://reference.wolfram.com/language/ref/Variables.html>`_


:code:`Variables` [:math:`expr`]
    gives a list of the variables that appear in the polynomial :math:`expr`.





>>> Variables[a x^2 + b x + c]
  = {a, b, c, x}
>>> Variables[{a + b x, c y^2 + x/2}]
  = {a, b, c, x, y}
>>> Variables[x + Sin[y]]
  = {x, Sin[y]}
