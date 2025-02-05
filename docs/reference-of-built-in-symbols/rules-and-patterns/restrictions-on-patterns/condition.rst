Condition
=========

`WMA link <https://reference.wolfram.com/language/ref/Condition.html>`_


:code:`Condition` [:math:`pattern`, :math:`expr`]
    same as

:code:`:math:`pattern` /; :math:`expr``
    places an additional constraint on :math:`pattern` that only           allows it to match if :math:`expr` evaluates to :code:`True` .





The controlling expression of a :code:`Condition`  can use variables from     the pattern:

>>> f[3] /. f[x_] /; x>0 -> t
  = t
>>> f[-3] /. f[x_] /; x>0 -> t
  = f[-3]

:code:`Condition`  can be used in an assignment:

>>> f[x_] := p[x] /; x>0

>>> f[3]
  = p[3]
>>> f[-3]
  = f[-3]
