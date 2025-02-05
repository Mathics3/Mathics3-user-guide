Function
========

`WMA link <https://reference.wolfram.com/language/ref/Function.html>`_


:code:`Function` [:math:`body`]
    same as

:code:`:math:`body` &`
    represents a pure function with parameters :code:`#1` , :code:`#2` , etc.

:code:`Function` [{:math:`x_1`, :math:`x_2`, ...}, :math:`body`]
    represents a pure function with parameters :math:`x_1`, :math:`x_2`, etc.

:code:`Function` [{:math:`x_1`, :math:`x_2`, ...}, :math:`body`, :math:`attr`]
    assume that the function has the attributes :math:`attr`.





>>> f := # ^ 2 &

>>> f[3]
  = 9
>>> #^3& /@ {1, 2, 3}
  = {1, 8, 27}
>>> #1+#2&[4, 5]
  = 9

You can use :code:`Function`  with named parameters:

>>> Function[{x, y}, x * y][2, 3]
  = 6

Parameters are renamed, when necessary, to avoid confusion:

>>> Function[{x}, Function[{y}, f[x, y]]][y]
  = Function[{y$}, f[y, y$]]
>>> Function[{y}, f[x, y]] /. x->y
  = Function[{y}, f[y, y]]
>>> Function[y, Function[x, y^x]][x][y]
  = x ^ y
>>> Function[x, Function[y, x^y]][x][y]
  = x ^ y

Slots in inner functions are not affected by outer function application:

>>> g[#] & [h[#]] & [5]
  = g[h[5]]

In the evaluation process, the attributes associated with an Expression are     determined by its Head.  If the Head is also a non-atomic Expression, in general,    no Attribute is assumed. In particular, it is what happens when the head     of the expression has the form:

``Function[:math:`body`]``
or:
``Function[:math:`vars`, :math:`body`]``

>>> h := Function[{x}, Hold[1+x]]

>>> h[1 + 1]
  = Hold[1 + 2]

Notice that :math:`Hold` in the body prevents the evaluation of :math:`1+x`, but not     the evaluation of :math:`1+1`. To avoid that evaluation, of its arguments, the Head     should have the attribute :code:`HoldAll` . This behavior can be obtained by using the     three arguments form version of this expression:

>>> h:= Function[{x}, Hold[1+x], HoldAll]

>>> h[1+1]
  = Hold[1 + (1 + 1)]

In this case, the attribute :code:`HoldAll`  is assumed,     preventing the evaluation of the argument :math:`1+1` before passing it     to the function body.