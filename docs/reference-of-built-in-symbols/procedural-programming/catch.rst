Catch
=====

`WMA link <https://reference.wolfram.com/language/ref/Catch.html>`_


:code:`Catch` [:math:`expr`]
    returns the argument of the first :code:`Throw`  generated in the evaluation of
    :math:`expr`.

:code:`Catch` [:math:`expr`, :math:`form`]
    returns value from the first :code:`Throw[:math:`value`, :math:`tag`]`  for which :math:`form` matches
    :math:`tag`.

:code:`Catch` [:math:`expr`, :math:`form`, :math:`f`]
    returns :math:`f`[:math:`value`, :math:`tag`].





Exit to the enclosing :code:`Catch`  as soon as :code:`Throw`  is evaluated:

>>> Catch[r; s; Throw[t]; u; v]
  = t

Define a function that can "throw an exception":

>>> f[x_] := If[x > 12, Throw[overflow], x!]


The result of :code:`Catch`  is just what is thrown by :code:`Throw` :

>>> Catch[f[1] + f[15]]
  = overflow
>>> Catch[f[1] + f[4]]
  = 25
>>> Clear[f]

