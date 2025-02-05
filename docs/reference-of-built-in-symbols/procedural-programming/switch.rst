Switch
======

`WMA link <https://reference.wolfram.com/language/ref/Switch.html>`_


:code:`Switch` [:math:`expr`, :math:`pattern_1`, :math:`value_1`, :math:`pattern_2`, :math:`value_2`, ...]
    yields the first :math:`value` for which :math:`expr` matches the corresponding           :math:`pattern`.





>>> Switch[2, 1, x, 2, y, 3, z]
  = y
>>> Switch[5, 1, x, 2, y]
  = Switch[5, 1, x, 2, y]
>>> Switch[5, 1, x, 2, a, _, b]
  = b
>>> Switch[2, 1]
  = Switch[2, 1]

Notice that :code:`Switch`  evaluates each pattern before it against     :math:`expr`, stopping after the first match:

>>> a:=(Print["a->p"];p); b:=(Print["b->q"];q);

>>> Switch[p,a,1,b,2]
  = 1
>>> a=.; b=.;

