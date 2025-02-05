TagSet
======

`WMA link <https://reference.wolfram.com/language/ref/TagSet.html>`_


:code:`TagSet` [:math:`f`, :math:`expr`, :math:`value`]
    same as

:math:`f` :code:`/:`  :math:`expr` :code:`=`  :math:`value`
    assigns :math:`value` to :math:`expr`, associating the corresponding assignment           with the symbol :math:`f`.





Create an upvalue without using :code:`UpSet` :

>>> square /: area[square[s_]] := s^2

>>> DownValues[square]
  = {}
>>> UpValues[square]
  = {HoldPattern[area[square[s_]]] :> s ^ 2}

The symbol :math:`f` must appear as the ultimate head of :math:`lhs` or as the head         of an element in :math:`lhs`:

>>> x /: f[g[x]] = 3;

>>> g /: f[g[x]] = 3;

>>> f[g[x]]
  = 3
