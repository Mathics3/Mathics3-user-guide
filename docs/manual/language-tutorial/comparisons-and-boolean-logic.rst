Comparisons and Boolean Logic
=============================

Values can be compared for equality using the operator :code:`==` :

>>> 3 == 3
  = True
>>> 3 == 4
  = False

The special symbols :code:`True`  and :code:`False`  are used to denote truth values. Naturally, there are inequality comparisons as well:

>>> 3 > 4
  = False

Inequalities can be chained:

>>> 3 < 4 >= 2 != 1
  = True

Truth values can be negated using :code:`!`  (logical `<not>`_) and combined using :code:`&&`  (logical `<and>`_) and :code:`||`  (logical `<or>`_):

>>> !True
  = False
>>> !False
  = True
>>> 3 < 4 && 6 > 5
  = True

:code:`&&`  has higher precedence than :code:`||` , i.e. it binds stronger:

>>> True && True || False && False
  = True
>>> True && (True || False) && False
  = False
